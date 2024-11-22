from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
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
if False:
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
""" NOTE: mooie grafiek"""
if True:
    A = 1.358
    B = -0.09

    C = np.log(np.exp(1.40) + intensity[0] - np.exp((A + B*thicknesses[0])))
    D = -1.97

    x, x_E, y, y_E = thicknesses, thicknesses_E, np.log(intensity), intensity_E/intensity 
    linsp_x = np.linspace(x[0]-0.5, x[-1]+0.5, 200)

    line2 = B * linsp_x + A 
    line1 = D * linsp_x + C

    plt.errorbar(x, y, yerr=y_E, fmt='o', color='black', label='Datapunten', capsize=4)

    plt.plot(linsp_x, line1, '-', label=r'Lineaire fit op laag-energetische $\gamma$-straling')
    plt.plot(linsp_x, line2, '--', label=r'Lineaire fit op hoog-energetische $\gamma$-straling')

# Add labels, title, and legend
    plt.xlabel('dikte Al [mm]')
    plt.ylabel('$ln(I)$ $[arb. eenh.]$')
    plt.title(r'Lineaire fits op beide $\gamma$-straling energieën')
    plt.legend()
    plt.grid(True)
    plt.xlim(x[0]-0.5, x[-1]+0.5)
    plt.ylim(0, y[0]*1.1)


# Show the plot
    plt.show()
