from mmelemental.models.util.output import ComputeOutput
from mmelemental.models import Molecule, ForceField, ProcOutput
from .input import AssignInput
from pydantic import Field
from typing import Optional, Dict


class AssignOutput(ProcOutput):
    proc_input: AssignInput = Field(..., description="Procedure input schema.")
    molecule: Dict[str, Molecule] = Field(
        ...,
        description="Molecular mechanics molecule object(s). See the :class:``Molecule`` class. "
        "Example: mol = {'ligand': Molecule, 'receptor': Molecule, 'solvent': Molecule}.",
    )
    forcefield: Dict[str, ForceField] = Field(
        ...,
        description="Forcefield object(s).",
    )


class ComputeOutput(ComputeOutput):
    proc_input: AssignInput = Field(
        None, description="Procedure input schema."
    )  # must become required field, eventually
    forcefield: str = Field(..., description="Force field params file string object.")
    molecule: str = Field(..., description="Molecule file string object.")
