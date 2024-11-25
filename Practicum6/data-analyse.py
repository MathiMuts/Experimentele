from fit_file import X_sq
import numpy as np
import matplotlib.pyplot as plt

# X_sq(data, param_names, initial_guess, model,
#         root_attempts=None, datafile=None,
#         VERBOSE=False, LaTeX=True,
#         PLOT=True, graf1_title='Fit voor hoog energetische straling', graf1_x_label='dikte Al [mm]', graf1_y_label='$ln(I) [arb. eenh.]$'
#         )

file=np.loadtxt("Practicum6/data.txt", delimiter=' ').T
f=file[0]
A=file[1]
phi=file[2]
print(f)
print(A)
print(phi)