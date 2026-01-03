"""
hydra-swmm
"""


from swmm_api import swmm5_run
from . import core
from . import utils
from . import rain
from .rain import chicago_list_2

__title__ = 'hydra-swmm'
__version__ = '0.0.1'


__all__ = [
    "core",
    "utils",
    "rain",
    "swmm5_run",
    "chicago_list_2"
]