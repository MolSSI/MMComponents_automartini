from mmic.components.blueprints.generic_component import GenericComponent
from typing import Dict, Any, List, Tuple, Optional
from mmic_param.models.output import ComputeOutput, ParamOutput 

class PostComponent(GenericComponent):
    """ A component for constructing a ForceField object from parsing force field files. """
    @classmethod
    def input(cls):
        return ComputeOutput

    @classmethod
    def output(cls):
        return ParamOutput