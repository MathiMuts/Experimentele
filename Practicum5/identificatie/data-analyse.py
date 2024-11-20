import numpy as np

file_name = 'Pb-1.txt'
file = f"identificatie/data/{file_name}"

data = np.loadtxt(file).T
N = len(data)

gem = np.sum(data)/N
s = np.sqrt(np.sum((data-gem)**2))/np.sqrt(N-1)
error = s/np.sqrt(N)

print(gem)
print(error)