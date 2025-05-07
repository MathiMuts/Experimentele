import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from Heatmap import process_heatmap

params = {
    "FILE_PATH": os.path.join(os.path.dirname(__file__), 'R5069_03581-v03.dat'),
    "OUTPUT_DIR":os.path.join(os.path.dirname(__file__), "output_images"),
    "NROFBINS": 100,
    "SI1RNGMIN": 27.6,
    "SI1RNGMAX": 30.4,
    "SI2RNGMIN": 13.8,
    "SI2RNGMAX": 15.2,
    "SI3RNGMIN": 9,
    "SI3RNGMAX": 10,
    "DELTANPMIN": 0,
    "DELTANPMAX": 10,
    "DELTANPOOP": 500,
    "SETDETRATE": 0.002,
}

process_heatmap(params)