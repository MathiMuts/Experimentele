from fit_file import X_sq
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

A=sp.Function('A')
f=sp.Function('f')
X,b,t=sp.symbols('X b t')
A=X/sp.sqrt((1-t**2)**2+2*b)
f=-sp.atan(sp.sqrt(2)*b*(t/1-t**2))
T=np.linspace(-10,10,1000)
B=sp.lambdify(t,A,"numpy")(T)
F=sp.lambdify(t,f,"numpy")(T)
