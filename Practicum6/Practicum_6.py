from fit_file import X_sq
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

A=sp.Function('A')
f=sp.Function('f')
X,b,t=sp.symbols('X b t')
A=X/sp.sqrt((1-t**2)**2+2*b)
f=-sp.atan(sp.sqrt(2)*b*t/(1-t**2))
T=np.linspace(-10,10,1000)
b_lst=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
for i in range(len(b_lst)):
    A_sub=A.subs([(X,1),(b,b_lst[i])])
    B=sp.lambdify(t,A_sub,"numpy")(T)
    fig, ax = plt.subplots(1,1)
    ax.plot(T,B)