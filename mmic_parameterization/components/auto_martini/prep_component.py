from mmelemental.models.util.input import FileOutput
from mmelemental.models.molecule.mm_molecule import Molecule
from typing import List, Tuple, Optional

import mmcomponents_forcefield

class PrepComponent(mmcomponents_forcefield.components.PrepComponent):
    """ A component for preparing input for auto_martini from MMSchema. """

    def execute(
        self,
        inputs: Molecule,
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, FileOutput]:

        if inputs.identifiers:
            filename = 'some_name.sdf'
            inputs.to_file(filename)
        else:
            filename = 'some_name.gro'
            inputs.to_file(filename)

        return True, FileOutput(path='some_name.gro')