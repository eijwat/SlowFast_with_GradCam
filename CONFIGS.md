# Configについて

## Configの全体概要
Configで設定できる値の全体の概要を以下に示します。

1. CONTRASTIVE: コントラストモデル設定、MoCo, SimCLR, SwAV, BYOLなどのコントラスト学習モデルに使用されるパラメータの設定。
    * T: コントラスト損失のための温度パラメータ。
    * DIM: 損失の出力次元。
    * LENGTH: kNNバンク用の訓練サンプル数。
    * QUEUE_LEN: MoCoのキューの長さやメモリバンクのサイズ。
    * MOMENTUM: モーメンタムエンコーダーの更新に使用されるモーメンタム。
    * MOMENTUM_ANNEALING: モーメンタムのアニーリング（徐々に減少させる）を行うかどうか。
    * TYPE: コントラスト学習のタイプ（例: memorybank, moco, simclr, byol, swav）。
    * INTERP_MEMORY: メモリバンクを時間的に補間するかどうか。
    * MEM_TYPE: メモリのタイプ（1dまたは2d）。
    * NUM_CLASSES_DOWNSTREAM: 下流のクラス数。
    * NUM_MLP_LAYERS: MLPプロジェクションの層数。
    * MLP_DIM: プロジェクションと予測MLPの次元。
    * BN_MLP: MLPにバッチ正規化を使用するかどうか。
    * BN_SYNC_MLP: MLPの同期バッチ正規化を使用するかどうか。
    * LOCAL_SHUFFLE_BN: バッチ正規化のシャッフルをローカルにのみ行うかどうか。
    * MOCO_MULTI_VIEW_QUEUE: キューに複数のクリップを埋め込むかどうか。
    * DELTA_CLIPS_MIN: 複数のクリップをサンプリングする場合、最小フレーム間隔。
    * DELTA_CLIPS_MAX: 最大フレーム間隔。
    * PREDICTOR_DEPTHS: 使用する予測器の深さを指定。
    * SEQUENTIAL: 複数のクリップを順次処理するか、バッチ処理するか。
    * SIMCLR_DIST_ON: SimCLR損失をマシン間で行うかどうか。
    * SWAV_QEUE_LEN: SwAVで使用するキューの長さ。
    * KNN_ON: 訓練中のオンラインkNN評価を行うかどうか。
2. BN: バッチ正規化オプション、バッチ正規化に関する設定。
    * USE_PRECISE_STATS: 正確なBN統計を使用するかどうか。
    * NUM_BATCHES_PRECISE: 正確なBNを計算するために使用するバッチの数。
    * WEIGHT_DECAY: BNに適用される重み減衰の値。
    * NORM_TYPE: 正規化のタイプ（batchnorm, sub_batchnorm, sync_batchnorm）。
    * NUM_SPLITS: SubBatchNormのパラメータ。バッチ次元を分割し、各々で独立にBNを実行。
    * NUM_SYNC_DEVICES: NaiveSyncBatchNormで統計を同期するデバイスの数。
    * GLOBAL_SYNC: NaiveSyncBatchNormで全デバイス間の統計をグローバルに同期するかどうか。
3. TRAIN: 訓練オプション、モデルの訓練に関する設定。
    * EVAL_PERIOD: 評価周期（エポック単位）。
    * CHECKPOINT_PERIOD: チェックポイントの保存周期（エポック単位）。
    * AUTO_RESUME: 出力ディレクトリの最新チェックポイントから訓練を再開するかどうか。
    * CHECKPOINT_FILE_PATH: 初期ウェイトを読み込むためのチェックポイントのパス。
    * CHECKPOINT_TYPE: チェックポイントのタイプ（caffe2 または pytorch）。
    * CHECKPOINT_INFLATE: チェックポイントを読み込む際に膨張（inflate）を行うかどうか。
    * CHECKPOINT_EPOCH_RESET: チェックポイントを読み込む際にエポックをリセットするかどうか。
    * CHECKPOINT_CLEAR_NAME_PATTERN: 特定のパターンに従ってレイヤー名をクリアするかどうか。
    * MIXED_PRECISION: アクティベーションにFP16を使用するかどうか。
    * CHECKPOINT_IN_INIT: ImageNetモデルから一部のパラメータを膨張させるかどうか。
