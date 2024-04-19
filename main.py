import numpy as np
import torch
import torch.nn.functional as F
from ml_collections import config_flags

_CONFIG = config_flags.DEFINE_config_file('config')

def main():
    params = _CONFIG.value
    return 1

if __name__ == '__main__':
    main()