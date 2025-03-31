import fit_classes as fp
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import os
data = np.loadtxt(r"C:\Users\micha\OneDrive\Documents\Desktop\Experimentele\Practicum 13-VRIJE PROEF\test_data_vrijeproef.csv.txt", delimiter=",",skiprows=1)

# Extract each column into a separate array
theta_vals, i_P, i_O = data[:, 0], data[:, 1], data[:, 2]

print("Column 1:", theta_vals)
print("Column 2:", i_P)
print("Column 3:", i_O)


theta_vals=np.array(theta_vals)
i_P=np.array(i_P)
I_P_err=np.ones_like(i_P)
i_O=np.array(i_O)
I_O_err=np.ones_like(i_O)
I_P=(i_P/(i_P+i_O))
I_O=(i_O/(i_P+i_O))
L=1
lamda=1
def modelP(params,x):
 phi=params
 return 1-1/2*(1-np.cos(phi))*np.sin(2*x)**2

def modelO(params,x):
 phi=params
 return 1/2*(1-np.cos(phi))*np.sin(2*x)**2

P_data=fp.Data(theta_vals,I_P,I_P_err)
O_data=fp.Data(theta_vals,I_O,I_O_err)
print(P_data.fit(model=modelP))
print(O_data.fit(model=modelO))


