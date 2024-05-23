#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.

"""Add custom configs and default values"""
from fvcore.common.config import CfgNode


def add_custom_config(_C):
    # Add your own customized configs.
    _C.GRADCAM = CfgNode()
    _C.GRADCAM.ENABLE = False
    _C.GRADCAM.LAYER = "s5.pathway0_res2"
