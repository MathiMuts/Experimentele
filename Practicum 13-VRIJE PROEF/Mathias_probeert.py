import fit_classes as fp
import numpy as np
import matplotlib.pyplot as plt
data  = np.loadtxt(r"/home/mathi/Experimentele/Practicum 13-VRIJE PROEF/paas_vrije_proef_2.csv", delimiter=",",skiprows=1)


ERROR = 0.0001
DELTA_N = -0.085
THICKNESS = 1 * 1e-3
LAMBDA = 590 * 1e-9

delta_phi = 2 * np.pi * DELTA_N * THICKNESS / LAMBDA
amplitude = 1/2 * (1 - np.cos(delta_phi))
def intensity(x):
    return amplitude * np.sin(2*x)**2

print(amplitude)


# theta_vals, i_P, i_O = data[:, 0], data[:, 1], data[:, 2]
# theta_vals=np.array(theta_vals)*np.pi/180
# i_P=np.array(i_P)
# I_P_err=np.ones_like(i_P)*ERROR
# i_O=np.array(i_O)
# I_O_err=np.ones_like(i_O)*ERROR
# I_P=(i_P/(i_P+i_O))
# I_O=(i_O/(i_P+i_O))