
ChalcogenideGrowth thermodynamic modelling package
====================================================

![Reactions](https://user-images.githubusercontent.com/25340554/228510930-f5993dfe-71e3-4050-809c-72b789a363aa.png)

Contents
--------
1. Determining the T(temperature) and P(pressure) conditions for growing chalcogenides;
2. Determining Defect concentration

Prerequist
--------
1. DFT calculations
2. Phonopy calculations

Installation
--------
git clone https://github.com/WMD-group/ChalcogenideGrowth.git
cd ChalcogenideGrowth
python setup install

Procedures
--------
* Growth reaction path

  Reaction 1:

  BaS + ZnS --> BaZrS3 (solid state)

  Reaction 2:

  Ba + Zr + S --> BaZrS3 (S flux)

* Creating materials instances for each reactants and products in the reaction (Reaction 1 as an example). 
    ```python

    BZS =solid(
        name='BaZrS3',
        pbesol_energy_eV= -1079.5348,
        fu_cell=32,
        volume=3901.173919,
        phonons='phonopy_output/BaS_n.dat',
        N=5
    )

    BaS =solid(
        name='BaS',
        pbesol_energy_eV= -.42876562E+02,
        fu_cell=4,
        volume=257.548609,
        phonons='phonopy_output/BaS_n.dat',
        N=2
    )

    ZrS =solid(
        name='ZrS2',
        pbesol_energy_eV= -.22548979E+02,
        fu_cell=1,
        volume=67.175661,
        phonons='phonopy_output/ZrS_n.dat',
        N=3
    )
    ```






Examples
============================
Example
-------

Each material is made available as an object in the module namespace,
and has methods which retrieve various properties. For example, to
generate a CSV file containing the chemical potentials of a selection of phases:

``` python
import csv
import numpy as np
from materials import CZTS_kesterite, Cu, beta_Sn, alpha_Sn
from materials import Cu2S, SnS2, SnS, Sn2S3, ZnS, S2, S8

T = np.arange(400, 1200, 50)

titles = []
data = []
for material in (CZTS_kesterite, Cu, beta_Sn,
                 alpha_Sn, Cu2S, SnS2,
                 SnS, Sn2S3, ZnS, S2, S8):

    titles.append(material.name)
    data.append(list(material.mu_kJ(T, 1E5)))

# Zip and list unpacking can be used together to transpose
# a matrix expressed as a list of lists
data = zip(*data)

with open('mu_data_Jmol.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(titles)
    writer.writerows(data)
```


Publications
============================

BaZrS3 growth
--------


2D Transition Metal Dichalcogenide growth
--------



CZTS thermodynamic modelling
--------

[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.57130.svg)](http://dx.doi.org/10.5281/zenodo.57130)

Research data and calculations for ab initio thermodynamic modelling of
the formation and decomposition of Cu<sub>2</sub>ZnSnS<sub>4</sub> (CZTS).

This repository acts as supplementary information for a [2014 publication in *J. Mater. Chem. A*](http://dx.doi.org/10.1039/C4TA00892H), and is also an active project currently hosted at
[http://github.com/WMD-Group/CZTS-model](http://github.com/WMD-Group/CZTS-model).
The [releases](https://github.com/WMD-group/CZTS-model/releases) correspond to key publication points in the project:

* [report-confirmation](https://github.com/WMD-group/CZTS-model/releases/tag/report-confirmation) [ajjackson](https://github.com/ajjackson)'s 1st year PhD confirmation report. [Not public]
* [v1.0](https://github.com/WMD-group/CZTS-model/releases/tag/v1.0) Initial submission to *J. Mater. Chem. A*.
* [v1.2a](https://github.com/WMD-group/CZTS-model/releases/tag/v1.2a) Supporting data for publication in *J. Mater. Chem. A.*. Includes minor bug fixes and data for comparison with [another study](https://dx.doi.org/10.1021/cm202379s), with permission from Jonathan Scragg.
* [thesis-submission](https://github.com/WMD-group/CZTS-model/releases/tag/thesis-submission) Supporting data for ajjackson PhD thesis submission. [Initial submission is not public]



(c) Adam Jackson 2016
This code is made available under the GNU General Public Licence (GPL) v3.
See the LICENSE file for the full text.

