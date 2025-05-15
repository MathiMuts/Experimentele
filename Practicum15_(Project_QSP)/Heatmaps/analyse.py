import numpy as np
import matplotlib as plt


#oxford
O_C=np.array([-0.256,-0.04])
O_LU=np.array([-1.0843,-0.7609])
O_RU=np.array([-0.4937,-0.8051]) 
O_RT=np.array([0.5074,0.6422])
O_LT=np.array([-0.9378,0.7244])

#leoben
L_C=np.array([-0.1121,-0.0142])
L_LU=np.array([-0.9793,-0.7601])
L_RU=np.array([0.6216,-0.8489])
L_RT=np.array([0.6287,0.6773])
L_LT=np.array([-0.7923,0.7635])

#error 
err=0.02
#np.sqrt((x * dx / r)**2 + (y * dy / r)**2)

O_CLU=O_C-O_LU
O_CRU=O_C-O_RU
O_CRT=O_C-O_RT
O_CLT=O_C-O_LT

L_CLU=L_C-L_LU
L_CRU=L_C-L_RU
L_CRT=L_C-L_RT
L_CLT=L_C-L_LT

def norm(vec):
    return np.sqrt(vec[0]**2+vec[1]**2)
ON_CLU=norm(O_CLU)
ON_CRU=norm(O_CRU)
ON_CRT=norm(O_CRT)
ON_CLT=norm(O_CLT)
print(ON_CLU)
print(ON_CRU)
print(ON_CRT)
print(ON_CLT)

print(np.std([norm(O_CLU),norm(O_CRU),norm(O_CRT),norm(O_CLT)]))
LN_CLU=norm(L_CLU)
LN_CRU=norm(L_CRU)
LN_CRT=norm(L_CRT)
LN_CLT=norm(L_CLT)
print(LN_CLU)
print(LN_CRU)
print(LN_CRT)
print(LN_CLT)

print(np.std([norm(L_CLU),norm(L_CRU),norm(L_CRT),norm(L_CLT)]))

L=3.5

print(0.44/np.arctan((ON_CLU)/L))
print(0.44/np.arctan((ON_CRU)/L))
print(0.44/np.arctan((ON_CLT)/L))
print(0.44/np.arctan((ON_CRT)/L))
print(0.44/np.arctan((LN_CLU)/L))
print(0.44/np.arctan((LN_CRU)/L))
print(0.44/np.arctan((LN_CLT)/L))
print(0.44/np.arctan((LN_CRT)/L))

O_RTLT=O_RT-O_LT
print(0.61/np.arctan(norm(O_RTLT)/L))
