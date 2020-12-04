Component for Forcefield Parametrization
==============================

[//]: # (Badges)
[![Travis Build Status](https://travis-ci.com/REPLACE_WITH_OWNER_ACCOUNT/MMComponents_automartini.svg?branch=master)](https://travis-ci.com/REPLACE_WITH_OWNER_ACCOUNT/MMComponents_automartini)
[![AppVeyor Build status](https://ci.appveyor.com/api/projects/status/REPLACE_WITH_APPVEYOR_LINK/branch/master?svg=true)](https://ci.appveyor.com/project/REPLACE_WITH_OWNER_ACCOUNT/MMComponents_automartini/branch/master)
[![codecov](https://codecov.io/gh/REPLACE_WITH_OWNER_ACCOUNT/MMComponents_automartini/branch/master/graph/badge.svg)](https://codecov.io/gh/REPLACE_WITH_OWNER_ACCOUNT/MMComponents_automartini/branch/master)

A component for generating parametrized molecules from existing force fields.

<p align="center">
<img src="mmic_forcefield/data/ff_component.png">
</p>

Supported forcefields:
- [Amber99SB-ILDN](https://pubmed.ncbi.nlm.nih.gov/20408171): Amber-based force field which improves side-chain torsion potentials for the Amber ff99SB protein force field. 
- [Martini](https://pubs.acs.org/doi/10.1021/jp071097f#:~:text=The%20new%20version%2C%20coined%20the,large%20number%20of%20chemical%20compounds):  Coarse-grained force field for biomolecular simulations.

Supported engines:
- [Auto Martini](https://github.com/tbereau/auto_martini): automated [MARTINI](http://www.cgmartini.nl) forcefield mapping and parametrization of small organic molecules.

#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.1.
