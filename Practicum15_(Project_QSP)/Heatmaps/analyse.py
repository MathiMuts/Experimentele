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
# print(ON_CLU)
# print(ON_CRU)
# print(ON_CRT)
# print(ON_CLT)

# print(np.std([norm(O_CLU),norm(O_CRU),norm(O_CRT),norm(O_CLT)]))
LN_CLU=norm(L_CLU)
LN_CRU=norm(L_CRU)
LN_CRT=norm(L_CRT)
LN_CLT=norm(L_CLT)
# print(LN_CLU)
# print(LN_CRU)
# print(LN_CRT)
# print(LN_CLT)

# print(np.std([norm(L_CLU),norm(L_CRU),norm(L_CRT),norm(L_CLT)]))

L=3.5

#
def icl(th,d,L):
    return(th/np.arctan(d/L))

print(icl(0.44,ON_CLU,L))
print(icl(0.44,ON_CRU,L))
print(icl(0.44,ON_CLT,L))
print(icl(0.44,ON_CRT,L))
print(icl(0.44,LN_CLU,L))
print(icl(0.44,LN_CRU,L))
print(icl(0.44,LN_CLT,L))
print(icl(0.44,LN_CRT,L))

#uncertainty
def err_f(th,d,L):
    s_d=0.02
    s_L=0.1
    return th*np.sqrt(s_d**2*L**2+s_L**2*d**2)*1/(np.arctan(d/L)*np.sqrt(d**2+L**2))

print(err_f(0.44,ON_CLU,L))
print(err_f(0.44,ON_CRU,L))
print(err_f(0.44,ON_CLT,L))
print(err_f(0.44,ON_CRT,L))
print(err_f(0.44,LN_CLU,L))
print(err_f(0.44,LN_CRU,L))
print(err_f(0.44,LN_CLT,L))
print(err_f(0.44,LN_CRT,L))


O_RTLT=O_RT-O_LT
O_RTLU=O_RT-O_LU
O_RTRU=O_RT-O_RU
O_LURU=O_LU-O_RU
O_LULT=O_LU-O_LT
O_LTRU=O_LT-O_RU

L_RTLT=L_RT-L_LT
L_RTLU=L_RT-L_LU
L_RTRU=L_RT-L_RU
L_LURU=L_LU-L_RU
L_LULT=L_LU-L_LT
L_LTRU=L_LT-L_RU

NO_RTLT=norm(O_RTLT)
NO_RTLU=norm(O_RTLU)
NO_RTRU=norm(O_RTRU)
NO_LURU=norm(O_LURU)
NO_LULT=norm(O_LULT)
NO_LTRU=norm(O_LTRU)

NL_RTLT=norm(L_RTLT)
NL_RTLU=norm(L_RTLU)
NL_RTRU=norm(L_RTRU)
NL_LURU=norm(L_LURU)
NL_LULT=norm(L_LULT)
NL_LTRU=norm(L_LTRU)

print(icl(0.61,NO_RTLT,L))
print(icl(0.88,NO_RTLU,L))
print(icl(0.61,NO_RTRU,L))
print(icl(0.61,NO_LURU,L))
print(icl(0.61,NO_LULT,L))
print(icl(0.88,NO_LTRU,L))

print(icl(0.61,NL_RTLT,L))
print(icl(0.88,NL_RTLU,L))
print(icl(0.61,NL_RTRU,L))
print(icl(0.61,NL_LURU,L))
print(icl(0.61,NL_LULT,L))
print(icl(0.88,NL_LTRU,L))


# print(0.61/np.arctan(norm(O_RTLT)/L))
