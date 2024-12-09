import fit_classes as fp 
import numpy as np

y = np.array([0.291, 0.540, 0.850, 1.008])
mistery_y = 0.670
dy = np.ones_like(y)*0.02
x = np.array([3*10**(-6), 6*10**(-6), 9*10**(-6), 12*10**(-6)])

absorbanties = fp.Data(x, y, dy)

def model(params, x):
    A = params
    return A*x
print(absorbanties.fit(model))
absorbanties.fit().show()

