import fit_classes as fp
import numpy as np
import os, time

class DataPlus(fp.Data):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def sinus_model(params, x):
            A,w,phi,c = params
            return A*np.sin(w*x + phi) + c
        
        self.fit = self.fit(sinus_model, initial_guess=(100, 0.006, 1, 25))
        self.A, self.w, self.phi, self.c = self.fit.minima

def data_from_file(file):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    data = np.genfromtxt(file_path, delimiter=",", skip_header=9)
    index = data[:, 0].astype(int)
    voltage = data[:, 1]
    """Quantization Error Calculation
        From the metadata:
        Voltage per ADC value: 0.122070 mV
        Since an ADC rounds the measured voltage to the nearest discrete step, the maximum possible error in a single measurement is half of this step size:
        Error=(Voltage per ADC value)/2 = 0.122070/2 mV = 0.061035 mV
    """
    E_voltage = 0.06*10**(-3)*np.ones_like(voltage)
    return DataPlus(index, voltage, E_voltage)
        
def get_lowest_folders(root):
    lowest_folders = []
    for dirpath, dirnames, filenames in os.walk(root):
        if not dirnames:
            lowest_folders.append(dirpath)
    return lowest_folders

def load_data_by_folder(root):
    start_time = time.time()
    folder_data = {}
    for folder in get_lowest_folders(root):
        folder_name = os.path.basename(folder)
        data_list = []
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            if os.path.isfile(file_path):
                data_list.append(data_from_file(file_path))
        
        if data_list:
            folder_data[folder_name] = np.array(data_list)

    elapsed_time = time.time() - start_time
    print(f"Data loaded in {elapsed_time:.6f} seconds")
    return folder_data

data_arrays = load_data_by_folder(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))

# print(data_arrays['opgave1'][0].show())
print(data_arrays['opgave1'][0].A)
data_arrays['opgave1'][0].fit.show(size=2)