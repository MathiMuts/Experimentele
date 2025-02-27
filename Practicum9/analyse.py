import fit_classes as fp
import numpy as np
import os

import pandas as pd
import glob

# Get the absolute path to the "data" folder
script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
data_folder = os.path.join(script_dir, "data")  # Construct the path to "data"

# Get all CSV files in the "data" folder
csv_files = glob.glob(os.path.join(data_folder, "*.csv"))

# Debug: Check if files are found
if not csv_files:
    print(f"No CSV files found in '{data_folder}'. Check the path and file extensions.")
    exit()

# Dictionaries to store separate arrays for each file
potential_1_dict = {}
potential_2_dict = {}
time_dict={}
# Read each CSV file
for file in csv_files:
    filename = os.path.basename(file)  # Get the filename without path

    # Read CSV
    df = pd.read_csv(file, delimiter=';', decimal=',')

    # Strip spaces from column names (just in case)
    df.columns = df.columns.str.strip()

    # Extract data if columns exist
    if "Latest: Time (s)" in df.columns and "Latest: Potential 1 (V)" in df.columns and "Latest: Potential 2 (V)" in df.columns:
        time_dict[filename]=df["Latest: Time (s)"].values
        potential_1_dict[filename] = df["Latest: Potential 1 (V)"].values
        potential_2_dict[filename] = df["Latest: Potential 2 (V)"].values
    else:
        print(f"Warning: Required columns not found in {filename}")

def model1(params, x):
    tau,a = params
    return (1-np.exp(-(x-0.160)/tau))*a

errors=0.01*np.ones_like(potential_1_dict['2-1.csv'])
test=fp.Data(time_dict['2-1.csv'][:500], potential_1_dict['2-1.csv'][:500],errors[:500])
test1=fp.Data(time_dict['2-1.csv'][25:145], potential_2_dict['2-1.csv'][25:145],errors[25:145])
#test1.fit(model=model1).show()
print(test1.fit(model=model1))
errors=0.1*np.ones_like(potential_2_dict['2-2_1.5Hz.csv'])

def sin_model(params,x):
    phi,A,f,c= params
    return(c+A*np.sin(2*np.pi*f*x+phi))
test2=fp.Data(time_dict['2-2_1.5Hz.csv'], potential_2_dict['2-2_1.5Hz.csv'],errors)
print(test2.fit(sin_model))
#test2.fit(sin_model, initial_guess=(1,0.9,1.5,0)).show()
test2.fit(sin_model, initial_guess=(1,0.9,1.5,0)).show_chi2()

