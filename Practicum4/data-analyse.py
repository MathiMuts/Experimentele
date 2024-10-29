from fit_file import X_sq
import numpy as np

param_names = ['B', 'C']
initial_guess = [1, 1]

def model(params, x):
    B, C = params
    return C + (B)*(x) #NOTE: waarom is da lineair? Kijk in uitleg


# NOTE: data load and call fit-function
file = "data.txt"
data = np.loadtxt(file).T
x = data[0]
dx = data[1]
y = data[2]
dy = data[3]

#NOTE: WTF doen we hier, zie uitlegblad
theta0 = 125.55
n = np.sin(((y-theta0)+60)*np.pi/360) / np.sin(np.pi/3)
dn = dy*(2/np.sqrt(3)) * np.abs(np.cos((y-theta0+60)*np.pi/360)*np.pi/360)

data = (x), (n ,dn)

X_sq(data, param_names, initial_guess, model,
        root_attempts=None, datafile=file,
        VERBOSE=False, LaTeX=False,
        PLOT=True, graf1_title='Fit and datapoints', graf1_y_label=r'$I$ [arb. eenh.]', graf1_x_label=r'$x$ [mm]'
        )