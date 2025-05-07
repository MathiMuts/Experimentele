# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 09:38:19 2022

@author: ybaron

This file reads the .dat file and creates a desorption map based on the number of pulses
between evaporation events (thought to be an indication of poles). It also creates various other figures.
"""

import os
import time
import numpy as np
import matplotlib.pyplot as plt
import warnings
from numba import cuda
from numba.core.errors import NumbaPerformanceWarning

startTime = time.perf_counter()
warnings.simplefilter("ignore", category=NumbaPerformanceWarning)

FILENAME = 'R5069_03581-v03.dat'

folder = os.path.dirname(__file__)
output_dir = os.path.join(os.path.dirname(__file__), "output_images")
os.makedirs(output_dir, exist_ok=True)

file_path = os.path.join(folder, FILENAME)
nrofbins = 100  # number of bins used to plot FEI etc: nrofbins x nrofbins  
Si1rngmin = 27.6
Si1rngmax = 30.4
Si2rngmin = 13.8
Si2rngmax = 15.2
Si3rngmin = 9
Si3rngmax = 10
deltaNpmin = 0
deltaNpmax = 10
DeltaNpOoP = 500
SetDetRate = 0.002  # ions per pulse

''' read out file'''
with open(file_path,'r') as r:
    lines = r.read().splitlines()
    
ElementMass=[]
PulseNb=[]
Xdtc=[]
Ydtc=[]
    
i = 0
for line in lines:
    if i < 4: # first 4 lines are not data lines
        1
    else:
        Atomnumberi,Pxi,Pyi,Pzi,RangeNb,ElementMassi,PulseNbi,Vdci,Tofi,Xdtci,Ydtci = line.split() #TODO check if RangeNb makes sense
        PulseNb.append(PulseNbi)
        Xdtc.append(Xdtci)
        Ydtc.append(Ydtci)  
        ElementMass.append(ElementMassi)
    i=i+1

# convert lists to array
Xdtcar = np.array(Xdtc,dtype=float)
Ydtcar = np.array(Ydtc,dtype=float)
PulseNbar = np.array(PulseNb,dtype=float)
ElementMass = np.array(ElementMass,dtype=float)
Xdtcar = 10*Xdtcar
Ydtcar = 10*Ydtcar


'''Compute results'''
Np = PulseNbar[1::]-PulseNbar[0:(len(PulseNbar)-1):] # number of pulses between two events
for i in range(len(Np)):                             # correction for the case there is a jump from 2^24 to 0 in the pulse counter
    if Np[i]<0:
        Np[i]=Np[i]+2**24

@cuda.jit
def compute_distances(Np, Xdtcar, Ydtcar, deltaNpmin, deltaNpmax, DeltaNpOoP, Distance, DistanceOP):
    i = cuda.grid(1)
    if i < len(Np) - 1:
        deltaNp = Np[i]
        if deltaNpmin <= deltaNp <= deltaNpmax:
            Distance[i] = ((Xdtcar[i + 1] - Xdtcar[i]) ** 2 + (Ydtcar[i + 1] - Ydtcar[i]) ** 2) ** 0.5
        elif deltaNp > DeltaNpOoP:
            DistanceOP[i] = ((Xdtcar[i + 1] - Xdtcar[i]) ** 2 + (Ydtcar[i + 1] - Ydtcar[i]) ** 2) ** 0.5

# Allocate GPU memory and launch the kernel
threads_per_block = 256
blocks_per_grid = (len(Np) + threads_per_block - 1) // threads_per_block

Distance = np.zeros(len(Np), dtype=np.float32)
DistanceOP = np.zeros(len(Np), dtype=np.float32)

compute_distances[blocks_per_grid, threads_per_block](
    Np, Xdtcar, Ydtcar, deltaNpmin, deltaNpmax, DeltaNpOoP, Distance, DistanceOP
)

Xdtcor = []
Ydtcor = []
Npcor  = []

i = 0
for deltaNp in Np: # filter for the events for which there is less than a certain pulses between them
    if deltaNpmin <= deltaNp <= deltaNpmax:
        Xdtcor.append(Xdtcar[i+1])
        Ydtcor.append(Ydtcar[i+1])
        Xdtcor.append(Xdtcar[i])
        Ydtcor.append(Ydtcar[i])
        Npcor.append(deltaNp)
    i = i+1

NpMat = np.zeros([nrofbins,nrofbins]) # sum of pulse number before event
NrMat = np.zeros([nrofbins,nrofbins]) # sum oh hits on detector coordinate
NSi1 = np.zeros([nrofbins,nrofbins])  # Si charge +
NSi2 = np.zeros([nrofbins,nrofbins])  # Si charge 2+
NSi3 = np.zeros([nrofbins,nrofbins])  # Si charge 3+
rownr = np.digitize(Ydtcar,np.linspace(np.min(Ydtcar),np.max(Ydtcar),nrofbins))  # Assign all Y-coordinates to vertical bins 
colmnr = np.digitize(Xdtcar,np.linspace(np.min(Xdtcar),np.max(Xdtcar),nrofbins)) # Assign all X-coordinates to horizontal bins 

from numba import cuda
import numpy as np

@cuda.jit
def update_matrices(Np, ElementMass, rownr, colmnr, nrofbins, Si1rngmin, Si1rngmax, Si2rngmin, Si2rngmax, Si3rngmin, Si3rngmax, 
                    NpMat, NrMat, NSi1, NSi2, NSi3):
    i, j = cuda.grid(2)  # Get the 2D thread indices
    if i < nrofbins and j < nrofbins:  # Ensure we are within bounds
        for k in range(len(Np)):  # Iterate over all events
            if colmnr[k] == i + 1 and rownr[k] == j + 1:  # Match bin indices
                if k < len(Np) - 1:
                    # Update NpMat and NrMat
                    cuda.atomic.add(NpMat, (i, j), Np[k - 1])
                    cuda.atomic.add(NrMat, (i, j), 1)

                    # Update charge state matrices
                    if Si1rngmin < ElementMass[k] < Si1rngmax:
                        cuda.atomic.add(NSi1, (i, j), 1)
                    elif Si2rngmin < ElementMass[k] < Si2rngmax:
                        cuda.atomic.add(NSi2, (i, j), 1)
                    elif Si3rngmin < ElementMass[k] < Si3rngmax:
                        cuda.atomic.add(NSi3, (i, j), 1)

# Allocate GPU memory and launch the kernel
threads_per_block = (16, 16)  # Define the number of threads per block (2D grid)
blocks_per_grid_x = (nrofbins + threads_per_block[0] - 1) // threads_per_block[0]
blocks_per_grid_y = (nrofbins + threads_per_block[1] - 1) // threads_per_block[1]
blocks_per_grid = (blocks_per_grid_x, blocks_per_grid_y)

# Convert arrays to GPU-compatible data types
NpMat = np.zeros((nrofbins, nrofbins), dtype=np.float32)
NrMat = np.zeros((nrofbins, nrofbins), dtype=np.float32)
NSi1 = np.zeros((nrofbins, nrofbins), dtype=np.float32)
NSi2 = np.zeros((nrofbins, nrofbins), dtype=np.float32)
NSi3 = np.zeros((nrofbins, nrofbins), dtype=np.float32)

NpMat_gpu = cuda.to_device(NpMat)
NrMat_gpu = cuda.to_device(NrMat)
NSi1_gpu = cuda.to_device(NSi1)
NSi2_gpu = cuda.to_device(NSi2)
NSi3_gpu = cuda.to_device(NSi3)

rownr_gpu = cuda.to_device(rownr)
colmnr_gpu = cuda.to_device(colmnr)
Np_gpu = cuda.to_device(Np)
ElementMass_gpu = cuda.to_device(ElementMass)

update_matrices[blocks_per_grid, threads_per_block](
    Np_gpu, ElementMass_gpu, rownr_gpu, colmnr_gpu, nrofbins, 
    Si1rngmin, Si1rngmax, Si2rngmin, Si2rngmax, Si3rngmin, Si3rngmax, 
    NpMat_gpu, NrMat_gpu, NSi1_gpu, NSi2_gpu, NSi3_gpu
)

# Copy results back to the host
NpMat = NpMat_gpu.copy_to_host()
NrMat = NrMat_gpu.copy_to_host()
NSi1 = NSi1_gpu.copy_to_host()
NSi2 = NSi2_gpu.copy_to_host()
NSi3 = NSi3_gpu.copy_to_host()

detectionrate = (len(Np)+1)/np.sum(Np) # this is the number of hits -1 +1 / total amount of pulses. Note that pulse counter sometimes resets so not so easy to use that one.
print('Set detection rate = ' + str(SetDetRate) +' ions per pulse')
print('detection rate from data = ' + str(detectionrate) +' ions per pulse')


'''Plot results'''
# Save the first plot (DEH classic)
f1 = plt.figure(1)
plt.hist2d(Xdtcar, Ydtcar, bins=[nrofbins, nrofbins], range=np.array([(-18, 18), (-18, 18)]))
plt.gca().set_aspect('equal')
plt.gca().set_xticks([-15, -10, -5, 0, 5, 10, 15])
plt.gca().set_yticks([-15, -10, -5, 0, 5, 10, 15])
plt.xlabel('Detector x [mm]', fontsize=18)
plt.ylabel('Detector y [mm]', fontsize=18)
plt.title('Detector event histogram', fontsize=18)
plt.gca().tick_params(labelsize=13)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
f1.savefig(os.path.join(output_dir, "DEH_classic.png"))
plt.close(f1)

# Save the second plot (DEH Np filtered)
f2 = plt.figure(2)
plt.hist2d(Xdtcor, Ydtcor, bins=[nrofbins, nrofbins], range=np.array([(-18, 18), (-18, 18)]))
plt.xlabel('Detector x [mm]', fontsize=18)
plt.ylabel('Detector y [mm]', fontsize=18)
plt.title(f'DEH {deltaNpmin} ≤ Np ≤ {deltaNpmax}', fontsize=18)
plt.gca().set_aspect('equal')
plt.gca().set_xticks([-15, -10, -5, 0, 5, 10, 15])
plt.gca().set_yticks([-15, -10, -5, 0, 5, 10, 15])
plt.gca().tick_params(labelsize=13)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
f2.savefig(os.path.join(output_dir, "DEH_Np_filtered.png"))
plt.close(f2)

# Save the third plot (CSR)
f3 = plt.figure(3)
plt.imshow(np.divide(NSi2, (NSi1 + NSi2 + 1e-6))[::1, ::-1].T, vmin=0.8, extent=[np.min(Xdtcar), np.max(Xdtcar), np.min(Ydtcar), np.max(Ydtcar)])
plt.ylim([-18, 18])
plt.xlim([-18, 18])
plt.xlabel('Detector x [mm]', fontsize=18)
plt.ylabel('Detector y [mm]', fontsize=18)
plt.title('CSR', fontsize=18)
plt.gca().set_xticks([-15, -10, -5, 0, 5, 10, 15])
plt.gca().set_yticks([-15, -10, -5, 0, 5, 10, 15])
plt.gca().tick_params(labelsize=13)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
f3.savefig(os.path.join(output_dir, "CSR.png"))
plt.close(f3)

# Save the fourth plot (DEH Np filtered NORMALIZED)
f4 = plt.figure(4)
H, xedges, yedges = np.histogram2d(Xdtcar, Ydtcar, bins=nrofbins)
Hcor, xedges, yedges = np.histogram2d(Xdtcor, Ydtcor, bins=nrofbins)
plt.imshow(np.divide((Hcor), (H + 1e-15))[::1, ::-1].T, vmin=0.1, vmax=0.3, extent=[np.min(Xdtcar), np.max(Xdtcar), np.min(Ydtcar), np.max(Ydtcar)])
plt.xlabel('Detector x [mm]', fontsize=18)
plt.ylabel('Detector y [mm]', fontsize=18)
plt.title(f'DEH percentage of hits {deltaNpmin} ≤ Np ≤ {deltaNpmax}', fontsize=18)
plt.ylim([-18, 18])
plt.xlim([-18, 18])
plt.gca().set_xticks([-15, -10, -5, 0, 5, 10, 15])
plt.gca().set_yticks([-15, -10, -5, 0, 5, 10, 15])
plt.gca().tick_params(labelsize=13)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
f4.savefig(os.path.join(output_dir, "DEH_Np_filtered_normalized.png"))
plt.close(f4)

# Save the fifth plot (Average number between pulses)
f5 = plt.figure(5)
resultMat = np.divide(NpMat, NrMat + 1e-9)
plt.imshow(resultMat[::1, ::-1].T, cmap='seismic', vmin=1 / detectionrate * 0.8, vmax=1 / detectionrate * 0.95, extent=[np.min(Xdtcar), np.max(Xdtcar), np.min(Ydtcar), np.max(Ydtcar)])
plt.xlim([-18, 18])
plt.ylim([-18, 18])
plt.gca().set_xticks([-15, -10, -5, 0, 5, 10, 15])
plt.gca().set_yticks([-15, -10, -5, 0, 5, 10, 15])
plt.xlabel('Detector x [mm]', fontsize=18)
plt.ylabel('Detector y [mm]', fontsize=18)
plt.title('Average number of pulses between events', fontsize=18)
plt.gca().tick_params(labelsize=13)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
f5.savefig(os.path.join(output_dir, "Average_pulses_between_events.png"))
plt.close(f5)

# Save the sixth plot (Average number between pulses bis)
f6 = plt.figure(6)
resultMat = np.divide(NpMat, NrMat + 1e-9)
plt.imshow((np.where(resultMat > 1 / detectionrate * 0.9, 0, resultMat))[::1, ::-1].T, extent=[np.min(Xdtcar), np.max(Xdtcar), np.min(Ydtcar), np.max(Ydtcar)])
plt.xlabel('Detector x [mm]', fontsize=18)
plt.ylabel('Detector y [mm]', fontsize=18)
plt.title('Average number of pulses between events', fontsize=18)
plt.xlim([-18, 18])
plt.ylim([-18, 18])
plt.gca().set_xticks([-15, -10, -5, 0, 5, 10, 15])
plt.gca().set_yticks([-15, -10, -5, 0, 5, 10, 15])
plt.gca().tick_params(labelsize=13)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
f6.savefig(os.path.join(output_dir, "Average_pulses_between_events_bis.png"))
plt.close(f6)

endTime = time.perf_counter()
print(f"All plots have been saved to {output_dir}.\nThe script took {endTime - startTime:.6f} seconds to execute.")