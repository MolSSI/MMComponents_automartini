from mmelemental.models.base import Base
from mmelemental.models.forcefield import ForceField
from mmelemental.models.molecule.mm_molecule import Molecule
from mmelemental.models.util.input import FileInput
from pydantic import Field
from typing import Union, Optional

class ParamInput(Base):
	forcefield: str = Field(..., description = 'Force field name e.g. charmm36.')
	solv_forcefield: Optional[str] = Field(None, description = 'Solvent force field name e.g. tip3p.')
	mol: Molecule = Field(..., description = 'Molecule object. See :class: ``Molecule``.')
	engine: str = Field(..., description = 'Engine name. See supported engines in :tuple:``mmic_param.components.engines``.')

class ComputeInput(Base):
	forcefield: str = Field(..., description = 'Force field file name e.g. charmm36.')
	solv_forcefield: Optional[str] = Field(None, description = 'Solvent force field name e.g. tip3p.')
	mol: str = Field(..., description = 'Molecule file contents.')
	engine: str = Field(..., description = 'Engine name. See supported engines in :tuple:``mmic_param.components.engines``.')