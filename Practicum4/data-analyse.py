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
dx = data[1]
y = data[2]
dy = data[3]

theta0 = 125.55
delta_sys = 0.0006

golflengtes = np.unique(x)

resultaten = []
for lambda_waarde in golflengtes:
    mask = x == lambda_waarde
    hoeken = y[mask]
    
    theta_gem = np.mean(hoeken)
    sigma_s = sem(hoeken)  # standaardfout (op basis van de vier metingen)
    delta_m = theta_gem - theta0
    sigma_delta_m = np.sqrt(sigma_s**2 + (delta_sys**2) / 12)
    resultaten.append((lambda_waarde, delta_m, sigma_delta_m))

resultaten = np.array(resultaten)
_lambda = resultaten[:, 0]
d_lambda = np.zeros_like(_lambda)
z = resultaten[:, 1]
dz = resultaten[:, 2]

n = np.sin((z+60)*np.pi/360) / np.sin(np.pi/3)
dn = dz*(2/np.sqrt(3)) * np.abs(np.cos((z+60)*np.pi/360)*np.pi/360)

data = (1/(_lambda**2), d_lambda), (n, dn)
X_sq(data, param_names, initial_guess, model,
        root_attempts=None, datafile=file,
        VERBOSE=False, LaTeX=True,
        PLOT=True, graf1_title='Fit and datapoints', graf1_y_label=r'$n$ [geen eenh.]', graf1_x_label=r'$1/\lambda^2$ [$nm^{-2}$]'
        )