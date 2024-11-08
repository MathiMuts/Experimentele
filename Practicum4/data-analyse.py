from fit_file import X_sq
import numpy as np
from scipy.stats import sem

param_names = ['B', 'C']
initial_guess = [1]

def model(params, x):
    B, C = params
    return C + (B)*(x)


# NOTE: data load and call fit-function
file = "data.txt"
file2="mystery_element.txt"
#data = np.loadtxt(file).T
#mystery_data=np.loadtxt(file2).T
#x = data[0]
#y = data[1]

theta0 = 125.55 * np.pi/180
#y = y * np.pi/180
delta_sys = 5/60 * np.pi/180

#golflengtes = np.unique(x)

#resultaten = []
#for lambda_waarde in golflengtes:
 #   mask = x == lambda_waarde
  #  hoeken = y[mask]
    
   # theta_gem = np.mean(hoeken)
    #sigma_s = sem(hoeken)  # standaardfout (op basis van de vier metingen)
    #delta_m = theta_gem - theta0
    #sigma_delta_m = np.sqrt(sigma_s**2 + (delta_sys**2)/6)
    #resultaten.append((lambda_waarde, delta_m, sigma_delta_m))

#resultaten = np.array(resultaten)
#_lambda = resultaten[:, 0]
#d_lambda = np.zeros_like(_lambda)
#z = resultaten[:, 1]
#dz = resultaten[:, 2]
#a = np.pi/3

#n = np.sin((z+a)/2) / np.sin(a/2)
#dn = dz * np.abs( np.cos((z+a)/2)/(2*np.sin(a/2)) )
#data = (1/(_lambda**2), d_lambda), (n, dn)

#X_sq(data, param_names, initial_guess, model,
#        root_attempts=None, datafile=file,
 #       VERBOSE=False, LaTeX=False,
  #      PLOT=True, graf1_title='Fit and datapoints', graf1_y_label=r'$n$ [geen eenh.]', graf1_x_label=r'$1/\lambda^2$ [$nm^{-2}$]'
   #     )



param_names = ['B']
initial_guess = [1]

def model2(params, x):
    B = params
    return (B)*(x)

rood_absorptie=np.array([0.08,0.16,0.25,0.35,0.46])
rood_concentratie=np.array([2.75e-6,5.50e-6,8.26e-6,1.1e-5,1.38e-5])
rood_error=(0.04/np.sqrt(12))*np.ones(5)
concentratie_error=np.zeros(5)
rood_data=((rood_concentratie,concentratie_error),(rood_absorptie,rood_error))
X_sq(rood_data, param_names, initial_guess, model2,
        root_attempts=None, datafile=None,
        VERBOSE=False, LaTeX=False,
        PLOT=True, graf1_title='Absorbtie per concentratie van rode oplossing', graf1_y_label=r'$A$ [geen eenh.]', graf1_x_label=r'Concentratie [$mol/l$]'
        )

geel_absorptie=np.array([0.07,0.12,0.18,0.25,0.33])
geel_concentratie=np.array([2.26e-6,4.52e-6,6.78e-6,9.04e-6,1.13e-5])
geel_error=(0.04/np.sqrt(12))*np.ones(5)
concentratie_error=np.zeros(5)
geel_data=((geel_concentratie,concentratie_error),(geel_absorptie,geel_error))
X_sq(geel_data, param_names, initial_guess, model2,
        root_attempts=None, datafile=None,
         VERBOSE=False, LaTeX=False,
          PLOT=True, graf1_title='Absorbtie per concentratie van gele oplossing', graf1_y_label=r'$A$ [geen eenh.]', graf1_x_label=r'Concentratie [$mol/l$]'
        )

blauw_absorptie=np.array([0.22, 0.43, 0.67, 0.89, 1.1])
blauw_concentratie=np.array([1.49e-6, 2.98e-6, 4.46e-6, 5.95e-6, 7.44e-6])
blauw_error=(0.04/np.sqrt(12))*np.ones(5)
concentratie_error=np.zeros(5)
blauw_data=((blauw_concentratie,concentratie_error),(blauw_absorptie,blauw_error))
X_sq(blauw_data, param_names, initial_guess, model2,
        root_attempts=None, datafile=None,
         VERBOSE=False, LaTeX=False,
          PLOT=True, graf1_title='Absorbtie per concentratie van blauwe oplossing', graf1_y_label=r'$A$ [geen eenh.]', graf1_x_label=r'Concentratie [$mol/l$]'
        )