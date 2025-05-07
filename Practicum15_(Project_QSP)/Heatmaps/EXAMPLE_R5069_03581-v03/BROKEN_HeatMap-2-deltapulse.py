# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 09:38:19 2022

@author: ybaron

This file reads the .dat file and creates a desorption map based on the number of pulses
between evaporation events (thought to be an indication of poles). It also creates various other figures.
"""

# from IPython import get_ipython
# get_ipython().magic('reset -sf')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# NOTE: there are quite some free prms in this script: perhaps bring them to "preamble" so that all def's are here.

file_path = 'R5069_03581-v03.dat'
nrofbins = 100 # number of bins used to plot FEI etc: nrofbins x nrofbins 
Si1rngmin = 27.6
Si1rngmax = 30.4
Si2rngmin = 13.9
Si2rngmax = 15.5
Si3rngmin = 9
Si3rngmax = 10
deltaNpmin = 1
deltaNpmax = 10
DeltaNpOoP = 2000
SetDetRate =  0.002 #ions per pulse

#below code is for text / .dat file
# ''' read out file'''
# with open(file_path,'r') as r:
#    lines = r.read().splitlines()

# below code reads in csv file mking a panda's object.
lines = pd.read_csv(file_path)
# below code is when text.dat is loaded, colums extracted, and converted to a (numpy array)     
# ElementMass=[]
# PulseNb=[]
# Xdtc=[]
# Ydtc=[]
   
# i = 0
# for line in lines:
#     if i < 1: # first 4 lines are not data lines
#         1
#     else:
#         #Atomnumberi,Pxi,Pyi,Pzi,RangeNb,ElementMassi,PulseNbi,Vdci,Tofi,Xdtci,Ydtci = line.split() #TODO check if RangeNb makes sense
#         # PulseNb.append(PulseNbi)
#         # Xdtc.append(Xdtci)
#         # Ydtc.append(Ydtci)  
#         #ElementMass.append(ElementMassi)
#         PulseNb.append(lines[i].split()[1])
#         Xdtc.append(lines[i].split()[3])
#         Ydtc.append(lines[i].split()[4])  
#         ElementMass.append(lines[i].split()[2])
#     i=i+1


# # convert lists to array
# Xdtcar = np.array(Xdtc,dtype=float)
# Ydtcar = np.array(Ydtc,dtype=float)
# PulseNbar = np.array(PulseNb,dtype=float)
# ElementMass = np.array(ElementMass,dtype=float)
# Xdtcar = 10*Xdtcar
# Ydtcar = 10*Ydtcar

#below code if for when file is loaded as CSV using panda, and proper columns need to be extracted as numpy arrays.
ElementMass = lines["Mass"]
#PulseNb = lines["pulse"]
NpRead = lines["Delta Pulse"]
Xdtc=lines["XDet_mm"]
Ydtc=lines["YDet_mm"]

ElementMassar = ElementMass.array
#PulseNbar = PulseNb.array
Npfull = NpRead.array
Xdtcar = Xdtc.array
Ydtcar = Ydtc.array

#'''Compute results'''
#Np = PulseNbar[1::]-PulseNbar[0:(len(PulseNbar)-1):] 
# number of pulses between two events: subtract from 2nd>last element, the 1st>second to last element.
# So Np = (second - first pulses, third - second pulses, ..... , last - second to last pulses)
# So, NP is one SHORTER than PulseNBar of course....
#for i in range(len(Np)):                             # correction for the case there is a jump from 2^24 to 0 in the pulse counter
#    if Np[i]<0:
#        Np[i]=Np[i]+2**24

#To be consistent with earlier method, we need to throw away the first element of NPfull (first entry always zero). this is index 0
Np=Npfull[1:]

Xdtcor = []
Ydtcor = []
Npcor  = []
Distance = []   # distance consecutive hits of which one is potentially pole
DistanceOP = [] # distance outside of poles

i = 0;
for deltaNp in Np: # filter for the events for which there is less than a certain pulses between them
    if deltaNpmin<=deltaNp<=deltaNpmax:
        Xdtcor.append(Xdtcar[i+1])
        # if Np[i] is w/i criterion, the "followed" ion is added: if second-first is w/i crit, then the second is added to Xdtcor
        Ydtcor.append(Ydtcar[i+1])
        Xdtcor.append(Xdtcar[i])
        # if Np[i] is w/i criterion, the "first" ion is added: if second-first is w/i crit, then the first is added to Xdtcor
        Ydtcor.append(Ydtcar[i])
        # Note htat in this case, BOTH first and second ion are in Xdtcor, unless one of them is commented.
        Distance.append(np.sqrt((Xdtcar[i+1]-Xdtcar[i])**2+(Ydtcar[i+1]-Ydtcar[i])**2)) # Distance between the consecutive events
        Npcor.append(deltaNp)   #Npcor has all deltaNp's within criterion. same length as Distance, half lenght of Xdtcor...
    elif deltaNp>DeltaNpOoP: # some kind of definiton for outside of pole: to be checked with average det rate I guess.
        DistanceOP.append(np.sqrt((Xdtcar[i+1]-Xdtcar[i])**2+(Ydtcar[i+1]-Ydtcar[i])**2))
    i = i+1

#Matrix: [row,column] 
NpMat = np.zeros([nrofbins,nrofbins]) # Matrix - sum of pulse number before event
NrMat = np.zeros([nrofbins,nrofbins]) # Matrix - sum of hits on detector coordinate
NSi1 = np.zeros([nrofbins,nrofbins])  # Matrix - Si charge +
NSi2 = np.zeros([nrofbins,nrofbins])  # Matrix - Si charge 2+
NSi3 = np.zeros([nrofbins,nrofbins])  # Matrix - Si charge 3+
rownr = np.digitize(Ydtcar,np.linspace(np.min(Ydtcar),np.max(Ydtcar),nrofbins))  # Assign all Y-coordinates to vertical bins 
# syntax: digitize( Array to be binned, " an array which is the "bin definition")
# in this case the bin definition is an array (linspace) between the min and max Y coordinate, even spaced by nrbins
# the output of rownr is same as Ydtcar, but it just evy Y coordinate is given a row nr between 1 -> nrofbins
colmnr = np.digitize(Xdtcar,np.linspace(np.min(Xdtcar),np.max(Xdtcar),nrofbins)) # Assign all X-coordinates to horizontal bins 

for i in range(1,nrofbins): # i = rownumbers
    print(round(i/nrofbins*100,0),"%") # gives a nice visual on progress. We go row by row. changed to %
    for k in np.array(np.where(colmnr==i),dtype=int).T: #k is going through all rows of a certain column T=transpose
        j = rownr[k]-1  #j is the index of a column in certain column  note that rownr goes from 1 to nrofbins
        if k<len(Np)-1:
            # calculating average number of pulses between events
            # first one this is simply sum of pulse numbers between events like above?
            NpMat[i,j]=NpMat[i,j]+Np[int(k-1)]
            #this is the total number of hits of a certain pixel
            NrMat[i,j]=NrMat[i,j]+1
            
            # calculating charge state
            if Si1rngmin<ElementMassar[k]<Si1rngmax:
                NSi1[i,j]= NSi1[i,j]+1
            elif Si2rngmin<ElementMassar[k]<Si2rngmax:
                NSi2[i,j]= NSi2[i,j]+1
            elif Si3rngmin<ElementMassar[k]<Si3rngmax:
                NSi3[i,j]= NSi3[i,j]+1
                
detectionrate = (len(Np)+1)/np.sum(Np) # this is the number of hits -1 +1 / total amount of pulses. Note that pulse counter sometimes resets so not so easy to use that one.
print('Set detection rate = ' + str(SetDetRate) +' ions per pulse')
print('detection rate from data = ' + str(detectionrate) +' ions per pulse')

'''Plot results'''
'''DEH (classic)'''
f1=plt.figure(1)
#plt.subplot(2,3,1)
# plt.figure(figsize=(9/1.5,7/1.5))
plt.hist2d(Xdtcar,Ydtcar,bins=[nrofbins,nrofbins], range=np.array([(-18,18), (-18,18)]))    # standard FEI
plt.gca().set_aspect('equal')
plt.gca().set_xticks([-15, -10, -5, 0, 5, 10, 15])
plt.gca().set_yticks([-15, -10, -5, 0, 5, 10, 15])
plt.xlabel('Detector x [mm]', fontsize=18);plt.ylabel('Detector y [mm]', fontsize=18);plt.title('Detector event histogram', fontsize=18)
plt.gca().tick_params(labelsize=13)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)

'''DEH (Np filtered)'''
f2=plt.figure(2)
#plt.subplot(2,3,2)
plt.hist2d(Xdtcor,Ydtcor,bins=[nrofbins,nrofbins], range=np.array([(-18,18), (-18,18)]))     
plt.xlabel('Detector x [mm]', fontsize=18);plt.ylabel('Detector y [mm]', fontsize=18);plt.title('DEH ' + str(deltaNpmin) + ' $\leq$ Np $\leq$ '+ str(deltaNpmax), fontsize=18) # change to input prm.
plt.gca().set_aspect('equal')
plt.gca().set_xticks([-15, -10, -5, 0, 5, 10, 15])
plt.gca().set_yticks([-15, -10, -5, 0, 5, 10, 15])
plt.gca().tick_params(labelsize=13)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)

'''CSR'''
f3=plt.figure(3)
#plt.subplot(2,3,3)  # CSR, ignore for now.
plt.imshow(np.divide(NSi2,(NSi1+NSi2+1e-6))[::1,::-1].T,vmin=0.8,extent=[np.min(Xdtcar),np.max(Xdtcar),np.min(Ydtcar),np.max(Ydtcar)])
plt.ylim([-18,18])
plt.xlim([-18,18])
plt.xlabel('Detector x [mm]', fontsize=18);plt.ylabel('Detector y [mm]', fontsize=18);plt.title('CSR', fontsize=18)
plt.gca().set_xticks([-15, -10, -5, 0, 5, 10, 15])
plt.gca().set_yticks([-15, -10, -5, 0, 5, 10, 15])
plt.gca().tick_params(labelsize=13)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)

'''DEH (Np filtered NORMALIZED)'''
f4=plt.figure(4)
#plt.subplot(2,3,4) # division of NP< criterion divided by total (classical) dens map. straightforward
H,xedges,yedges=np.histogram2d(Xdtcar,Ydtcar,bins=nrofbins)
Hcor,xedges,yedges=np.histogram2d(Xdtcor,Ydtcor,bins=nrofbins)
# plt.imshow(np.divide((H-Hcor),(H+1e-15))[::1,::-1].T,vmin=0.7,vmax=1,extent=[np.min(Xdtcar),np.max(Xdtcar),np.min(Ydtcar),np.max(Ydtcar)])
plt.imshow(np.divide((Hcor),(H+1e-15))[::1,::-1].T,vmin = 0.1,vmax=0.2,extent=[np.min(Xdtcar),np.max(Xdtcar),np.min(Ydtcar),np.max(Ydtcar)])
#plt.imshow(np.divide((Hcor),(H+1e-15))[::1,::-1].T,vmin = 0.1,vmax=0.3)
plt.xlabel('Detector x [mm]',fontsize=18);plt.ylabel('Detector y [mm]', fontsize=18);plt.title('DEH percentage of hits '+ str(deltaNpmin) + ' $\leq$ Np $\leq$ '+ str(deltaNpmax), fontsize=18)
plt.ylim([-18,18])
plt.xlim([-18,18])
plt.gca().set_xticks([-15, -10, -5, 0, 5, 10, 15])
plt.gca().set_yticks([-15, -10, -5, 0, 5, 10, 15])
plt.gca().tick_params(labelsize=13)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)

'''Average number between pulses'''
f5=plt.figure(5)
#plt.subplot(2,3,5)
detectionrate = (len(Np)+1)/np.sum(Np) # this is the number of hits -1 +1 / total amount of pulses. Note that pulse counter sometimes resets so not so easy to use that one.
resultMat = np.divide(NpMat,NrMat+1e-9) 
# divide sum of inbetween pulses / all pulses: formule for average (per pixel)
plt.imshow(resultMat[::1,::-1].T,cmap='seismic',vmin=1/detectionrate*0.8, vmax=1/detectionrate*0.95,extent=[np.min(Xdtcar),np.max(Xdtcar),np.min(Ydtcar),np.max(Ydtcar)])
plt.xlim([-18,18])
plt.ylim([-18,18])
plt.gca().set_xticks([-15, -10, -5, 0, 5, 10, 15])
plt.gca().set_yticks([-15, -10, -5, 0, 5, 10, 15])
plt.xlabel('Detector x [mm]', fontsize=18);plt.ylabel('Detector y [mm]', fontsize=18);plt.title('Average number of pulses between events', fontsize=18)
plt.gca().tick_params(labelsize=13)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)

'''Average number between pulses bis'''
f6=plt.figure(6)
#plt.subplot(2,3,6)
detectionrate = len(Np)/np.sum(Np)
resultMat=np.divide(NpMat,NrMat+1e-9)
plt.imshow((np.where(resultMat>1/detectionrate*0.9,0,resultMat))[::1,::-1].T,extent=[np.min(Xdtcar),np.max(Xdtcar),np.min(Ydtcar),np.max(Ydtcar)])
plt.xlabel('Detector x [mm]',fontsize=18);plt.ylabel('Detector y [mm]', fontsize=18);plt.title('Average number of pulses between events', fontsize=18)
plt.xlim([-18,18])
plt.ylim([-18,18])
plt.gca().set_xticks([-15, -10, -5, 0, 5, 10, 15])
plt.gca().set_yticks([-15, -10, -5, 0, 5, 10, 15])
plt.gca().tick_params(labelsize=13)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)


plt.figure()
#plt.subplot(1,2,1)
x,bins = np.histogram(Distance,bins=300)
xop,bins = np.histogram(DistanceOP,bins=300)
bincor = 0.5*(bins[1:]+bins[:-1])
#plt.plot(bincor,x/np.max(x));
#plt.plot(bincor,xop/np.max(xop))
plt.hist(Distance, bins=300)
plt.xlabel('Hit distance [mm] ' + str(deltaNpmin) + ' $\leq$ Np $\leq$ '+ str(deltaNpmax), fontsize=18);plt.ylabel('Counts', fontsize=18);plt.title('', fontsize=18)
plt.gca().tick_params(labelsize=13)
plt.xlim([0,3])
plt.ylim([0,2e5])
#plt.legend(['Pole locations','Not pole locations'])
# plt.subplot(1,2,2)
# plt.hist(DistanceOP,bins=200)
# plt.xlabel('Distance consecutive events');plt.ylabel('Count');plt.title('Distribution of the distance between consecutive events (one does not originate from pole)')
plt.show()

# plt.figure()
# #plt.subplot(1,2,2)
# plt.yscale('log')
# plt.hist(Np,bins=100)
# plt.ylim([1,0.6e7])
# plt.xlim([0,6000])
# plt.xlabel('Np', fontsize=18);plt.ylabel('Count', fontsize=18);plt.title('')

# Fitting the count vs np histogram
# Npmax = 5000
# Npmin = 2000
# x = np.arange(Npmin,Npmax+1)
# n, bins = np.histogram(Np,bins=Npmax-Npmin+1,range=[Npmin-0.5,Npmax+0.5])
# # A,B=np.polyfit(-x,np.log(n),1,w=np.sqrt(n))
# A,B=np.polyfit(-x,np.log(n),1)
# x = np.arange(0,Npmax+1)
# n, bins = np.histogram(Np,bins=Npmax+1,range=[-0.5,Npmax+0.5])
# plt.yscale('log')
# plt.scatter(x,n)
# plt.plot(x,A*len(Np)*np.exp(-x*A),color='red')


# forcing the detection rate in the fit of count vs np histogram
Npmax = 5000
x = np.arange(0,Npmax+1)
n, bins = np.histogram(Np,bins=Npmax+1,range=[-0.5,Npmax+0.5])
plt.yscale('log')
plt.scatter(x,n, s=1, c='black')
plt.plot(x,len(Np)*detectionrate*np.exp(-detectionrate*x), linewidth=3, c='red') # theoretical prediction
plt.xlabel('Np', fontsize=18);plt.ylabel('Count', fontsize=18);plt.title('', fontsize=18)
plt.gca().tick_params(labelsize=15)
plt.ylim([1e2,1e6])
plt.xlim([-500,4000])
plt.show()

# show zoom
Npmax = 5000
x = np.arange(0,Npmax+1)
n, bins = np.histogram(Np,bins=Npmax+1,range=[-0.5,Npmax+0.5])
plt.yscale('log')
plt.scatter(x,n, s=1, c='black')
plt.plot(x,len(Np)*detectionrate*np.exp(-detectionrate*x), linewidth=3, c='red') # theoretical prediction
plt.xlabel('Np', fontsize=18);plt.ylabel('Count', fontsize=18);plt.title('', fontsize=18)
plt.ylim([2e4,5e5])
plt.xlim([0,100])
plt.gca().tick_params(labelsize=15)
plt.show()


# average Np as a function of distance to pole location
# plt.figure()
# j = 15 # X coordinate pole
# i = 56 # Y coordinate pole

# avrad = []
# for k in range(1,10):
#     avrad.append((np.sum(resultMat[i-k:i+k+1,j-k:j+k+1])-np.sum(resultMat[i-k+1:i+k,j-k+1:j+k]))/((2*k+1)**2-(2*k-1)**2))
    
# plt.plot(avrad)
# plt.xlabel('Distance to pole');plt.ylabel('Radial average Np');
# # plt.subplot(1,3,2)
# plt.plot(resultMat[i,j:j+10:]) #x-direction
# plt.subplot(1,3,3)
# plt.plot(resultMat[i:i+10:,j]) #y-direction