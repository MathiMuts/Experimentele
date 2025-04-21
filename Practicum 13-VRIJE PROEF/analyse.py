import fit_classes as fp
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import os

#polarisator moet op 33 deg voor loodrecht
data = np.loadtxt(r"C:\Users\micha\OneDrive\Documents\Desktop\Experimentele\Practicum 13-VRIJE PROEF\paas_vrije_proef_2.csv", delimiter=",",skiprows=1)
# data  = np.loadtxt(r"/home/mathi/Experimentele/Practicum 13-VRIJE PROEF/Vrijdag_data_vrije3.csv", delimiter=",",skiprows=1)

# Extract each column into a separate array
theta_vals, i_P, i_O = data[:, 0], data[:, 1], data[:, 2]
print("Column 1:", theta_vals)
print("Column 2:", i_P)
print("Column 3:", i_O)

ERROR = 0
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
 return (1-1/2*(1-np.cos(phi))*np.sin(2*(x+delta))**2)*C

def modelO(params,x):
 phi,C,delta=params
 return (1/2*(1-np.cos(phi))*np.sin(2*(x+delta))**2)*C

P_data=fp.Data(theta_vals,I_P,I_P_err)
O_data=fp.Data(theta_vals,I_O,I_O_err)
P_data.show()
O_data.show()
print(P_data.fit(model=modelP,initial_guess=(1,0.02,0)))
print(O_data.fit(model=modelO),initial_guess=(1,0.02,0))
P_data.fit(model=modelP,initial_guess=(1,0.02,0)).show()
O_data.fit(model=modelO,initial_guess=(1,0.02,0)).show()
#safier-1
#lithium niobaat-2