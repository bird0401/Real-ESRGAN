# flake8: noqa
from os.path import dirname, abspath
import sys

parent_dir = dirname(dirname(abspath(__file__)))
sys.path.append(parent_dir)

import os.path as osp
from basicsr.train import train_pipeline

import realesrgan.archs
import realesrgan.data
import realesrgan.models

if __name__ == '__main__':
    root_path = osp.abspath(osp.join(__file__, osp.pardir, osp.pardir))
    train_pipeline(root_path)
