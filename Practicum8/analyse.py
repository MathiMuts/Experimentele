import fit_classes as fp
import numpy as np
import os
import time
from scipy.interpolate import interp1d
from scipy import optimize

errors = []
ERROR = 2 # Error in mV

class DataPlus(fp.Data):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def sinus_model(params, x):
            A,f,phi,c = params
            return A*np.sin(2*np.pi*f*x + phi) + c
        
        A, f, phi, c = 100, 0.006, -13.06097, 25
        A = (np.abs(max(self.y)) + np.abs(min(self.y)))/2
        c = (max(self.y) + min(self.y))/2*1.0001

        f_interp = interp1d(self.x, self.y, kind='cubic')
        x_dense = np.linspace(self.x.min(), self.x.max(), 1000)
        y_dense = f_interp(x_dense)

        crossings = []
        for i in range(len(x_dense)-1):
            if (y_dense[i] - c) * (y_dense[i+1] - c) < 0:  # Sign change
                # Refine crossing with brentq
                root = optimize.brentq(lambda x_val: f_interp(x_val) - c, x_dense[i], x_dense[i+1])
                crossings.append(root)
                # punt
                # if self.x[list(self.x).index(punt) - 5] > self.x[list(self.x).index(punt) + 5]:
                #     dalende_root.append(punt)


        # Find descending zero-crossings
        stijgende_root = []
        for i in range(len(self.y) - 2):
            if (self.y[i - 1] + self.y[i - 2])/2 < c and (self.y[i + 1] + self.y[i + 2])/2 >= c and self.x[i] > 10:
                if stijgende_root != []:
                    if self.x[i] - stijgende_root[-1] > 10:
                        stijgende_root.append(self.x[i])
                else:
                    stijgende_root.append(self.x[i])
        
        f = len(crossings)/20000
        print(f"A = {A}")
        print(f"c = {c}")
        # print(f"crossings = {crossings}")
        print(f"##crossings = {len(crossings)}")
        phi = -(stijgende_root[0]*f)*2*np.pi

        FIT_POINTS = 400

        self.x = self.x[:FIT_POINTS][::3]
        self.y = self.y[:FIT_POINTS][::2]
        self.dx = self.dx[:FIT_POINTS][::2]
        self.dy = self.dy[:FIT_POINTS][::2]


        self.fit = self.fit(sinus_model, initial_guess=(A, f, phi, c))
        self.fit.init = A, f, phi, c

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
    print("----------------------------------------------------------------------------------------------------------------")
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
                print(f"-------------------------------------")
                print(f"File: {current_file:>3}/{total_files}")
                data_list.append(data_from_file(file_path))
        
        if data_list:
            folder_data[folder_name] = np.array(data_list)

    elapsed_time = time.time() - start_time
    print("----------------------------------------------------------------------------------------------------------------")
    print(f"Data loaded in {elapsed_time:.6f} seconds")
    print("----------------------------------------------------------------------------------------------------------------")
    return folder_data

data_arrays = load_data_by_folder(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))

for error in errors:
    print(error)
# print(data_arrays['opgave1'][0].show())
#print(data_arrays['opgave2_1'][16].fit)
#print(data_arrays['opgave2_1'][16].fit.init)
# print(data_arrays['opgave1'][0].A) # amplitude
# print(data_arrays['opgave1'][0].f) # hoekfreq
#data_arrays['opgave1'][0].fit.show(size=2, fit_guess=True)
#data_arrays['opgave2_1'][16].fit.show(size=2, fit_guess=True)
print(data_arrays['opgave1'][0].fit)
print(data_arrays['opgave1'][0].show())
