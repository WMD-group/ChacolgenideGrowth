def main():
    from materials
    import numpy as np

    from plot_potential import plot_potential

    T = np.linspace(600,1200,100)    # K
    P = np.array( np.logspace(1,7,100),ndmin=2).transpose() # Pa
    
    #D_mu_S8 = 1/8*(S8.mu_kJ(T, P) - alpha_S.mu_kJ(T, P))
    mu_S2 = 1/2*S2.mu_kJ(T, P)
    mu_Ss = 1/8 *alpha_S.mu_kJ(T, P)
    mu_S8 = 1/8 * S8.mu_kJ(T, P)
    D_mu = 1/2 * S2.mu_kJ(T, P) - 1/8 *alpha_S.mu_kJ(T, P)
    #D_mu = 1/2* S2.mu_kJ(T, P) - 1/8 * S8.mu_kJ(T, P)
    
    E_Ss = (-.12378465E+04) - (-.12377738E+04) + (1) * (mu_Ss) * 0.0103636 + (+2)*(3.15+0.846)
    E_S8 = (-.12378465E+04) - (-.12377738E+04) + (1) * (mu_S8) * 0.0103636 + (+2)*(3.15+0.846)
    E_S2 = (-.12378465E+04) - (-.12377738E+04) + (1) * (mu_S2) * 0.0103636 + (+2)*(3.15+0.846)
    kbt = (1.380649e-23) * T / (1.6e-19)
    n_S2 = np.log10(1 * 64 * np.exp(-E_S2/kbt))
    n_S8 = np.log10(1 * 64 * np.exp(-E_S8/kbt))
    n_Ss = np.log10(1 * 64 * np.exp(-E_Ss/kbt))
    
    
    n =(- D_mu * 1000 / ((1.380649e-23) * (6.0221408e+23) * T))
    
    D_mu_label = 'ln(n(V$_{S}$)/n(V$_{S(ref)}$))'
    formation = 'V$_{S}$$^{+2}$ formation energy (eV)'
    con_label= 'V$_{S}$$^{+2}$ Defect concentration (log10)'
    scale_range = [0,35]
    
    #plot_potential(T,P,E_S2,formation,scale_range,filename='plots/FormationS2.png')
    plot_potential(T,P,mu_Ss,con_label,scale_range,filename='plots/muSs_y.png')
    plot_potential(T,P,E_S8,con_label,scale_range,filename='plots/E8.png')
    plot_potential(T,P,n_S2,con_label,scale_range,filename='plots/ConcentrationS2_y.png')
    plot_potential(T,P,n_S8,con_label,scale_range,filename='plots/ConcentrationS8_y.png')
    plot_potential(T,P,n_Ss,con_label,scale_range,filename='plots/ConcentrationSs_y.png')

if __name__ == "__main__":
    main()
