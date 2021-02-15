"""
Unit and regression test for the mmic_ffpa package.
"""

# Import package, test suite, and other packages as needed
import mmic_ffpa
import mmelemental
import pytest
import sys, os


def test_automartini_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mmic_ffpa" in sys.modules


from mmic_ffpa.components import PrepComponent
from mmic_ffpa.models.input import ParamInput, ComputeInput
from mmic_ffpa.components.gmx.compute_component import ComputeComponent
from mmic_ffpa.components.gmx.post_component import PostComponent

fpath = os.path.join("mmic_ffpa", "data", "molecules", "dialanine.pdb")

mol = mmelemental.models.molecule.Molecule.from_file(fpath)

############## VACUUM ################
# Prepare input for molecule in vacuum
paramInput = ParamInput(mol=mol, forcefield="amber99", engine="gmx")
computeInput = PrepComponent.compute(paramInput)

# Compute FF params for molecule using gromacs
computeOutput = ComputeComponent.compute(computeInput)

# Convert file objects to MM objects
paramOutput = PostComponent.compute(computeOutput)
print(paramOutput.mol)

############## SOLVENT ##############
# Prepare input for molecule in vacuum
# paramInput = ParamInput(mol=mol, forcefield='amber99', solv_forcefield='tip3p', engine='gmx')
# computeInput = PrepComponent.compute(paramInput)

# Compute FF params for molecule using gromacs
# computeOutput = ComputeComponent.compute(computeInput)