4. AUG: 拡張オプション、データ拡張に関する設定。
    * ENABLE: ランダム拡張を有効にするかどうか。
    * NUM_SAMPLE: 訓練中に使用する繰り返し拡張の数。
    * COLOR_JITTER: カラージッターの強度。
    * AA_TYPE: RandAugパラメータ。
    * INTERPOLATION: 補間方法。
    * RE_PROB: ランダム消去の確率。
    * RE_MODE: ランダム消去モード。
    * RE_COUNT: ランダム消去の回数。
    * RE_SPLIT: 最初の拡張分割でランダム消去を行わないかどうか。
    * GEN_MASK_LOADER: 画像処理中に入力マスクを生成するかどうか。
    * MASK_TUBE: マスキングモードが "tube" かどうか。
    * MASK_FRAMES: マスキングモードが "frame" かどうか。
    * MASK_WINDOW_SIZE: 生成されるマスクのサイズ。
    * MASK_RATIO: マスクされたトークンの全トークンに対する比率。
    * MAX_MASK_PATCHES_PER_BLOCK: マスクされる最大ブロック数。
5. TEST: テストオプション、モデルのテストに関する設定。
    * ENABLE: テストを行うかどうか。
    * DATASET: テストに使用するデータセット。
    * BATCH_SIZE: バッチサイズ。
    * CHECKPOINT_FILE_PATH: 初期ウェイトを読み込むためのチェックポイントのパス。
    * NUM_ENSEMBLE_VIEWS: 予測結果を集約するためにビデオから一様にサンプリングするクリップ数。
    * NUM_SPATIAL_CROPS: 予測結果を集約するためのフレームから空間的にサンプリングするクロップ数。
    * CHECKPOINT_TYPE: チェックポイントのタイプ。
    * SAVE_RESULTS_PATH: 予測結果ファイルを保存するパス。
    * NUM_TEMPORAL_CLIPS: 時間的クリップの数。
6. RESNET: ResNetオプション、ResNetアーキテクチャに特有の設定。
    * TRANS_FUNC: 変換関数のタイプ。
    * NUM_GROUPS: グループの数。
    * WIDTH_PER_GROUP: グループごとの幅。
    * INPLACE_RELU: reluをインプレースで適用するかどうか
    * STRIDE_1X1: 1x1畳み込みにストライドを適用するかどうか。
    * ZERO_INIT_FINAL_BN: 各ブロックの最後のBNのガンマをゼロで初期化するかどうか。
    * ZERO_INIT_FINAL_CONV: 各ブロックの最終畳み込み層をゼロで初期化するかどうか。
    * DEPTH: ネットワークの深さ。
    * NUM_BLOCK_TEMP_KERNEL: 特定のブロック数以上で、残りのブロックに対して時間的カーネルサイズ1を使用。
    * SPATIAL_STRIDES: 異なる解像度ステージの空間的ストライドサイズ。
    * SPATIAL_DILATIONS: 異なる解像度ステージの空間的拡張サイズ。
7. X3D: X3Dオプション、X3Dモデルに関する設定。
    * WIDTH_FACTOR: 幅の拡張因子。
    * DEPTH_FACTOR: 深さの拡張因子。
    * BOTTLENECK_FACTOR: 3x3x3畳み込みのボトルネック拡張因子。
    * DIM_C5: 分類前の最後の線形層の次元。
    * DIM_C1: 最初の3x3畳み込み層の次元。
    * SCALE_RES2: Res2の幅をスケールするかどうか。
    * BN_LIN5: 分類器の前にBN層を使用するかどうか。
    * CHANNELWISE_3x3x3: 残差ブロックの中心でチャネルワイズ（深さ方向）畳み込みを使用するかどうか。
