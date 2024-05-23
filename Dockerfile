FROM nvidia/cuda:11.7.1-cudnn8-devel-ubuntu22.04

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y tzdata
ENV TZ Asia/Tokyo

RUN apt-get update && apt-get install -y \
    libopencv-dev \
    python3.9 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

RUN pip install torch==2.0.1+cu117 torchvision==0.15.2+cu117 --index-url https://download.pytorch.org/whl/cu117 \
    && pip install 'git+https://github.com/facebookresearch/fvcore'

RUN git clone https://github.com/facebookresearch/detectron2 detectron2_repo \
    && cd detectron2_repo \
    && pip install .

RUN git clone https://github.com/facebookresearch/pytorchvideo.git \
    && cd pytorchvideo \
    && pip install .

ENV PYTHONPATH=/workspace:$PYTHONPATH

COPY . /workspace

RUN python3 setup.py build develop

RUN pip install torchinfo
