# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 09:38:19 2022

@authors: ybaron, Mathias, Michail

This file reads the .dat file and creates a desorption map based on the number of pulses
between evaporation events (thought to be an indication of poles). It also creates various other figures.
"""

import os
import time
import numpy as np
import matplotlib.pyplot as plt
import warnings
from numba import cuda, njit, prange
from numba.core.errors import NumbaPerformanceWarning
warnings.simplefilter("ignore", category=NumbaPerformanceWarning)


def process_heatmap(params, Cuda=False):
    print("------------------START-SCRIPT--------------------")
    startTime = time.perf_counter()
    tempTime = time.perf_counter()

    # Extract parameters from the dictionary
    FILE_PATH = params["FILE_PATH"]
    OUTPUT_DIR = params["OUTPUT_DIR"]
    NROFBINS = params["NROFBINS"]
    SI1RNGMIN = params["SI1RNGMIN"]
    SI1RNGMAX = params["SI1RNGMAX"]
    SI2RNGMIN = params["SI2RNGMIN"]
    SI2RNGMAX = params["SI2RNGMAX"]
    SI3RNGMIN = params["SI3RNGMIN"]
    SI3RNGMAX = params["SI3RNGMAX"]
    DELTANPMIN = params["DELTANPMIN"]
    DELTANPMAX = params["DELTANPMAX"]
    DELTANPOOP = params["DELTANPOOP"]


    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Read the file
    with open(FILE_PATH, 'r') as r:
        lines = r.read().splitlines()

    dataInlaadTijd = time.perf_counter() - tempTime
    print(f"- Loading in RAM: {dataInlaadTijd:.3f}s")
    tempTime = time.perf_counter()

    # Parse the data
    ElementMass = []
    PulseNb = []
    Xdtc = []
    Ydtc = []

    columns4 = len(lines[0].split(",")) == 4

    for i, line in enumerate(lines[4:]):
        if columns4:
            ElementMassi, Xdtci, Ydtci, PulseNbi = line.split(",")
        else:
            Atomnumberi, Pxi, Pyi, Pzi, RangeNb, ElementMassi, PulseNbi, Vdci, Tofi, Xdtci, Ydtci = line.split()
        PulseNb.append(PulseNbi)
        Xdtc.append(Xdtci)
        Ydtc.append(Ydtci)
        ElementMass.append(ElementMassi)

    # Convert lists to arrays
    Xdtcar = np.array(Xdtc, dtype=float)
    Ydtcar = np.array(Ydtc, dtype=float)
    PulseNbar = np.array(PulseNb, dtype=float)
    ElementMass = np.array(ElementMass, dtype=float)
    Xdtcar = 1 * Xdtcar # INFO: daar stond maal 10
    Ydtcar = 1 * Ydtcar

    dataParseTijd = time.perf_counter() - tempTime
    print(f"- Parsing the data: {dataParseTijd:.3f}s")
    tempTime = time.perf_counter()

    # Compute results
    Np = np.array(PulseNbar[1:], dtype=float)

    # GPU kernel for distance computation
    threads_per_block = 256
    blocks_per_grid = (len(Np) + threads_per_block - 1) // threads_per_block

    Distance = np.zeros(len(Np), dtype=np.float32)
    DistanceOP = np.zeros(len(Np), dtype=np.float32)

    if Cuda:
        # ---- GPU distance computation ----
        @cuda.jit
        def compute_distances_GPU(Np, Xdtcar, Ydtcar, DELTANPMIN, DELTANPMAX, DELTANPOOP, Distance, DistanceOP):
            i = cuda.grid(1)
            if i < len(Np) - 1:
                deltaNp = Np[i]
                if DELTANPMIN <= deltaNp <= DELTANPMAX:
                    Distance[i] = ((Xdtcar[i + 1] - Xdtcar[i]) ** 2 + (Ydtcar[i + 1] - Ydtcar[i]) ** 2) ** 0.5
                elif deltaNp > DELTANPOOP:
                    DistanceOP[i] = ((Xdtcar[i + 1] - Xdtcar[i]) ** 2 + (Ydtcar[i + 1] - Ydtcar[i]) ** 2) ** 0.5

        compute_distances_GPU[blocks_per_grid, threads_per_block](
            Np, Xdtcar, Ydtcar, DELTANPMIN, DELTANPMAX, DELTANPOOP, Distance, DistanceOP
        )

    else:
        # ---- CPU distance computation ----
        @njit(parallel=True)
        def compute_distances_cpu(Np, Xdtcar, Ydtcar, DELTANPMIN, DELTANPMAX, DELTANPOOP, Distance, DistanceOP):
            for i in prange(len(Np) - 1):
                deltaNp = Np[i]
                dx = Xdtcar[i + 1] - Xdtcar[i]
                dy = Ydtcar[i + 1] - Ydtcar[i]
                dist = (dx ** 2 + dy ** 2) ** 0.5
                if DELTANPMIN <= deltaNp <= DELTANPMAX:
                    Distance[i] = dist
                elif deltaNp > DELTANPOOP:
                    DistanceOP[i] = dist

        compute_distances_cpu(Np, Xdtcar, Ydtcar, DELTANPMIN, DELTANPMAX, DELTANPOOP, Distance, DistanceOP)

    dataComputeDistanceTijd = time.perf_counter() - tempTime
    print(f"- Calculating the distances: {dataComputeDistanceTijd:.3f}s")
    tempTime = time.perf_counter()

    # Filter events
    Xdtcor = []
    Ydtcor = []
    Npcor = []

    for i, deltaNp in enumerate(Np):
        if DELTANPMIN <= deltaNp <= DELTANPMAX:
            Xdtcor.append(Xdtcar[i + 1])
            Ydtcor.append(Ydtcar[i + 1])
            Xdtcor.append(Xdtcar[i])
            Ydtcor.append(Ydtcar[i])
            Npcor.append(deltaNp)

    # Initialize matrices
    NpMat = np.zeros([NROFBINS, NROFBINS], dtype=np.float32)
    NrMat = np.zeros([NROFBINS, NROFBINS], dtype=np.float32)
    NSi1 = np.zeros([NROFBINS, NROFBINS], dtype=np.float32)
    NSi2 = np.zeros([NROFBINS, NROFBINS], dtype=np.float32)
    NSi3 = np.zeros([NROFBINS, NROFBINS], dtype=np.float32)

    rownr = np.digitize(Ydtcar, np.linspace(np.min(Ydtcar), np.max(Ydtcar), NROFBINS))
    colmnr = np.digitize(Xdtcar, np.linspace(np.min(Xdtcar), np.max(Xdtcar), NROFBINS))    


    if Cuda:
        # ---- GPU matrix update ----
        # GPU kernel for matrix updates
        threads_per_block = (16, 16)
        blocks_per_grid_x = (NROFBINS + threads_per_block[0] - 1) // threads_per_block[0]
        blocks_per_grid_y = (NROFBINS + threads_per_block[1] - 1) // threads_per_block[1]
        blocks_per_grid = (blocks_per_grid_x, blocks_per_grid_y)

        NpMat_gpu = cuda.to_device(NpMat)
        NrMat_gpu = cuda.to_device(NrMat)
        NSi1_gpu = cuda.to_device(NSi1)
        NSi2_gpu = cuda.to_device(NSi2)
        NSi3_gpu = cuda.to_device(NSi3)

        rownr_gpu = cuda.to_device(rownr)
        colmnr_gpu = cuda.to_device(colmnr)
        Np_gpu = cuda.to_device(Np)
        ElementMass_gpu = cuda.to_device(ElementMass)
        @cuda.jit
        def update_matrices(Np, ElementMass, rownr, colmnr, NROFBINS, SI1RNGMIN, SI1RNGMAX, SI2RNGMIN, SI2RNGMAX, SI3RNGMIN, SI3RNGMAX, NpMat, NrMat, NSi1, NSi2, NSi3):
            i, j = cuda.grid(2)  # Get the 2D thread indices
            if i < NROFBINS and j < NROFBINS:  # Ensure we are within bounds
                for k in range(len(Np)):  # Iterate over all events
                    if colmnr[k] == i + 1 and rownr[k] == j + 1:  # Match bin indices
                        if k < len(Np) - 1:
                            # Update NpMat and NrMat
                            cuda.atomic.add(NpMat, (i, j), Np[k - 1])
                            cuda.atomic.add(NrMat, (i, j), 1)

                            # Update charge state matrices
                            if SI1RNGMIN < ElementMass[k] < SI1RNGMAX:
                                cuda.atomic.add(NSi1, (i, j), 1)
                            elif SI2RNGMIN < ElementMass[k] < SI2RNGMAX:
                                cuda.atomic.add(NSi2, (i, j), 1)
                            elif SI3RNGMIN < ElementMass[k] < SI3RNGMAX:
                                cuda.atomic.add(NSi3, (i, j), 1)

        update_matrices[blocks_per_grid, threads_per_block](
            Np_gpu, ElementMass_gpu, rownr_gpu, colmnr_gpu, NROFBINS,
            SI1RNGMIN, SI1RNGMAX, SI2RNGMIN, SI2RNGMAX, SI3RNGMIN, SI3RNGMAX,
            NpMat_gpu, NrMat_gpu, NSi1_gpu, NSi2_gpu, NSi3_gpu
        )
        NpMat = NpMat_gpu.copy_to_host()
        NrMat = NrMat_gpu.copy_to_host()
        NSi1 = NSi1_gpu.copy_to_host()
        NSi2 = NSi2_gpu.copy_to_host()
        NSi3 = NSi3_gpu.copy_to_host()

    else:
        # ---- CPU matrix update ----
        @njit(parallel=True)
        def update_matrices_cpu(Np, ElementMass, rownr, colmnr, NpMat, NrMat, NSi1, NSi2, NSi3,
                                SI1RNGMIN, SI1RNGMAX, SI2RNGMIN, SI2RNGMAX, SI3RNGMIN, SI3RNGMAX):
            for k in prange(len(Np)):
                i = colmnr[k] - 1
                j = rownr[k] - 1
                if 0 <= i < NROFBINS and 0 <= j < NROFBINS:
                    NpMat[i, j] += Np[k - 1] if k > 0 else 0
                    NrMat[i, j] += 1
                    mass = ElementMass[k]
                    if SI1RNGMIN < mass < SI1RNGMAX:
                        NSi1[i, j] += 1
                    elif SI2RNGMIN < mass < SI2RNGMAX:
                        NSi2[i, j] += 1
                    elif SI3RNGMIN < mass < SI3RNGMAX:
                        NSi3[i, j] += 1

        update_matrices_cpu(Np, ElementMass, rownr, colmnr, NpMat, NrMat, NSi1, NSi2, NSi3,
                            SI1RNGMIN, SI1RNGMAX, SI2RNGMIN, SI2RNGMAX, SI3RNGMIN, SI3RNGMAX)

    detectionrate = (len(Np) + 1) / np.sum(Np)

    dataComputeResultsTijd = time.perf_counter() - tempTime
    print(f"- Calculating the results: {dataComputeResultsTijd:.3f}s")
    tempTime = time.perf_counter()

    '''Plot results'''
    LIMIT = 1.75
    TICKS = [-1.5, -0.75, 0, 0.75, 1.5]
    # Save the first plot (DEH classic)
    f1 = plt.figure(1)
    plt.hist2d(Xdtcar, Ydtcar, bins=[NROFBINS, NROFBINS], range=np.array([(-LIMIT, LIMIT), (-LIMIT, LIMIT)]))
    plt.gca().set_aspect('equal')
    plt.gca().set_xticks(TICKS)
    plt.gca().set_yticks(TICKS)
    plt.xlabel('Detector x [mm]', fontsize=18)
    plt.ylabel('Detector y [mm]', fontsize=18)
    plt.title('Detector event histogram', fontsize=18)
    plt.gca().tick_params(labelsize=13)
    cb = plt.colorbar()
    cb.ax.tick_params(labelsize=14)
    f1.savefig(os.path.join(OUTPUT_DIR, "DEH_classic.png"), dpi=500)
    plt.close(f1)

    # Save the second plot (DEH Np filtered)
    f2 = plt.figure(2)
    plt.hist2d(Xdtcor, Ydtcor, bins=[NROFBINS, NROFBINS], range=np.array([(-LIMIT, LIMIT), (-LIMIT, LIMIT)]))
    plt.xlabel('Detector x [mm]', fontsize=18)
    plt.ylabel('Detector y [mm]', fontsize=18)
    plt.title(f'DEH {DELTANPMIN} ≤ Np ≤ {DELTANPMAX}', fontsize=18)
    plt.gca().set_aspect('equal')
    plt.gca().set_xticks(TICKS)
    plt.gca().set_yticks(TICKS)
    plt.gca().tick_params(labelsize=13)
    cb = plt.colorbar()
    cb.ax.tick_params(labelsize=14)
    f2.savefig(os.path.join(OUTPUT_DIR, "DEH_Np_filtered.png"), dpi=500)
    plt.close(f2)

    # Save the third plot (CSR)
    f3 = plt.figure(3)
    plt.imshow(np.divide(NSi2, (NSi1 + NSi2 + 1e-6))[::1, ::-1].T, vmin=0.8, extent=[np.min(Xdtcar), np.max(Xdtcar), np.min(Ydtcar), np.max(Ydtcar)])
    plt.ylim([-LIMIT, LIMIT])
    plt.xlim([-LIMIT, LIMIT])
    plt.xlabel('Detector x [mm]', fontsize=18)
    plt.ylabel('Detector y [mm]', fontsize=18)
    plt.title('CSR', fontsize=18)
    plt.gca().set_xticks(TICKS)
    plt.gca().set_yticks(TICKS)
    plt.gca().tick_params(labelsize=13)
    cb = plt.colorbar()
    cb.ax.tick_params(labelsize=14)
    f3.savefig(os.path.join(OUTPUT_DIR, "CSR.png"), dpi=500)
    plt.close(f3)

    # Save the fourth plot (DEH Np filtered NORMALIZED)
    f4 = plt.figure(4)
    H, xedges, yedges = np.histogram2d(Xdtcar, Ydtcar, bins=NROFBINS)
    Hcor, xedges, yedges = np.histogram2d(Xdtcor, Ydtcor, bins=NROFBINS)
    plt.imshow(np.divide((Hcor), (H + 1e-15))[::1, ::-1].T, vmin=0.1, vmax=0.3, extent=[np.min(Xdtcar), np.max(Xdtcar), np.min(Ydtcar), np.max(Ydtcar)])
    plt.xlabel('Detector x [mm]', fontsize=18)
    plt.ylabel('Detector y [mm]', fontsize=18)
    plt.title(f'DEH percentage of hits {DELTANPMIN} ≤ Np ≤ {DELTANPMAX}', fontsize=18)
    plt.ylim([-LIMIT, LIMIT])
    plt.xlim([-LIMIT, LIMIT])
    plt.gca().set_xticks(TICKS)
    plt.gca().set_yticks(TICKS)
    plt.gca().tick_params(labelsize=13)
    cb = plt.colorbar()
    cb.ax.tick_params(labelsize=14)
    f4.savefig(os.path.join(OUTPUT_DIR, "DEH_Np_filtered_normalized.png"), dpi=500)
    plt.show()
    plt.close(f4)

    # Save the fifth plot (Average number between pulses)
    f5 = plt.figure(5)
    resultMat = np.divide(NpMat, NrMat + 1e-9)
    plt.imshow(resultMat[::1, ::-1].T, cmap='seismic', vmin=1 / detectionrate * 0.8, vmax=1 / detectionrate * 0.95, extent=[np.min(Xdtcar), np.max(Xdtcar), np.min(Ydtcar), np.max(Ydtcar)])
    plt.xlim([-LIMIT, LIMIT])
    plt.ylim([-LIMIT, LIMIT])
    plt.gca().set_xticks(TICKS)
    plt.gca().set_yticks(TICKS)
    plt.xlabel('Detector x [mm]', fontsize=18)
    plt.ylabel('Detector y [mm]', fontsize=18)
    plt.title('Average number of pulses between events', fontsize=18)
    plt.gca().tick_params(labelsize=13)
    cb = plt.colorbar()
    cb.ax.tick_params(labelsize=14)
    f5.savefig(os.path.join(OUTPUT_DIR, "Average_pulses_between_events.png"), dpi=500)
    plt.close(f5)

    # Save the sixth plot (Average number between pulses bis)
    f6 = plt.figure(6)
    resultMat = np.divide(NpMat, NrMat + 1e-9)
    plt.imshow((np.where(resultMat > 1 / detectionrate * 0.9, 0, resultMat))[::1, ::-1].T, extent=[np.min(Xdtcar), np.max(Xdtcar), np.min(Ydtcar), np.max(Ydtcar)])
    plt.xlabel('Detector x [mm]', fontsize=18)
    plt.ylabel('Detector y [mm]', fontsize=18)
    plt.title('Average number of pulses between events', fontsize=18)
    plt.xlim([-LIMIT, LIMIT])
    plt.ylim([-LIMIT, LIMIT])
    plt.gca().set_xticks(TICKS)
    plt.gca().set_yticks(TICKS)
    plt.gca().tick_params(labelsize=13)
    cb = plt.colorbar()
    cb.ax.tick_params(labelsize=14)
    f6.savefig(os.path.join(OUTPUT_DIR, "Average_pulses_between_events_bis.png"), dpi=500)
    plt.close(f6)

    dataGenImagesTijd = time.perf_counter() - tempTime
    print(f"- Generating the images: {dataGenImagesTijd:.3f}s")
    tempTime = time.perf_counter()

    endTime = time.perf_counter()
    print("--------------------")
    print(f"- All plots have been saved to {OUTPUT_DIR}")
    print(f"- Executing the script: {endTime - startTime:.3f}s")
    print("-------------------END--SCRIPT--------------------")


if __name__ == "__main__":
    print("This should not be executed on it's own")