from fit_file import X_sq
import numpy as np
from scipy.stats import sem

param_names = ['B', 'C']
initial_guess = [1, 1]

def model(params, x):
    B, C = params
    return C + (B)*(x)


# NOTE: data load and call fit-function
file = "data.txt"
data = np.loadtxt(file).T
x = data[0]
y = data[1]

theta0 = 125.55 * np.pi/180
y = y * np.pi/180
delta_sys = 2/60 * np.pi/180

golflengtes = np.unique(x)

resultaten = []
for lambda_waarde in golflengtes:
    mask = x == lambda_waarde
    hoeken = y[mask]
    
    theta_gem = np.mean(hoeken)
    sigma_s = sem(hoeken)  # standaardfout (op basis van de vier metingen)
    delta_m = theta_gem - theta0
    sigma_delta_m = np.sqrt(sigma_s**2 + (delta_sys**2))
    resultaten.append((lambda_waarde, delta_m, sigma_delta_m))

resultaten = np.array(resultaten)
_lambda = resultaten[:, 0]
d_lambda = np.zeros_like(_lambda)
z = resultaten[:, 1]
dz = resultaten[:, 2]

a = np.pi/3

n = np.sin((z+a)/2) / np.sin(a/2)
dn = dz * np.abs( np.cos((z+a)/2)/(2*np.sin(a/2)) )

data = (1/(_lambda**2), d_lambda), (n, dn)

X_sq(data, param_names, initial_guess, model,
        root_attempts=None, datafile=file,
        VERBOSE=True, LaTeX=True,
        PLOT=True, graf1_title='Fit and datapoints', graf1_y_label=r'$n$ [geen eenh.]', graf1_x_label=r'$1/\lambda^2$ [$nm^{-2}$]'
        )