import numpy as np

# Constants
DELTA_N = -0.085
THICKNESS = 0.5 * 1e-3  # in meters
LAMBDA = 670 * 1e-9  # in meters
ERROR = 0.015  # Error for intensity

# Generate theta values (angles in degrees from 0 to 360 in steps of 10)
theta_vals_deg = np.arange(0, 361, 10)  # Degrees
theta_vals_rad = np.deg2rad(theta_vals_deg)  # Convert to radians

# Calculate delta_phi
delta_phi = 2 * np.pi * DELTA_N * THICKNESS / LAMBDA
delta_phi_normalised = np.mod(delta_phi, 2 * np.pi)
print("amount of 2pi's", (delta_phi - delta_phi_normalised) / (2 * np.pi))
print(delta_phi_normalised)

# Calculate theoretical intensities
I_P = 1 - 0.5 * (1 - np.cos(delta_phi_normalised)) * np.sin(2*theta_vals_rad)**2
I_O = 0.5 * (1 - np.cos(delta_phi_normalised)) * np.sin(2*theta_vals_rad)**2

# Add noise to the intensities
I_P_noisy = I_P + np.random.normal(0, ERROR, size=I_P.shape)
I_O_noisy = I_O + np.random.normal(0, ERROR, size=I_O.shape)

# Save the dataset to a CSV file
output_file = r"C:\Users\Mathi\Documents\3) - Study\3) - Uni\2) - Ba2\Experimentele\Practicum 13-VRIJE PROEF\synthetic_dataset.csv"
data = np.column_stack((theta_vals_deg, I_P_noisy, I_O_noisy))  # Use degrees for theta
np.savetxt(output_file, data, delimiter=",", header="theta_deg,I_P,I_O", comments="")

print(f"Synthetic dataset saved to {output_file}")


# FOR SYNTHETIC DATASET:
DELTA_N = -0.085
THICKNESS = 1 * 1e-3
LAMBDA = 660 * 1e-9

initial_guess=(1.33, 1, 0)
phi = 1.33646
E_phi = 0.03153

print("phi", phi)
k = 129.0
phi = -phi + k*2*np.pi
print("phi + k*2*pi", phi)


dikte = (LAMBDA * -phi) / (2 * np.pi * DELTA_N)

print(dikte *1e3, "mm")
# INFO: phi = 2pi L N / lambda