from mmelemental.models import Molecule, ForceField, ProcOutput
from .input import AssignInput
from pydantic import Field
from typing import Optional, Dict


__all__ = ["AssignOutput"]


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
