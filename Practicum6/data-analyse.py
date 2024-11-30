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
phi_E = np.ones_like(f)*10*np.pi/180
f_E2 = np.ones_like(f2)*0.01*(2*np.pi)
A_E2 = np.ones_like(f2)*1
phi_E2 = np.ones_like(f2)*2*np.pi/180

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

# data 2 amplitude fit
if False:
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
#data1 fitten frequentie    
if True:
     print(len(phi))
     phi=np.delete(phi,25)
     phi_E=np.delete(phi_E,25)
     f=np.delete(f,25)
     f_E=np.delete(f_E,25)

     param_names = ['w', 'C','S']
     initial_guess = [0.26, -0.07, 1]

     def model(params, x):
        w, C, S= params
        return S-np.arctan2((x*C),(w**2-x**2))
    
     data = ((f, f_E), ((phi), phi_E))


     X_sq(data, param_names, initial_guess, model,
        root_attempts=None, datafile=None,
        VERBOSE=False, LaTeX=True,
        PLOT=True, graf1_title=r'Fit voor $\phi(\omega)$ 1', graf1_x_label='$\omega$ [Hz]', graf1_y_label=r'$(\phi)$ [/]'
        )
#data 2 fitten frequentie
if True:
    param_names = ['w', 'C','S']
    initial_guess = [0.26, -0.07, 1]

    def model(params, x):
        w, C, S= params
        return S-np.arctan2((x*C),(w**2-x**2))
    
    data = ((f2, f_E2), ((phi2), phi_E2))


    X_sq(data, param_names, initial_guess, model,
        root_attempts=None, datafile=None,
        VERBOSE=False, LaTeX=True,
        PLOT=True, graf1_title=r'Fit voor $\phi(\omega)$ 2', graf1_x_label='$\omega$ [Hz]', graf1_y_label=r'$(\phi)$ [/]'
        )
