[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/MolSSI/mmic_param/workflows/CI/badge.svg)](https://github.com/MolSSI/mmic_param/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/MolSSI/mmic_param/branch/master/graph/badge.svg)](https://codecov.io/gh/MolSSI/mmic_param/branch/master)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/MolSSI/mmic_param.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/MolSSI/mmic_param/context:python)

Forcefield parameter association component
========================================
This is part of the [MolSSI](http://molssi.org) Molecular Mechanics Interoperable Components ([MMIC](https://github.com/MolSSI/mmic)) project. This package provides a component for generating parametrized molecules from existing force fields.

<p align="center">
<img src="mmic_param/data/ff_component.png">
</p>

# Basic Usage
```python
# Import main component for running the computation
from mmic_param import RunComponent

# Import the param input and molecule models that comply with MMSchema
from mmic_param.models.input import ParamInput
from mmelemental.models.molecule import Mol

# Create an MMSchema molecule
mol = Mol.from_file(path_to_file)

# Create input for Amber99 FF (optionally) using the GMX engine
paramInput = ParamInput(mol=mol, forcefield='amber99', engine='gmx')
paramOutput = RunComponent.compute(paramInput)

# Extract MMSchema mol and and its associated ff object
mol, ff = paramOutput.mol, paramOutput.ff
```

# Models and subcomponents
This component provided 4 models derived from MMSchema: 
- [ParamInput](https://github.com/MolSSI/mmic_param/blob/master/mmic_param/models/input.py#L8)
- [ComputeInput](https://github.com/MolSSI/mmic_param/blob/master/mmic_param/models/input.py#L14)
- [ParamOutput](https://github.com/MolSSI/mmic_param/blob/master/mmic_param/models/output.py#L12)
- [ComputeOutput](https://github.com/MolSSI/mmic_param/blob/master/mmic_param/models/output.py#L8)

```python
from mmic_param.models.input import ParamInput, ComputeInput, ParamOutput, ComputeOutput
```

This component provided 3 subcomponents for associating the force field parameters to a given MMSchema molecule: 
- [PrepComponent](https://github.com/MolSSI/mmic_param/blob/master/mmic_param/components/prep_component.py#L7)
- [ComputeComponent](https://github.com/MolSSI/mmic_param/blob/master/mmic_param/components/post_component.py#L5)
- [PostComponent](https://github.com/MolSSI/mmic_param/blob/master/mmic_param/components/post_component.py#L5)

```python
from mmic_param.components import PrepComponent, ComputeComponent, PostComponent
```
# Supported engines
- [GMX pdb2gmx](https://manual.gromacs.org/documentation/5.1/onlinehelp/gmx-pdb2gmx.html): part of the [Gromacs](https://www.gromacs.org) software suite
- [Auto Martini](https://github.com/tbereau/auto_martini): automated [MARTINI](http://www.cgmartini.nl) forcefield mapping and parametrization of small organic molecules.

# Supported forcefields
- [Amber94](https://pubs.acs.org/doi/abs/10.1021/ja00124a002): Second Generation Amber-based force field for the simulation of proteins, nucleic acids, and organic molecules
- [Amber96](): 
- [Amber99](): 
- [Amber99-ILDN]
- [Amber99SB-ILDN](https://pubmed.ncbi.nlm.nih.gov/20408171): Amber-based force field which improves side-chain torsion potentials for the Amber ff99SB protein force field. 
- [Amber03](https://onlinelibrary.wiley.com/doi/abs/10.1002/jcc.10349): Point‐charge force field for molecular mechanics simulations of proteins
- [AMBERGS]
- [Martini](https://pubs.acs.org/doi/10.1021/jp071097f#:~:text=The%20new%20version%2C%20coined%20the,large%20number%20of%20chemical%20compounds):  Coarse-grained force field for biomolecular simulations & organic molecules.
- [Charmm27]():
- [Gromos96-43a1]
- [Gromos96-43a2]
- [Gromos96-45a3]
- [Gromos96-53a5]
- [Gromos96-53a6]
- [Gromos96-54a7]
- [OPLS-AA](https://pubs.acs.org/doi/abs/10.1021/jp003919d): OPLS-based force field for proteins

#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.1.
