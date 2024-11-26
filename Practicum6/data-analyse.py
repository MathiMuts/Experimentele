from fit_file import X_sq
import numpy as np
import matplotlib.pyplot as plt

file=np.loadtxt("Practicum6/data.txt", delimiter=' ').T
file2=np.loadtxt("Practicum6/data2.txt", delimiter=' ').T

f=file[0]
A=file[1]
phi=file[2]*np.pi/180

f2=file2[0]
A2=file2[1]
phi2=file2[2]*np.pi/180


f_E = np.ones_like(f)*0.01
A_E = np.ones_like(f)*2.5
phi_E = np.ones_like(f)*3*np.pi/180

f_E2 = np.ones_like(f2)*0.01
A_E2 = np.ones_like(f2)*2.5
phi_E2 = np.ones_like(f2)*3*np.pi/180


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
        PLOT=True, graf1_title='Fit en data amplitude', graf1_x_label='f [Hz]', graf1_y_label='A [mm]'
        )
    
if False:
    param_names = ['w', 'm', 'n']
    initial_guess = [1.69, 0.07, 0.006]

    def model(params, x):
        w, m, n = params
        return (w**2-x**2)/(x*(n/m))
    
    data = ((f, f_E), (1/np.tan(phi), 1/np.tan(phi_E)))

    X_sq(data, param_names, initial_guess, model,
        root_attempts=None, datafile=None,
        VERBOSE=False, LaTeX=True,
        PLOT=True, graf1_title='', graf1_x_label='', graf1_y_label=''
        )
    
if False:
    param_names = ['w', 'm', 'n']
    initial_guess = [1.69, 0.07, 0.006]

    def model(params, x):
        a, b, c = params
        return np.arctan(a*x+b)+c
    
    data = ((f, f_E), (phi, phi_E))

    X_sq(data, param_names, initial_guess, model,
        root_attempts=None, datafile=None,
        VERBOSE=False, LaTeX=True,
        PLOT=True, graf1_title='', graf1_x_label='', graf1_y_label=''
        )
    
    
if False:
    x, x_E2, y, y_E2 = f2, f_E2, A2, A_E2
    plt.errorbar(x, y, xerr=x_E2, yerr=y_E2, fmt='o', color='black', label='Datapunten', capsize=4)

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
     
     data = ((f2, f_E2), (A2, A_E2))

     X_sq(data, param_names, initial_guess, model,
         root_attempts=None, datafile=None,
         VERBOSE=False, LaTeX=True,
         PLOT=True, graf1_title='Fit en data amplitude', graf1_x_label='f [Hz]', graf1_y_label='A [mm]'
        )
if True:
    param_names = ['w', 'm', 'n']
    initial_guess = [1.69, 0.07, 0.006]

    def model(params, x):
        w, m, n = params
        return (w**2-x**2)/(x*(n/m))
    
    data = ((f2, f_E2), (1/np.tan(phi2), phi_E2/np.sin(phi2)**2))

    X_sq(data, param_names, initial_guess, model,
        root_attempts=None, datafile=None,
        VERBOSE=False, LaTeX=True,
        PLOT=True, graf1_title=r'Fit voor $\phi$(f)', graf1_x_label='f [Hz]', graf1_y_label=r'$1/tan(\phi)$ [/]'
        )
if False:
    param_names = ['w', 'm', 'n']
    initial_guess = [1.69, 0.07, 0.006]

    def model(params, x):
        w, m, n = params
        return (w**2-x**2)/(x*(n/m))
    
    data = ((f, f_E), (1/np.tan(phi), phi_E/np.sin(phi)**2))

    X_sq(data, param_names, initial_guess, model,
        root_attempts=None, datafile=None,
        VERBOSE=False, LaTeX=True,
        PLOT=True, graf1_title='', graf1_x_label='', graf1_y_label=''
        )
if False:
    x, x_E, y, y_E = f, f_E, phi, phi_E
    plt.errorbar(x, y, xerr=x_E, yerr=y_E, fmt='o', color='black', label='Datapunten', capsize=4)

    # Add labels, title, and legend
    plt.xlabel('x-label')
    plt.ylabel('y-label')
    plt.title('Titel')
    plt.legend()
    plt.grid(True)

    plt.show()

if False:
    x, x_E, y, y_E = f2, f_E2, phi2, phi_E2
    plt.errorbar(x, y, xerr=x_E, yerr=y_E, fmt='o', color='black', label='Datapunten', capsize=4)

    # Add labels, title, and legend
    plt.xlabel('x-label')
    plt.ylabel('y-label')
    plt.title('Titel')
    plt.legend()
    plt.grid(True)

    plt.show()
