from pathlib import Path
import numpy as np
from fit_file import X_sq

folder_path = Path("Practicum5/penetration/data/")

values = []
achtergrond = 3.1
for file_name in [file.name for file in folder_path.iterdir()]:
    file = f"Practicum5/penetration/data/{file_name}"
    thickness_value = float(file_name.split("-")[1].replace(".txt", "").replace(",", "."))

    data = (np.loadtxt(file).T-achtergrond)/10
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

""" NOTE: Hieronder alle data"""
# data = ((thicknesses, thicknesses_E), (np.log(intensity), intensity_E/intensity ))

# X_sq(data, param_names, initial_guess, model,
#         root_attempts=None, datafile=None,
#         VERBOSE=False, LaTeX=False,
#         PLOT=True, graf1_title='Titel', graf1_x_label='Label'
#         )

""" NOTE: Hieronder een fit op de laag energetische straling"""
# cutoff = 6
# data = ((thicknesses[:cutoff], thicknesses_E[:cutoff]), (np.log(intensity[:cutoff]), intensity_E[:cutoff]/intensity[:cutoff] ))

# X_sq(data, param_names, initial_guess, model,
#         root_attempts=None, datafile=None,
#         VERBOSE=False, LaTeX=True,
#         PLOT=False, graf1_title='Titel', graf1_x_label='Label'
#         )

""" NOTE: Hieronder een fit op de hoog energetische straling"""
# start = 9
# data = ((thicknesses[start:], thicknesses_E[start:]), (np.log(intensity[start:]), intensity_E[start:]/intensity[start:] ))

# X_sq(data, param_names, initial_guess, model,
#         root_attempts=None, datafile=None,
#         VERBOSE=False, LaTeX=True,
#         PLOT=True, graf1_title='Fit voor hoog energetische straling', graf1_x_label='dikte Al [mm]', graf1_y_label='$ln(I) [arb. eenh.]$'
#         )

# """ NOTE: Hieronder eerste deel min hoog energetische straling volgens model"""
A = 1.358
B = -0.09
A_e = 0.03
B_e = 0.006


intensity_corrected = []
for i in range(len(intensity)):
    intensity_corrected.append(intensity[i] - np.exp((A + B*thicknesses[i])))

intensity_corrected_E = []
for i in range(len(intensity_corrected)):
    intensity_corrected_E.append(np.sqrt(intensity_E[i]**2 + (np.exp((A + B*thicknesses[i])))**2 * A_e**2 + (thicknesses[i]* np.exp((A + B*thicknesses[i])))**2 * B_e**2))
intensity_corrected_E = np.array(intensity_corrected_E)

data = ((thicknesses[:9], thicknesses_E[:9]), (np.log(intensity_corrected[:9]), intensity_corrected_E[:9]/intensity_corrected[:9] ))
# data = ((thicknesses[:9], thicknesses_E[:9]), (np.log(intensity_corrected[:9]), intensity_E[:9]/intensity_corrected[:9] ))

X_sq(data, param_names, initial_guess, model,
        root_attempts=None, datafile=None,
        VERBOSE=False, LaTeX=True,
        PLOT=True, graf1_title='Fit op laag energetische straling', graf1_x_label='dikte Al [mm]', graf1_y_label='$ln(I) [arb. eenh.]$'
        )

""" WARNING: geen correcte constanten en fout 
NOTE: Hieronder tweede deel min laag energetische straling volgens model"""
# A = 3.71603917
# B = -1.96933049

# intensity_corrected = []
# for i in range(len(intensity)):
#     intensity_corrected.append(intensity[i] - np.exp((A + B*thicknesses[i])))

# data = ((thicknesses[6:], thicknesses_E[6:]), (np.log(intensity_corrected[6:]), intensity_E[6:]/intensity_corrected[6:] ))

# X_sq(data, param_names, initial_guess, model,
#         root_attempts=None, datafile=None,
#         VERBOSE=False, LaTeX=False,
#         PLOT=True, graf1_title='Titel', graf1_x_label='thickness (mm)', graf1_y_label='ln(I)'
#         )
