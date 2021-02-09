from mmic.components.blueprints.generic_component import GenericComponent
from typing import Dict, Any, List, Tuple, Optional
from mmic_param.models.output import ComputeOutput, ParamOutput 

__all__ = ['PostComponent']

class PostComponent(GenericComponent):
    """ A component for constructing Molecule & ForceField objects from parsing mol/top/ff files. """
    @classmethod
    def input(cls):
        return ComputeOutput

    @classmethod
    def output(cls):
        return ParamOutput

    def execute(
        self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, Dict[str, Any]]:
        raise NotImplementedError