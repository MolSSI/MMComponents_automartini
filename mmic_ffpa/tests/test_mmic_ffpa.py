"""
Unit and regression test for the mmic_ffpa package.
"""

# Import package, test suite, and other packages as needed
import mmic_ffpa
from mmic_ffpa.models import AssignInput, AssignOutput
from mmic_ffpa.components import *
import pytest
import sys


def test_mmic_docking_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mmic_ffpa" in sys.modules


def test_mmic_docking_input():
    ...
