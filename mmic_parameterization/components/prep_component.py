from mmic.components.blueprints.generic_component import GenericComponent
from mmelemental.models.util.output import FileOutput
from mmic_parameterization.models import ForceFieldInput

class PrepComponent(GenericComponent):
    """ A component for converting a Molecule object to a FileOutput. """
    @classmethod
    def input(cls):
        return ForceFieldInput

    @classmethod
    def output(cls):
        return FileOutput
