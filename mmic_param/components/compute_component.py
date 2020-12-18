from mmic.components.blueprints.generic_component import GenericComponent
from mmic_param.models.input import ComputeInput
from mmic_param.models.output import ComputeOutput 

class ComputeComponent(GenericComponent):
    """ A component for converting a Molecule object to a FileOutput. """
    @classmethod
    def input(cls):
        return ComputeInput

    @classmethod
    def output(cls):
        return ComputeOutput
