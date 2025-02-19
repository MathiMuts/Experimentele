import fit_classes as fp
import numpy as np
import os, time

errors = []
ERROR = 1.85 # Error in mV

class DataPlus(fp.Data):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def sinus_model(params, x):
            A,w,phi,c = params
            return A*np.sin(w*x + phi) + c
        try:
            self.fit = self.fit(sinus_model, initial_guess=(200, 0.006, -10, 25))
        except ValueError as e:
            errors.append(self.name)

        self.A, self.w, self.phi, self.c = self.fit.minima

def data_from_file(file):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    data = np.genfromtxt(file_path, delimiter=",", skip_header=9)
    x = data[:, 0].astype(int)
    y = data[:, 1]
    mask = np.concatenate(([True], y[1:] != y[:-1]))
    x = x[mask]
    y = y[mask]

    dy = ERROR*np.ones_like(y)
    return DataPlus(x, y, dy, name=file_path)
        
def get_lowest_folders(root):
    lowest_folders = []
    for dirpath, dirnames, filenames in os.walk(root):
        if not dirnames:
            lowest_folders.append(dirpath)
    return lowest_folders

def load_data_by_folder(root):
    print(f"----------------------------------------------------------------------------------------------------------------")
    start_time = time.time()
    folder_data = {}
    total_files = 0
    for folder in get_lowest_folders(root):
        total_files += len([f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))])

    current_file = 0
    for folder in get_lowest_folders(root):
        folder_name = os.path.basename(folder)
        data_list = []
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            if os.path.isfile(file_path):
                current_file += 1
                print(f"File: {current_file:>3}/{total_files}")
                data_list.append(data_from_file(file_path))
        
        if data_list:
            folder_data[folder_name] = np.array(data_list)

    elapsed_time = time.time() - start_time
    print(f"----------------------------------------------------------------------------------------------------------------")
    print(f"Data loaded in {elapsed_time:.6f} seconds")
    print(f"----------------------------------------------------------------------------------------------------------------")
    return folder_data

data_arrays = load_data_by_folder(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))

for error in errors:
    print(error)
# print(data_arrays['opgave1'][0].show())
print(data_arrays['opgave1'][0].fit)
print(data_arrays['opgave1'][0].A) # amplitude
print(data_arrays['opgave1'][0].w) # hoekfreq
data_arrays['opgave1'][0].fit.show(size=2)
