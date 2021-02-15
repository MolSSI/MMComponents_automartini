from mmelemental.models.base import Base
from mmelemental.models.molecule import Molecule
from pydantic import Field
from typing import Optional


class ParamInput(Base):
    forcefield: str = Field(..., description="Force field name e.g. charmm36.")
    solv_forcefield: Optional[str] = Field(
        None, description="Solvent force field name e.g. tip3p."
    )
    mol: Molecule = Field(..., description="Molecule object. See :class: ``Molecule``.")
    engine: str = Field(
        ...,
        description="Engine name. See supported engines in :tuple:``mmic_ffpa.components.engines``.",
    )


class ComputeInput(Base):
    forcefield: str = Field(..., description="Force field file name e.g. charmm36.")
    solv_forcefield: Optional[str] = Field(
        None, description="Solvent force field name e.g. tip3p."
    )
    mol: str = Field(..., description="Molecule file contents.")
    engine: str = Field(
        ...,
        description="Engine name. See supported engines in :tuple:``mmic_ffpa.components.engines``.",
    )
