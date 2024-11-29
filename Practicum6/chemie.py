from fit_file import X_sq
import numpy as np
import matplotlib.pyplot as plt

t=np.array([273,298,318])
c=np.array([7.87e3,3.46e5,4.98e6])
t_err=np.array([0,0,0])
c_err=np.array([0.1,0.1,0.1])
c2=np.log(c)
initial_guess=[-0.0001,1]
def model(params,x):
        a,b=params
        return a/x+b
data=((t,t_err),(c2,c_err))
param_names=['a','b']
X_sq(data, param_names, initial_guess, model,
         root_attempts=None, datafile=None,
         VERBOSE=False, LaTeX=True,
         PLOT=True, graf1_title='Fit en data amplitude', graf1_x_label=r'$\omega$ [Hz]', graf1_y_label='A [mm]'
        )
