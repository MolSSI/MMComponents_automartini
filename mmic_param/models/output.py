from mmelemental.models.base import Base
from mmelemental.models.forcefield import ForceField
from mmelemental.models.molecule.mm_molecule import Molecule
from mmelemental.models.util.input import FileInput
from pydantic import Field

class ComputeOutput(Base):
	forcefield: FileInput = Field(..., description = 'Force field params file object. See :class:`FileInput`.')
	mol: FileInput = Field(..., description = 'Molecule file object. See :class: ``FileInput``.')

class ParamOutput(Base):
	forcefield: ForceField = Field(..., description = 'Force field object. See :class:`ForceField`.')
	mol: Molecule = Field(..., description = 'Molecule object. See :class: ``Molecule``.')