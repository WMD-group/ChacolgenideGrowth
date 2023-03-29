import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def plot_potential(T,P,potential,potential_label,scale_range,filename=False,
                   precision="%1.3f",T_units='K',P_units='Pa', color='summer'):

    mpl.rcParams['font.family'] = 'serif'
    mpl.rcParams['font.serif'] = 'Times New Roman'
    mpl.rcParams['font.size'] = 16

    # Unit conversions (all calculations are in SI units, conversion needed for plots)
    if T_units=='K':
        x_values = T
        x_unitlabel = 'K'
    elif T_units=='C':
        x_values = T - 273.15
        x_unitlabel = '$^\circ$ C'
    else:
        raise ValueError('Invalid temperature unit: {0}'.format(T_units))


    if P_units=='Pa':
        y_values = P.flatten()
    elif P_units=='Bar' or P_units=='bar':
        y_values = P.flatten()*1E-5
    elif P_units=='mbar': 
        y_values = P.flatten()*1E-5*1E3
    elif P_units=='kPa':
        y_values = P.flatten()*1E-3
    elif P_units=='mmHg' or P_units=='torr':
        y_values = P.flatten()*760/(1.01325E5)
    else:
        raise ValueError('Invalid pressure unit: {0}.'.format(T_units))

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    vmin=scale_range[0]
    vmax=scale_range[1]
    #levels = np.arange(vmin, vmax, 0.01)
    a = plt.contour(x_values,y_values,potential,10, linewidths = 1, colors = 'k')
    cmap = plt.get_cmap(color)
    plt.pcolormesh(x_values,y_values,potential,
    #              cmap=plt.get_cmap('BuPu'),vmin=scale_range[0], vmax=scale_range[1])
                   cmap=cmap,vmin=vmin, vmax=vmax)
    colours = plt.colorbar()
    plt.xlabel('Temperature / {0}'.format(x_unitlabel))    
    plt.ylabel('Pressure / {0}'.format(P_units))
    colours.set_label(potential_label, labelpad=20)
    ax.set_yscale('log')
    plt.clabel(a, fmt=precision)
    if filename:
        plt.savefig(filename,dpi=200)
    else:
        plt.show()
