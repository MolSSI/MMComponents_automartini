from mmcomponents.components.blueprints.generic_component import GenericComponent
from mmelemental.models.util.output import FileOutput
from mmelemental.models.molecule.mm_molecule import Molecule

class PrepComponent(GenericComponent):
    """ A component for converting a Molecule object to a FileOutput. """
    @classmethod
    def input(cls):
        return Molecule

    @classmethod
    def output(cls):
        return FileOutput