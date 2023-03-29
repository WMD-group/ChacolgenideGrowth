import numpy as np
from scripts.materials import Cu, Zn, Sn, alpha_S, CZTS_kesterite, CZTS_stannite
from scripts.materials import Cu2S_low, ZnS_zincblende, ZnS_wurtzite, SnS2, SnS_pcma
from scripts.materials import Cu2SnS3_mo1, Cu2SnS3_mo2
from matplotlib import pyplot as plt

from itertools import cycle
lines = ["-","--","-."]
linecycler = cycle(lines)

T = np.linspace(0,1200,100)  # K
P = 1E5                      # Pa

for material in (Cu, Zn, Sn, alpha_S, CZTS_kesterite, CZTS_stannite,
                 Cu2S_low, ZnS_zincblende, ZnS_wurtzite, SnS2, SnS_pcma,
                 Cu2SnS3_mo1, Cu2SnS3_mo2):
    plt.plot(T,(material.mu_kJ(T,P)-material.mu_kJ(0,P))/material.N,next(linecycler),
             label=material.name)

#plt.axis([0,1200,0,3])
plt.xlabel('Temperature (K)')
plt.ylabel('$\Delta \mu$ (kJ atom mol$^{-1}$)')
plt.legend(loc=3)
plt.savefig('plots/Delta_mu.pdf')
plt.show()
