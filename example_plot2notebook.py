################################################################################
#  Copyright Adam J. Jackson (2014)                                            #
#                                                                              #
#   This program is free software: you can redistribute it and/or modify       #
#   it under the terms of the GNU General Public License as published by       #
#   the Free Software Foundation, either version 3 of the License, or          #
#   (at your option) any later version.                                        #
#                                                                              #
#   This program is distributed in the hope that it will be useful,            #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of             #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              #
#   GNU General Public License for more details.                               #
#                                                                              #
#   You should have received a copy of the GNU General Public License          #
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.      #
################################################################################
from materials import solid, ideal_gas
import numpy as np
from plot_potential import plot_potential
from utils import phonon_Jmol2eV

##Step1: convert phonopy calculated information
#phonon_Jmol2eV(file_in='phonopy_in/BaS.dat', file_out='phonopy_output/BaS_n.dat')

##Step2: Plot!
#For one example reaction
CZTS_kesterite = solid(name='Kesterite CZTS',
                        stoichiometry={'Cu':2,'Zn':1,'Sn':1,'S':4},
                        pbesol_energy_eV=-0.706480597450521e06,
                        fu_cell=2, #formula_unit in calculation cell
                        volume=310.86645888987351,
                        phonons='phonopy_output/czts-conventional.dat', #same name as file_out in the phonopy_output folder
                        N=8 #number of atoms per formula_unit
                       )

CZTS = CZTS_kesterite

Cu = solid(name='Cu',
           stoichiometry={'Cu':1},
           pbesol_energy_eV=-180838.168712673,
           fu_cell=4,
           volume=45.2576997892,
           phonons='phonopy_output/Cu.dat'
)

beta_Sn = solid(name='Beta Sn',
                stoichiometry={'Sn':1},
                pbesol_energy_eV=-0.340581412216286E+06,
                fu_cell=2,
                volume=53.538071915,
                phonons='phonopy_output/beta_Sn.dat'
)
Sn = beta_Sn

Zn = solid(name='Zn',
           stoichiometry={'Zn':1},
           pbesol_energy_eV=-0.981596036898606e05, 
           fu_cell=2,
           volume=28.2580218348,
           phonons='phonopy_output/Zn.dat'
)

S8=ideal_gas(
    name='S8',
    stoichiometry={'S':8},
    pbesol_energy_eV=-0.868936310037924e05,
    thermo_file='nist_janaf/S8.dat',
    zpe_pbesol=0.32891037,
    N=8
)

T = np.linspace(100,1500,100)    # K
P = np.array(np.logspace(1,7,100),ndmin=2).transpose() # Pa

#Recommended levels = 10 in kJ/mol unit; 
#Recommended levels = 0.01 in eV unit.
D_mu = CZTS.mu_kJ(T,P) - (2*Cu.mu_kJ(T,P) +
                                Zn.mu_kJ(T,P) +
                                Sn.mu_kJ(T,P) +
                                0.5*S8.mu_kJ(T,P)
    )

D_mu_label = '$\Delta G_f$ / kJ mol$^{-1}$'
scale_range = [-380,-240]

plot_potential(T,P,D_mu,D_mu_label,scale_range, filename='plots/DG_CZTS_S8_new.png', color='summer',levels=0.01)

