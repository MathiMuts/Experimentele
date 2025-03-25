import fit_classes as fp
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize
import matplotlib.pyplot as plt


I=[1,1.1,1.2,1.3,1.4,1.5,2]
h_1=np.array([12.95,13.5,14.05,14.55,14.75,14.5,16.3])
h_2=np.array([25.45,25.55,25.3,24.3,23.8,23.55,22.2])
R=(h_2-h_1)/2*0.01
print(R)
R_err=np.ones_like(R)*0.0025
print(R)
def model1(params, x):
    A = params
    return A/x
data=fp.Data(I,R,R_err)
print(data.fit(model=model1))
data.fit(model=model1).show()
N=130
r=0.15
mu=2*np.pi*10**(-7)
a=mu*(4/5)**(3/2)*N/r
A=0.06460
V_a=223.5
eta=2*V_a/(A**2*a**2)
print(a)
print(eta)
