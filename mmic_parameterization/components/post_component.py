from mmcomponents.components.blueprints.generic_component import GenericComponent
from mmelemental.models.util.input import FileInput
from mmelemental.models.molecule.mm_molecule import Molecule
from typing import Dict, Any, List, Tuple, Optional

from mmelemental.models.forcefield.atomtype import ForceField

class PostComponent(GenericComponent):
    """ A component for constructing a ForceField object from parsing force field files. """
    @classmethod
    def input(cls):
        return FileInput

    @classmethod
    def output(cls):
        return ForceField