8. NONLOCAL: NonLocalオプション
    * LOCATION: ノンローカルレイヤーを追加するステージとブロックのインデックス。
    * GROUP: 各ステージでのノンローカルのグループ数。
    * INSTANTIATION: ノンローカルレイヤーのインスタンス化方法（例：dot_product）。
    * POOL: ノンローカルで使用するプーリングレイヤーのサイズ。
9. MODEL: Modelオプション
    * ARCH: モデルアーキテクチャ。(c2d, slow, slowfast, slow_c2d, mvit, i3d, x3d, r2plus1d, maskmvit)
    * MODEL_NAME: モデル名。
    * NUM_CLASSES: 予測するクラスの数。
    * LOSS_FUNC: 損失関数。
    * SINGLE_PATHWAY_ARCH: 単一経路アーキテクチャのリスト。
    * MULTI_PATHWAY_ARCH: 複数経路アーキテクチャのリスト。
    * DROPOUT_RATE: バックボーンの最終プロジェクション前のドロップアウト率。
    * DROPCONNECT_RATE: Resブロックのランダムドロップ率。
    * FC_INIT_STD: FCレイヤーを初期化するための標準偏差。
    * HEAD_ACT: 出力ヘッドのアクティベーションレイヤー。
    * ACT_CHECKPOINT: GPUメモリ節約のためのアクティベーションチェックポインティングの有無。
    * DETACH_FINAL_FC: 最終FCレイヤーをネットワークから切り離すかどうか。
    * FROZEN_BN: 訓練中にBNの統計を凍結するかどうか。
    * FP16_ALLREDUCE: 勾配のAllReduceをFP16で圧縮するかどうか。
10. MVIT: MViTオプション
    * MODE: パッチ化のモード（例: conv, max）。
    * POOL_FIRST: 注意力計算でプロジェクション前にプールを行うかどうか。
    * CLS_EMBED_ON: トランスフォーマー内でCLS埋め込みを使用するかどうか。
    * PATCH_KERNEL: パッチ化のためのカーネルサイズ。
    * PATCH_STRIDE: パッチ化のためのストライドサイズ。
    * PATCH_PADDING: パッチ化のためのパディングサイズ。
    * PATCH_2D: 2Dパッチを使用するかどうか。
    * EMBED_DIM: トランスフォーマーの基本埋め込み次元。
    * NUM_HEADS: トランスフォーマーのヘッド数。
    * MLP_RATIO: MLPレイヤーの次元削減比率。
    * QKV_BIAS: 注意力のFCレイヤーにバイアス項を使用するかどうか。
    * DROPPATH_RATE: トランスフォーマーのドロップパス率。
    * LAYER_SCALE_INIT_VALUE: レイヤースケールの初期値。
    * DEPTH: トランスフォーマーの深さ。
    * NORM: トランスフォーマーの正規化レイヤー。
    * DIM_MUL: レイヤーiでの次元の倍増比率。
    * HEAD_MUL: レイヤーiでのヘッド数の倍増比率。
    * POOL_KV_STRIDE: KVのプールストライドサイズ。
    * POOL_KV_STRIDE_ADAPTIVE: KVのストライドサイズを適応的に調整するかどうか。
    * POOL_Q_STRIDE: Qのプールストライドサイズ。
    * POOL_KVQ_KERNEL: KVQのカーネルサイズ。
    * ZERO_DECAY_POS_CLS: 位置埋め込みとCLS埋め込みに対して減衰を行わないかどうか。
    * NORM_STEM: ステム後の正規化を使用するかどうか。
    * SEP_POS_EMBED: 個別の位置埋め込みを使用するかどうか。
    * DROPOUT_RATE: MViTバックボーンのドロップアウト率。
    * USE_ABS_POS: 絶対位置埋め込みを使用するかどうか。
    * REL_POS_SPATIAL: 空間次元に対して相対位置埋め込みを使用するかどうか。
    * REL_POS_TEMPORAL: 時間次元に対して相対位置埋め込みを使用するかどうか。
    * REL_POS_ZERO_INIT: 相対位置埋め込みをゼロで初期化するかどうか。
    * RESIDUAL_POOLING: 残差プーリング接続を使用するかどうか。
    * DIM_MUL_IN_ATT: 注意ブロックのQKV線形レイヤーで次元を増やすかどうか。
    * SEPARATE_QKV: 注意ブロックでQ、K、Vの線形レイヤーを個別に使用するかどうか。
    * HEAD_INIT_SCALE: ヘッドパラメータの初期スケールファクター。
    * USE_MEAN_POOLING: パッチトークンの平均プーリングを出力として使用するかどうか。
    * USE_FIXED_SINCOS_POS: 固定されたsin-cos位置埋め込みを使用するかどうか。
