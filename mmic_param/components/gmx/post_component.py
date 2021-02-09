from mmelemental.models.util.output import FileOutput
from mmelemental.models.forcefield import ForceField
from mmelemental.models.molecule import Mol
from ..post_component import PostComponent
from mmic_param.models.output import ParamOutput 
from typing import Dict, Any, List, Tuple, Optional

class PostComponent(PostComponent):
    def execute(
        self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, Dict[str, Any]]:

        ff, mol = inputs.forcefield, inputs.mol
        mol_name = FileOutput.rand_name() + '.gro'
        ff_name = FileOutput.rand_name() + '.top'

        with FileOutput(path=mol_name, clean=True) as fp:
            fp.write(mol)
            with FileOutput(path=ff_name, clean=True) as fp:
                fp.write(ff)
                mol = Mol.from_file(mol_name, ff_name)
                #top = ForceField.from_file(mol_name, ff_name)

        return True, ParamOutput(mol=mol)