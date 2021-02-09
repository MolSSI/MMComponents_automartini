from mmelemental.models.base import Base
from mmelemental.models.forcefield import ForceField
from mmelemental.models.molecule import Mol
from mmelemental.models.util.output import ComputeOutput
from pydantic import Field


class ComputeOutput(ComputeOutput):
    forcefield: str = Field(..., description="Force field params file string object.")
    mol: str = Field(..., description="Molecule file string object.")


class ParamOutput(Base):
    forcefield: ForceField = Field(
        ..., description="Force field object. See :class:`ForceField`."
    )
    mol: Mol = Field(..., description="Molecule object. See :class: ``Molecule``.")
