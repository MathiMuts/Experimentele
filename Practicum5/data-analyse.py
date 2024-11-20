from pathlib import Path
import numpy as np
from fit_file import X_sq

folder_path = Path("penetration/data/")

values = []
for file_name in [file.name for file in folder_path.iterdir()]:
    file = f"penetration/data/{file_name}"
    thickness_value = float(file_name.split("-")[1].replace(".txt", "").replace(",", "."))

    data = np.loadtxt(file).T
    N = len(data)

    gem = np.sum(data)/N
    s = np.sqrt(np.sum((data-gem)**2))/np.sqrt(N-1)
    error = s/np.sqrt(N)

    values.append(tuple([thickness_value, gem, error, error/gem]))

# -----------

param_names = ['A', 'B']
initial_guess = [1, 1]

def model(params, x):
    A, B = params
    return A + (B)*(x)

thicknesses = np.array([value[0] for value in values])
thicknesses_E = np.zeros(len(thicknesses))
intensity = np.array([value[1] for value in values])
intensity_E = np.array([value[2] for value in values])

sorted_indices = np.argsort(thicknesses)

thicknesses = thicknesses[sorted_indices]
thicknesses_E = thicknesses_E[sorted_indices]
intensity = intensity[sorted_indices]
intensity_E = intensity_E[sorted_indices]

cutoff = 6
data = ((thicknesses[:cutoff], thicknesses_E[:cutoff]), (np.log(intensity[:cutoff]), intensity_E[:cutoff]/intensity[:cutoff] ))

X_sq(data, param_names, initial_guess, model,
        root_attempts=None, datafile=None,
        VERBOSE=False, LaTeX=False,
        PLOT=True, graf1_title='Titel', graf1_x_label='Label'
        )

start = 9
data = ((thicknesses[start:], thicknesses_E[start:]), (np.log(intensity[start:]), intensity_E[start:]/intensity[start:] ))

X_sq(data, param_names, initial_guess, model,
        root_attempts=None, datafile=None,
        VERBOSE=False, LaTeX=False,
        PLOT=True, graf1_title='Titel', graf1_x_label='Label'
        )