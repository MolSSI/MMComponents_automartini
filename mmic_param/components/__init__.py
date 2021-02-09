from .compute_component import *
from .post_component import *
from .prep_component import *
from collections.abc import Mapping
import os


class _findEngines(Mapping):
    @staticmethod
    def engines():
        comp_dir = __path__[0]
        engines = [
            eng for eng in next(os.walk(comp_dir))[1] if not eng.startswith("__")
        ]
        return tuple(engines)


engines = _findEngines.engines()