11. MASK: Maskオプション
    * ENABLE: マスクされたスタイルの事前学習を有効にするかどうか。
    * MAE_ON: MAE（マスクされたオートエンコーダー）を有効にするかどうか。
    * MAE_RND_MASK: MAEにおけるランダムマスキングを行うかどうか。
    * PER_FRAME_MASKING: MAEでフレームごとにランダムマスキングを行うかどうか。
    * TIME_STRIDE_LOSS: 時間的にストライドされたパッチのみに損失を適用するか、全時間範囲に適用するか。
    * NORM_PRED_PIXEL: 予測されたピクセルの損失を正規化するかどうか。
    * SCALE_INIT_BY_DEPTH: レイヤーの深さによる初期化を固定するかどうか。
    * DECODER_EMBED_DIM: デコーダーのトランスフォーマーの基本埋め込み次元。
    * DECODER_SEP_POS_EMBED: デコーダーの別個の位置埋め込みを使用するかどうか。
    * DEC_KV_KERNEL: デコーダーでKVカーネルを使用するかどうか。
    * DEC_KV_STRIDE: デコーダーでKVストライドを使用するかどうか。
    * PRETRAIN_DEPTH: 予測ヘッドの入力として使用される特徴の深さ。
    * HEAD_TYPE: マスクされた事前学習の予測ヘッドのタイプ。
    * DECODER_DEPTH: MAEデコーダーの深さ。
    * PRED_HOG: HOGターゲット損失の重み。
12. SLOWFAST: SlowFastオプション
    * BETA_INV: SlowとFastパスウェイ間のチャネル削減比の逆数。
    * ALPHA: SlowとFastパスウェイ間のフレームレート減少比。
    * FUSION_CONV_CHANNEL_RATIO: FastパスウェイからSlowパスウェイへの情報融合時のチャネル比。
    * FUSION_KERNEL_SZ: FastパスウェイからSlowパスウェイへの情報融合に使用されるカーネルの次元。
13. DATA: データオプション、データ処理に関する設定。
    * PATH_TO_DATA_DIR: データディレクトリへのパス。
    * NUM_FRAMES: 入力クリップのフレーム数。
    * SAMPLING_RATE: 入力クリップのサンプリングレート。
    * MEAN: ビデオの生ピクセルのRGBチャンネルごとの平均値。
    * STD: RGBチャンネルごとの標準偏差。
    * TRAIN_JITTER_SCALES: 訓練用の空間的ジッタースケール。
    * TRAIN_CROP_SIZE: 訓練用の空間的クロップサイズ。
    * TEST_CROP_SIZE: テスト用の空間的クロップサイズ。
    * TARGET_FPS: 入力ビデオを変換する目標FPS。
    * TRAIN_JITTER_FPS: 訓練時のFPSジッターの範囲。
    * DECODING_BACKEND: デコーディングのバックエンド。
    * RANDOM_FLIP: 訓練中にランダムに水平フリップを行うかどうか。
    * MULTI_LABEL: メトリックとしてmapを計算するかどうか。
