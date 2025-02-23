import os
import numpy as np
import csv

def convert_txt_to_csv(file_path):
    """
    Converts a .txt file to a .csv file by reading tab-delimited data
    and saving it as comma-separated values.
    """
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    base, _ = os.path.splitext(file_path)
    csv_file_path = base + ".csv"

    try:
        with open(file_path, 'r') as file:
            header = [next(file).strip() for _ in range(9)]
        # Load data from the text file
        data = np.genfromtxt(file_path, delimiter="\t\t", skip_header=9)

        # Save the data to a CSV file
        with open(csv_file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for line in header:
                writer.writerow([line])
            writer.writerows(data)
        
        os.remove(file_path)      
        print(f"Conversion successful: {csv_file_path}")
    except Exception as e:
        print(f"Error converting file: {e}")

def get_lowest_folders(root):
    lowest_folders = []
    for dirpath, dirnames, filenames in os.walk(root):
        if not dirnames:
            lowest_folders.append(dirpath)
    return lowest_folders

def load_data_by_folder(root):
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
                # os.system(f'echo "File: {current_file:>3}/{total_files}"')
                # data_list.append(data_from_file(file_path))
                print(file_path)
                convert_txt_to_csv(os.path.join(os.path.dirname(os.path.abspath(os.getcwd())), file_path))
        
        if data_list:
            folder_data[folder_name] = np.array(data_list)
    return folder_data

load_data_by_folder(os.path.join(os.path.abspath(os.getcwd()), "data"))