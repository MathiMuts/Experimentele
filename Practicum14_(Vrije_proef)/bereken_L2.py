import numpy as np
import matplotlib.pyplot as plt

# Constants
DELTA_N = -0.085
THICKNESS = 0.5 * 1e-3  # in meters
LAMBDA1 = 670 * 1e-9  # in meters
LAMBDA2 = 635 * 1e-9  # in meters
PHI1 = 0.02898
PHI2 = 0

def k2(k1):
    return ( (LAMBDA1/LAMBDA2) * (-PHI1 + k1*2*np.pi) - PHI2) / (2*np.pi)

def plot(x, y):
    plt.scatter(x, y)
    plt.xlabel('k1')
    plt.ylabel('k2 - floor(k2)')
    plt.title('k2-kommagedeelte vs k1')
    plt.grid(True)
    plt.show()


k1_values = np.arange(0, 101)
k2_values = np.abs(k2(k1_values) - np.floor(k2(k1_values)))

plot(k1_values, k2_values)