14. SOLVER: ソルバーオブション
    * BASE_LR: 基本学習率。
    * LR_POLICY: 学習率ポリシー。
    * GAMMA: 指数減衰因子。
    * STEP_SIZE: expおよびcosポリシーにおけるステップサイズ（エポック単位）。
    * STEPS: 'steps_'ポリシーにおけるステップ（エポック単位）。
    * LRS: 'steps_'ポリシーでの学習率。
    * COSINE_END_LR: 'cosine'ポリシーの最終学習率。
    * MAX_EPOCH: 最大エポック数。
    * MOMENTUM: モーメンタム。
    * WEIGHT_DECAY: 重み減衰（L2正則化）。
    * WARMUP_FACTOR: ウォームアップ期間中の基本学習率の乗数。
    * WARMUP_EPOCHS: 学習率をウォームアップするエポック数。
    * WARMUP_START_LR: ウォームアップ開始時の学習率。
    * OPTIMIZING_METHOD: 最適化手法。
    * BASE_LR_SCALE_NUM_SHARDS: 基本学習率をNUM_SHARDSでスケールするかどうか。
    * COSINE_AFTER_WARMUP: ウォームアップ後にピークのコサイン学習率から開始するかどうか。
    * ZERO_WD_1D_PARAM: 1次元パラメータ（バイアスなど）に対して重み減衰を行わないかどうか。
    * CLIP_GRAD_VAL: オプティマイザー更新前にこの値で勾配をクリップするかどうか。
    * CLIP_GRAD_L2NORM: オプティマイザー更新前にこのノルムで勾配をクリップするかどうか。
    * LARS_ON: LARSオプティマイザーを使用するかどうか。
    * LAYER_DECAY: レイヤーごとの学習率の減衰率。1.0に設定すると減衰なし。
    * BETAS: Adamのベータパラメータ。
15. DATA_LOADER: データローダオプション
    * NUM_WORKERS: トレーニングプロセスごとのデータローダーワーカーの数。
    * PIN_MEMORY: データをピン留めされたホストメモリにロードするかどうか。
    * ENABLE_MULTI_THREAD_DECODE: マルチスレッドデコーディングを有効にするかどうか。
16. DETECTION: 検出オプション
    * ENABLE: ビデオ検出を有効にするかどうか。
    * ALIGNED: RoIのアラインメントバージョン。
    * SPATIAL_SCALE_FACTOR: 空間スケールファクター。
    * ROI_XFORM_RESOLUTION: RoI変換解像度。
17. DATA: データオプション
    * TRAIN_PCA_EIGVAL: PCAジッターの固有値（RGBベース）。
    * TRAIN_PCA_EIGVEC: PCAジッターの固有ベクトル。
    * PATH_TO_PRELOAD_IMDB: ローカルファイルにダンプされたIMDBへのパス。
    * INPUT_CHANNEL_NUM: 入力フレームチャンネルの次元数のリスト。
    * TRAIN_JITTER_SCALES_RELATIVE: インセプションスタイルのエリアベースランダムリサイズ拡張の相対スケール範囲。
    * TRAIN_JITTER_ASPECT_RELATIVE: インセプションスタイルのエリアベースランダムリサイズ拡張の相対アスペクト比範囲。
    * USE_OFFSET_SAMPLING: ストライド長の均一な時間的サンプリングを適用するかどうか。
    * TRAIN_JITTER_MOTION_SHIFT: 拡張のためにモーションシフトを適用するかどうか。
    * DECODING_SHORT_SIZE: デコーディングでの短いサイズのリサイズ。
    * INV_UNIFORM_SAMPLE: スケールのサンプリング方法。
    * SSL_COLOR_JITTER: SSLベースのSimCLR / MoCo v1/v2カラー拡張を適用するかどうか。
    * SSL_COLOR_BRI_CON_SAT: 明るさ、コントラスト、彩度のためのカラージッターの割合。
    * SSL_COLOR_HUE: 色相のためのカラージッターの割合。
    * SSL_MOCOV2_AUG: SimCLR / MoCo v2の拡張を適用するかどうか。
    * SSL_BLUR_SIGMA_MIN: SimCLR / MoCo v2のぼかし拡張の最小ガウスシグマ。
    * SSL_BLUR_SIGMA_MAX: 最大ガウスシグマ。
    * IN22K_TRAINVAL: IN21kで訓練/検証分割を結合するかどうか。
    * IN22k_VAL_IN1K: IN21kの訓練中にIN1kを検証分割として使用するかどうか。
    * IN_VAL_CROP_RATIO: 大解像度モデルが使用する異なるクロップ比率。
    * DUMMY_LOAD: Kinetics.pyで実際のビデオを使用しないかどうか。
