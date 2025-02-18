import fit_classes as fp 
import numpy as np
from pathlib import Path

y = np.array([0.291, 0.540, 0.850, 1.108])
mistery_y = 0.670
dy = np.ones_like(y)*0.02
x = np.array([3*10**(-6), 6*10**(-6), 9*10**(-6), 12*10**(-6)])

absorbanties = fp.Data(x, y, dy)

def model(params, x):
    A = params
    return A*x
# print(absorbanties.fit(model))
# absorbanties.fit().show(title="A(c) plot",x_label="c [mol/L]",y_label="A [arb.eenh.]")



data_1=np.array([0.6777,0.61495,0.55706,0.50277,0.45396,0.4072,0.36515,0.32651,0.2922,0.26294,0.23723,0.21136,0.18762,0.16799,0.14923,0.13225,0.11662,0.10335])
data_2=np.array([0.75223,0.71715,0.68048,0.6455,0.61031,0.57533,0.54337,0.51178,0.48297,0.45412,0.4277,0.40186,0.37751,0.3522,0.32759,0.30677,0.28685,0.26855,0.25045])
data_1=data_1/87000
data_2=data_2/87000
t=[]

for i in range(0,len(data_1)):
  t.append(20*i)

t2=[]
for i in range(0,len(data_2)):
  t2.append(20*i) 

T2=np.array(t2)


d1=data_1*0.02
d2=data_2*0.02
# d1=np.ones_like(data_1)*0.02
# d2=np.ones_like(data_2)*0.02
T=np.array(t)

# absorbanties2 = fp.Data(T2, (data_2), d2)
# absorbanties2.fit().show()
# print(absorbanties2.fit())

# absorbanties1 = fp.Data(T, (data_1), d1)
# absorbanties1.show()
# absorbanties1.fit(model).show()
# print(absorbanties1.fit(model))

absorbanties1log = fp.Data(T, np.log(data_1), d1/data_1)
absorbanties1log.fit().show(title="Lineariseerde A(t) plot",x_label="t[s]",y_label="ln(A) [/]")
print(absorbanties1log.fit())

absorbanties2log = fp.Data(T2, np.log(data_2), d2/data_2)
absorbanties2log.fit().show(title="Lineariseerde A(t) plot",x_label="t[s]",y_label="ln(A) [/]")
print(absorbanties2log.fit())

