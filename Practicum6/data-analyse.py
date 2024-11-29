from fit_file import X_sq
import numpy as np
import matplotlib.pyplot as plt

file=np.loadtxt("Practicum6/data.txt", delimiter=' ').T
file2=np.loadtxt("Practicum6/data2.txt", delimiter=' ').T

f=file[0]*(2*np.pi)
A=file[1]
phi=file[2]*np.pi/180

f2=file2[0]*(2*np.pi)
A2=file2[1]
phi2=file2[2]*np.pi/180


f_E = np.ones_like(f)*0.01*(2*np.pi)
A_E = np.ones_like(f)*2.5
phi_E = np.ones_like(f)*3*np.pi/180

f_E2 = np.ones_like(f2)*0.01*(2*np.pi)
A_E2 = np.ones_like(f2)*1
phi_E2 = np.ones_like(f2)*3*np.pi/180

#data 1 amplitude plotten
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

#data1 fitten amplitude    
if False:
    print(len(f_E))
    print(len(A_E))
    param_names = ['w','B','C']
    initial_guess = [2,0.1,0.01]

    def model(params, x):
        w,B,C = params
        return C/(np.sqrt((x**2-w**2)**2+(x*B)**2))
    data = ((f, f_E), (A, A_E))

    X_sq(data, param_names, initial_guess, model,
        root_attempts=None, datafile=None,
        VERBOSE=False, LaTeX=True,
        PLOT=True, graf1_title='Fit en data amplitude', graf1_x_label=r'$\omega$ [Hz]', graf1_y_label='A [mm]'
        )
#data1 fitten frequentie    
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
#data 2 amplitude plot
       
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
# data 2 amplitude fit
if True:
     param_names = ['w','B','C']
     initial_guess = [10,0.1,1]

     def model(params, x):
        w,B,C = params
        return C/(np.sqrt((x**2-w**2)**2+(x*B)**2))

     data = ((f2, f_E2), (A2, A_E2))

     X_sq(data, param_names, initial_guess, model,
         root_attempts=None, datafile=None,
         VERBOSE=False, LaTeX=True,
         PLOT=True, graf1_title='Fit en data amplitude', graf1_x_label=r'$\omega$ [Hz]', graf1_y_label='A [mm]'
        )
# frequentie fit2 semi lineair
if False:
    param_names = ['w', 'C']
    initial_guess = [1.69, 0.07, 0.006]

    def model(params, x):
        w, C = params
        return (w**2-x**2)/(x*C)
    
    data = ((f2, np.ones_like(f2)*0), (1/np.tan(phi2), phi_E2/np.sin(phi2)**2))

    X_sq(data, param_names, initial_guess, model,
        root_attempts=None, datafile=None,
        VERBOSE=False, LaTeX=True,
        PLOT=True, graf1_title=r'Fit voor $\phi$(f)', graf1_x_label='f [Hz]', graf1_y_label=r'$1/tan(\phi)$ [/]'
        )
#frequentie fit 2 niet lineair
if False:
    param_names = ['w', 'C','S']
    initial_guess = [0.26, -0.07, 1]

    def model(params, x):
        w, C, S= params
        return S-np.arctan2((x*C),(w**2-x**2))
    
    data = ((f, f_E), ((-phi), phi_E))

    X_sq(data, param_names, initial_guess, model,
        root_attempts=None, datafile=None,
        VERBOSE=False, LaTeX=True,
        PLOT=True, graf1_title=r'Fit voor $\phi$(f)', graf1_x_label='f [Hz]', graf1_y_label=r'$(\phi)$ [/]'
        )

 # frequentie fit1 semi-lineair DEZE IS ASS
if False:
    param_names = ['w', 'C']
    initial_guess = [1.69, 0.006]

    def model(params, x):
        w, C = params
        return (w**2-x**2)/(x*C)
    
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
