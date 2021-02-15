"""
Unit and regression test for the mmic_ffpa package.
"""

# Import package, test suite, and other packages as needed
import mmic_ffpa
import pytest
import sys


def test_automartini_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mmic_ffpa" in sys.modules
