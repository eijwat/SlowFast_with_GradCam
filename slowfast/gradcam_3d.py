import numpy as np
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt


def gradcam_3d(feat, gradient, input_shape, apply_batch=0):
    # feat: [B, C, T, H, W]
    # outputs: [CLS]
    b = apply_batch
    B, C, T, H, W = feat.shape

    feat_v = gradient.view(B, C, T * H * W)
    alpha = torch.mean(feat_v[b], axis=1)
    lgradcam = F.relu(torch.sum(feat[b].view(C, T, H, W) * alpha.view(-1, 1, 1, 1), 0))
    lgradcam = F.interpolate(
        lgradcam.view(1, 1, T, H, W),
        size=(input_shape[-3], input_shape[-2], input_shape[-1]),
        mode="trilinear",
    )
    lgradcam /= torch.max(lgradcam)

    return lgradcam.detach()


class LayerGradHookContext:
    def __init__(self, model, target_layer):
        self.model = model
        self.target_layer = target_layer
        self.feats = None
        self.gradient = None
        self.hooks = []

    def __enter__(self):
        self.hooks.append(self.target_layer.register_forward_hook(self.hook_forward_fn))
        self.hooks.append(self.target_layer.register_backward_hook(self.hook_backward_fn))
        return self

    def __exit__(self, type, value, traceback):
        for hook in self.hooks:
            hook.remove()

    def hook_forward_fn(self, module, input, output):
        self.feats = output.detach()

    def hook_backward_fn(self, module, grad_input, grad_output):
        self.gradient = grad_output[0].detach()


def plot_movie(data, cam, suffix, alpha=0.5):
    data = data.permute(1, 2, 3, 0).cpu().numpy()
    cam = cam.squeeze().cpu().numpy()
    color_map = plt.get_cmap("jet")
    cam = color_map(cam)
    frames_combined = (1 - alpha) * data + alpha * cam[..., :3]

    # 合成したフレームを表示
    _, axs = plt.subplots(data.shape[0], 2, figsize=(10, 80))
    for i, ax in enumerate(axs):
        ax[0].imshow(data[i])
        ax[1].imshow(frames_combined[i])
        ax[0].axis('off')
        ax[1].axis('off')
    plt.tight_layout()
    plt.savefig(f"gradcam_out/gradcam_{suffix}.png")
