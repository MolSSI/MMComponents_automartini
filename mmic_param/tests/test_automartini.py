"""
Unit and regression test for the mmic_param package.
"""

# Import package, test suite, and other packages as needed
import mmic_param
import pytest
import sys

def test_automartini_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mmic_param" in sys.modules
