from mmic_param.models.input import ComputeInput
from mmic_param.models.output import ComputeOutput 
from mmelemental.components.util.cmd_component import CmdComponent
from mmelemental.models.util.output import FileOutput

from typing import Any, Dict, List, Tuple, Optional

__all__ = ['ComputeComponent']

class ComputeComponent(CmdComponent):
    """ A template component for generating a pramaterized molecule. 
    Cmd process: build_input() -> run() -> parse_output().
    build_input() and parse_output() must be implemented at the specific component 
    (engine) level. See gmx, auto_martini, etc. dirs. """
    @classmethod
    def input(cls):
        return ComputeInput

    @classmethod
    def output(cls):
        return ComputeOutput

    def execute(
        self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, Dict[str, Any]]:
        """ 
        Writes Molecule as a pdb file and then calls: 
        ComputeComponent.build_input() -> ComputeComponent.parse_output()
        Both methods must be implemented in specific engines see for e.g. gmx
        """
        ff, mol = inputs.forcefield, inputs.mol
        input_model = inputs.dict()
        fname = FileOutput.rand_name() + '.pdb'

        with FileOutput(path=fname) as fp:
            fp.write(mol)
            input_model['mol'] = fp.abs_path

        input_model['clean_files'] = fp
        return super().execute(input_model)

    def build_input(
        self,
        input_model: Dict[str, Any],
        config: Optional["TaskConfig"] = None,
        template: Optional[str] = None,
    ) -> Dict[str, Any]:
        raise NotImplementedError

    def parse_output(
        self, 
        output: Dict[str, str], 
        inputs: Dict[str, Any]
    ) -> ComputeOutput:
        raise NotImplementedError