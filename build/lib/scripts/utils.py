#Gathering information from DFT (different I/O)



#Gathering information from phonopy, convert J/mol unit systems to ev


#      T [K]      F [kJ/mol]    S [J/K/mol]  C_v [J/K/mol]     E [kJ/mol]
#Older version has data organised as: T(K) F(kJ/mol)  S(J/K/mol) Cv(J/Kmol)  U(kJ/mol).
#Newer version has data organised as: T(K) F(eV/cell) U(eV/cell) Cv(kB/cell) -TS(eV/cell)

#The calculated values are written into thermal_properties.yaml. 
# The unit systems of free energy, heat capacity, and entropy are kJ/mol, J/K/mol, and J/K/mol, respectively, 
# where 1 mol means your input unit cell (not formula unit).

import pandas as pd
from scipy import constants

kJmol2eV = 1000 * constants.physical_constants['joule-electron volt relationship'][0] / constants.N_A 

def phonon_Jmol2eV(file_in='phonopy_in/BaS.dat', file_out='phonopy_output/BaS_n.dat'):
    with open(file_out, 'w+') as f:
        data = pd.read_csv(file_in,  comment="#", delim_whitespace=True, names=["T", "F", "S", "Cv", "U"])
        T = data.iloc[:,0]
        F = data.iloc[:,1] * kJmol2eV 
        S = data.iloc[:,2]
        C_v = data.iloc[:,3] / (constants.Boltzmann  * constants.N_A )
        U = data.iloc[:,4] * kJmol2eV 
        TS = -(T * S) * kJmol2eV /1000 

        f.write('# Phonon free energy and specific heat from phonopy-VASP'+'\n')
        f.write(f'# Phonon zero point energy = {F[0]}'+'\n')
        f.write(str('#    Temperature (K)') +'   ' +str('Free energy (eV/cell)') +'   '+str('Internal energy (eV/cell)' )+'   '+str(' c_v (kB/cell)')+'   '+ str('-TS_vib(eV/cell)') +'\n')
        for i in range(len(T)):
            f.write(str(T[i]) + '   ' + str(F[i]) + '   '+ str(U[i]) + '   '+ str(C_v[i]) + '   '+ str(TS[i]) + '\n') 



