from mmelemental.models import Molecule, ForceField, ProcInput
from pydantic import Field
from typing import Optional, Dict, Union

__all__ = ["AssignInput"]


class AssignInput(ProcInput):
    molecule: Dict[str, Molecule] = Field(
        ...,
        description="Molecular mechanics molecule object(s). See the :class:``Molecule`` class. "
        "Example: mol = {'ligand': Molecule, 'receptor': Molecule, 'solvent': Molecule}.",
    )
    forcefield: Union[Dict[str, ForceField], Dict[str, str]] = Field(
        ...,
        description='Forcefield object(s) or name(s) for every Molecule defined in "molecule".',
    )
