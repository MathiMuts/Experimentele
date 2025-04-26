import fit_classes as fp
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import os

#polarisator moet op 33 deg voor loodrecht
# data = np.loadtxt(r"C:\Users\micha\OneDrive\Documents\Desktop\Experimentele\Practicum 13-VRIJE PROEF\paas_vrije_proef_2.csv", delimiter=",",skiprows=1)
# data  = np.loadtxt(r"/home/mathi/Experimentele/Practicum 13-VRIJE PROEF/paas_vrije_proef_2.csv", delimiter=",",skiprows=1)
# data  = np.loadtxt(r"C:\Users\Mathi\Documents\3) - Study\3) - Uni\2) - Ba2\Experimentele\Practicum 13-VRIJE PROEF\synthetic_dataset.csv", delimiter=",",skiprows=1)
data  = np.loadtxt(r"C:\Users\Mathi\Documents\3) - Study\3) - Uni\2) - Ba2\Experimentele\Practicum 13-VRIJE PROEF\paas_vrije_proef_2.csv", delimiter=",",skiprows=1)

# Extract each column into a separate array
theta_vals, i_P, i_O = data[:, 0], data[:, 1], data[:, 2]
# print("Column 1:", theta_vals)
# print("Column 2:", i_P)
# print("Column 3:", i_O)

ERROR = 0.03
theta_vals=np.array(theta_vals)*np.pi/180
i_P=np.array(i_P)
I_P_err=np.ones_like(i_P)*ERROR
i_O=np.array(i_O)
I_O_err=np.ones_like(i_O)*ERROR
I_P=(i_P/(i_P+i_O))
I_O=(i_O/(i_P+i_O))
L=1
lamda=1
def modelP(params,x):
 phi,C,delta=params
 return (1 - 1/2*(1-np.cos(phi)) * np.sin(2*(x+delta))**2)*C

def modelP_simple(params,x):
 A, w, delta, c =params
 return A* np.sin(2*(w*x+delta))**2 + c

def modelO(params,x):
 phi,C,delta, d=params
 return (1/2*(1-np.cos(phi))*np.sin(2*(x+delta))**2)*C + d

def sin(params,x):
 A, w, phi, c =params
 return A* np.sin(w*x+phi)+c

P_data=fp.Data(theta_vals,I_P,I_P_err)
O_data=fp.Data(theta_vals,I_O,I_O_err)
# P_data.show()
# # O_data.show()
# initial_guess=(0.0002, 1, 0, 0.9993)
# print(P_data.fit(model=sin, initial_guess=initial_guess)) # WERKT!
# P_data.fit(model=sin, initial_guess=initial_guess).show()

EXP_AMPLITUDE = 0.00021 # uit fit hierboven

DELTA_N = -0.085
THICKNESS = 0.5 * 1e-3
LAMBDA = 670 * 1e-9

# # INFO: wat we zouden moeten uitkomen
# delta_phi = 2 * np.pi * DELTA_N * THICKNESS / LAMBDA
# delta_phi_normalised = np.mod(delta_phi, 2 * np.pi)
# amplitude = 1/2 * (1 - np.cos(delta_phi_normalised))
# print("phi:", delta_phi_normalised / np.pi, "pi")
# print("amplitude:", amplitude)

# print("-----------------------")

# INFO: Wat we uikomen
exp_delta_phi = np.arccos(1 - 2*EXP_AMPLITUDE)
print("phi:", exp_delta_phi)
k= 63
phi = -exp_delta_phi + 2 * np.pi * k
exp_dikte = (LAMBDA * phi) / (2 * np.pi * -DELTA_N)

print(f"phi + k ({k}) * 2pi:", phi)
print("dikte:", exp_dikte * 1e3, "mm")

# print("-----------------------")

# # INFO: Wat we uikomen
# exp_delta_phi = np.arccos(1 - 2*EXP_AMPLITUDE)
# exp_delta_N = (exp_delta_phi * LAMBDA) / (2 * np.pi * THICKNESS)
# print("phi:", exp_delta_phi / np.pi, "pi")
# print("delta N:", exp_delta_N)
