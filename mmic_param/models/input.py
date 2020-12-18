from mmelemental.models.base import Base
from mmelemental.models.forcefield import ForceField
from mmelemental.models.molecule.mm_molecule import Molecule
from mmelemental.models.util.input import FileInput
from pydantic import Field
from typing import Union

class ParamInput(Base):
	forcefield: Union[ForceField, str] = Field(..., description = 'Force field object or name e.g. charmm36. See :class:`ForceField`.')
	mol: Molecule = Field(..., description = 'Molecule object. See :class: ``Molecule``.')

class ComputeInput(Base):
	forcefield: Union[FileInput, str] = Field(..., description = 'Force field file object or name e.g. charmm36. See :class:`FileInput`.')
	mol: FileInput = Field(..., description = 'Molecule file object. See :class:`FileInput`.')