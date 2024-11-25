from fit_file import X_sq
import numpy as np
import matplotlib.pyplot as plt

file=np.loadtxt("Practicum6/data.txt", delimiter=' ').T
f=file[0]
A=file[1]
phi=file[2]*np.pi/180

f_E = np.ones_like(f)*0.01
A_E = np.ones_like(f)*0.5
phi_E = np.ones_like(f)*5*np.pi/180

if False:
    x, x_E, y, y_E = f, f_E, A, A_E
    plt.errorbar(x, y, xerr=x_E, yerr=y_E, fmt='o', color='black', label='Datapunten', capsize=4)

    # Add labels, title, and legend
    plt.xlabel('x-label')
    plt.ylabel('y-label')
    plt.title('Titel')
    plt.legend()
    plt.grid(True)

    plt.show()
    
if False:
    param_names = ['F', 'w', 'm', 'n']
    initial_guess = [1, 1, 1, 1]

    def model(params, x):
        F, w, m, n = params
        return F/( m*np.sqrt((w**2 - x**2)**2 + (x*(n/m))**2) )
    
    data = ((f, f_E), (A, A_E))

    X_sq(data, param_names, initial_guess, model,
        root_attempts=None, datafile=None,
        VERBOSE=False, LaTeX=True,
        PLOT=True, graf1_title='Fit voor hoog energetische straling', graf1_x_label='dikte Al [mm]', graf1_y_label='$ln(I) [arb. eenh.]$'
        )
    
if True:
    param_names = ['w', 'm', 'n']
    initial_guess = [1.69, 0.07, 0.006]

    def model(params, x):
        w, m, n = params
        return (x*(n/m))/(w**2-x**2)
    
    data = ((f, f_E), (np.tan(phi), np.tan(phi_E)))

    X_sq(data, param_names, initial_guess, model,
        root_attempts=None, datafile=None,
        VERBOSE=False, LaTeX=True,
        PLOT=True, graf1_title='Fit voor hoog energetische straling', graf1_x_label='dikte Al [mm]', graf1_y_label='$ln(I) [arb. eenh.]$'
        )