import numpy as np
import time

while True:
    file = "data/penetration/Al-9.txt"
    data = np.loadtxt(file).T
    N = len(data)

    gem = np.sum(data)/N
    s = np.sqrt(np.sum((data-gem)**2))/np.sqrt(N-1)
    error = s/np.sqrt(N)

    print(data)
    print(gem, error)
    print(error/gem)
    time.sleep(1)