18. DEMO: デモオプション
    * ENABLE: デモモードでモデルを実行するかどうか。
    * LABEL_FILE_PATH: クラス名とIDのマッピングを提供するjsonファイルへのパス。
    * WEBCAM: 入力としてカメラデバイスを指定するかどうか（-1の場合は入力ビデオを使用）。
    * INPUT_VIDEO: デモのための入力ビデオパス。
    * DETECTRON2_CFG: 検出タスクのためのDetectron2オブジェクト検出モデル設定。
    * DETECTRON2_WEIGHTS: Detectron2オブジェクト検出モデルの事前学習済みウェイトへのパス。
    * DETECTRON2_THRESH: Detectron2で予測されたバウンディングボックスを選択するためのスコア閾値。
    * DISPLAY_WIDTH: 入力ビデオデータのカスタム幅。
    * DISPLAY_HEIGHT: 入力ビデオデータのカスタム高さ。
    * BUFFER_SIZE: 連続するクリップ間のオーバーラップフレーム数。
    * OUTPUT_FILE: 可視化出力をこのビデオファイルに書き込むパス。
    * OUTPUT_FPS: 出力ビデオファイルのフレームレート。
    * INPUT_FORMAT: デモビデオリーダーからの入力フォーマット（"RGB" または "BGR"）。
    * NUM_VIS_INSTANCES: ビデオ可視化のためのプロセス数。
    * PREDS_BOXES: 事前に計算された予測ボックスへのパス。
    * THREAD_ENABLE: マルチスレッドビデオリーダーを使用するかどうか。
    * NUM_CLIPS_SKIP: 予測と可視化の頻度を減らすためにスキップするクリップ数。
    * GT_BOXES: グラウンドトゥルースボックスとラベルのパス（オプション）。
    * STARTING_SECOND: バウンディングボックスファイルに対するビデオの開始秒数。
    * FPS: 入力ビデオ/画像フォルダのフレームレート。
    * VIS_MODE: トップk予測または特定の閾値以上の予測を可視化する方法。
    * COMMON_CLASS_THRES: 一般的なクラス名の閾値。
    * UNCOMMON_CLASS_THRES: 一般的でないクラス名の閾値。
    * COMMON_CLASS_NAMES: AVAデータセット内のクラス名の分布に基づいて選択された一般的なクラス名のリスト。
    * SLOWMO: 可視化されたビデオのスローモーションレート。
19. その他
    * TASK: 現在のタスクの名前。
    * NUM_GPUS: 使用するGPUの数。
    * NUM_SHARDS: ジョブに使用するマシンの数。
    * SHARD_ID: 現在のマシンのインデックス。
    * OUTPUT_DIR: 出力のベースディレクトリ。
    * RNG_SEED: 乱数生成のためのシード。
    * LOG_PERIOD: ログの周期（イテレーション単位）。
    * LOG_MODEL_INFO: モデル情報をログに記録するかどうか。
    * DIST_BACKEND: 分散バックエンド。


## モデルの指定について

MODEL.MODEL_NAMEでモデルの指定を行います。
現状使用できるモデルは以下です。

* contrastiveモデル
  * ContrastiveModel
* maskedモデル
  * MaskMViT
* ptv(pytorchvideo)モデル
  * PTVResNet
  * PTVSlowFast
  * PTVX3D
  * PTVCSN
  * PTVR2plus1D
  * PTVMViT
