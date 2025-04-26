import fit_classes as fp
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import os

#polarisator moet op 33 deg voor loodrecht
# data = np.loadtxt(r"C:\Users\micha\OneDrive\Documents\Desktop\Experimentele\Practicum 13-VRIJE PROEF\paas_vrije_proef_2.csv", delimiter=",",skiprows=1)
data  = np.loadtxt(r"/home/mathi/Experimentele/Practicum 13-VRIJE PROEF/paas_vrije_proef_2.csv", delimiter=",",skiprows=1)

# Extract each column into a separate array
theta_vals, i_P, i_O = data[:, 0], data[:, 1], data[:, 2]
# print("Column 1:", theta_vals)
# print("Column 2:", i_P)
# print("Column 3:", i_O)

ERROR = 0.0001
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
 phi,C,delta, d=params
 return (1 - 1/2*(1-np.cos(phi)) * np.sin(2*(x+delta))**2)*C + d

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
# O_data.show()
initial_guess=(0.0002, 1, 0, 0.9993)
print(P_data.fit(model=sin, initial_guess=initial_guess)) # WERKT!
P_data.fit(model=sin, initial_guess=initial_guess).show()

initial_guess=(0.0002, 1, 0, 0.9993)
# print(P_data.fit(model=modelP_simple, initial_guess=initial_guess).show())

# print(O_data.fit(model=modelO, initial_guess=(1,0.02,0, 1)).show())
# P_data.fit(model=modelP,initial_guess=(0,0.02,0)).show()
# O_data.fit(model=modelO,initial_guess=(0,0.02,0)).show()
#safier-1
#lithium niobaat-2



# INFO: Guess for fit
model = modelP_simple
model_x = np.linspace(0.9*np.min(P_data.x), 1.1*np.max(P_data.x), 120)
# model_y = P_data.model(P_data.minima, model_x)
guess_y = model(initial_guess, model_x)

fig, ax = plt.subplots(nrows=1, ncols=1, dpi=120, figsize=(5, 3))
ax.errorbar(P_data.x, P_data.y, xerr=P_data.dx, yerr=P_data.dy,
        marker="o", markersize=1, fmt=" ", color="b", ecolor="black", capsize=2, capthick=0.6, linewidth=0.6)
plt.plot(model_x, guess_y, color="r", label="guess")
ax.legend()
plt.tight_layout()
plt.show()