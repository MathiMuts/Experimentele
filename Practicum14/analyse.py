import fit_classes as fp
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize
import matplotlib as plt

metingen1=[17,17,15.5,16]
metingen2=[11.5,13,12]
metingen3=[11,12,11.5]
avg1=(17+17+15.5+16)/4
avg2=(11.5+13+12)/3
avg3=(21+23+22.5)/3
Lambda=2/5*avg1*10**(-6)
err=0.5
print(Lambda)
N_1=avg2/10*2*10**(-5)
err_N1=0.5/2/10*2*10**(-5)
p_0=10**5*1.013
T=294.15
T_0=273.15
L=3.82*10**(-2)
n_O=N_1*Lambda*T*p_0/(2*L*T_0)
print(n_O)
print(err_N1/N_1)
N_2=avg3/10*2*10**(-5)
n_CO=N_2*Lambda*T*p_0/(2*L*T_0)
print(n_CO)