* videoモデル
  * SlowFast
  * ResNet
  * X3D
  * MViT

上記のそれぞれのモデルに対して、MODEL.ARCHでアーキテクチャを指定できます。
それぞれのモデルでARCHの使用方法が異なるため、それぞれ説明します。

### contrastiveモデル
contrastiveモデルではARCHはバックボーンのモデルを指定するパラメタになります。

* slowfast: SlowFast
* slow: ResNet
* c2d: ResNet
* i3d: ResNet
* slow_c2d: ResNet
* x3d: X3D
* mvit: MViT

### maskedモデル
maskedモデルではARCHは使用されません。

### ptvモデル・videoモデル
ptvモデルおよびvideoモデルの場合ARCHはプーリング層に与えるパラメタになります。
以下のアーキテクチャが用意されています。実際のパラメタはそれぞれプーリング層のカーネルサイズとストライドのサイズとして主に使用されます。

* 2d: [[1, 1, 1]],
* c2d: [[2, 1, 1]],
* slow_c2d: [[1, 1, 1]],
* i3d: [[2, 1, 1]],
* slow_i3d: [[1, 1, 1]],
* slow: [[1, 1, 1]],
* slowfast: [[1, 1, 1], [1, 1, 1]],
* x3d: [[1, 1, 1]],


## NonLocalのオプションについて
NONLOCALで与えられるオプションに関して更に詳細に説明します。

### LOCATION
このパラメータは、NonLocalレイヤを追加するネットワーク内の特定のステージとブロックの位置を指定します。
位置の選択は、モデルがどの程度の範囲の特徴を考慮に入れるかに直接影響します。早い段階でNonLocalレイヤを使用すると、より広範囲の特徴を捉えることができる可能性がありますが、計算コストが増加する可能性もあります。

例:

```yaml
LOCATION: [[[]], [[1, 3]], [[1, 3, 5]], [[]]]
```

### GROUP
このパラメータは、各NonLocalブロックで使用されるグループの数を定義します。グループ化されたNonLocal演算は、計算効率を高めるために特徴マップをグループに分割して処理します。

グループ数を増やすと計算効率が向上する可能性がありますが、一方で特徴間の相互作用を十分に捉えられなくなる可能性があります。

### INSTANTIATION
NonLocalの具体的な実装方法を指定します。"dot_product"と"softmax"があります。デフォルトは"softmax"です。

### POOL
NonLocal内で使用されるプーリングレイヤのサイズを指定します。この設定は、NonLocal演算の前後に適用されるプーリング操作に影響します。

プーリングサイズを大きくすると、特徴マップの空間的な解像度が低下し、計算コストが減少しますが、細かい特徴情報が失われる可能性があります。


## 選択できるパラメタについて
今回のデータセットの形式と使用しているビデオデコーダの関係でvideoモデルのみが使用できる形になります。
NONLOCALのパラメタに関しては、SlowFastで以下の設定値が使用されています。

* MODEL.LOCATIONは以下の3パターン
  * [[[]], [[]], [[]], [[]]]
  * [[[]], [[1, 3]], [[1, 3, 5]], [[]]]
  * [[[], []], [[], []], [[6, 13, 20], []], [[], []]]
* MODEL.GROUPは以下の2パターン
  * [[1], [1], [1], [1]]
  * [[1, 1], [1, 1], [1, 1], [1, 1]]
* MODEL.INSTANTIATIONは以下の2パターン
  * softmax
  * dot_product
* MODEL.POOLは以下の3パターン
  * 設定なし
  * [[[1, 2, 2], [1, 2, 2]], [[1, 2, 2], [1, 2, 2]], [[1, 2, 2], [1, 2, 2]], [[1, 2, 2], [1, 2, 2]]]
  * [[[2, 2, 2], [2, 2, 2]], [[2, 2, 2], [2, 2, 2]], [[2, 2, 2], [2, 2, 2]], [[2, 2, 2], [2, 2, 2]]]
