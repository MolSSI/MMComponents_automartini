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


from mmic_param.components import PrepComponent, ComputeComponent
from mmic_param.models.input import ParamInput, ComputeInput

fpath = os.path.join('mmic_param', 'data', 'ibuprofen', 'ibu.gro')

mol = mmelemental.models.molecule.mm_molecule.Molecule.from_file(fpath)

# Prepare input
paramInput = ParamInput(mol=mol, forcefield='charmm27')
computeInput = PrepComponent.compute(paramInput)

# Compute FF params for molecule
computeOutput = ComputeComponent.compute(computeInput)

# Convert file objects to MM objects
# paramOutput = PostComponent.compute(computeOutput)