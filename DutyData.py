# DutyGetData: Obtain fhs(Fetal heart signal) and acceration signal from the file of fnRaw
# fnRaw: filename
# dFhs: fhs signal, fs = 500Hz, 1 channel
# dAcc: acceration signal, fs = 25Hz, 3 channels
import numpy as np

def DutyGetData(fnRaw):
    
    import os
    fExist = os.path.exists(fnRaw)
    if(not fExist):
        dFhs = []
        dAcc = []
        return (dFhs, dAcc)
    else:
        dRaw = np.loadtxt(fnRaw)
        
        
    