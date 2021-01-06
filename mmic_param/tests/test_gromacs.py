"""
Unit and regression test for the mmic_param package.
"""

# Import package, test suite, and other packages as needed
import mmic_param
import mmelemental
import pytest
import sys, os

def test_automartini_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mmic_param" in sys.modules

from mmic_param.components import PrepComponent
from mmic_param.models.input import ParamInput, ComputeInput
from mmic_param.components.gmx.compute_component import ComputeComponent 
from mmic_param.components.gmx.post_component import PostComponent

fpath = os.path.join('mmic_param', 'data', 'molecules', 'dialanine.pdb')

mol = mmelemental.models.molecule.mm_molecule.Molecule.from_file(fpath)

############## VACUUM ################
# Prepare input for molecule in vacuum
paramInput = ParamInput(mol=mol, forcefield='amber99', engine='gmx')
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
