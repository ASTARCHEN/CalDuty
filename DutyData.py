# DutyData:
# All the data processing work for the project.

import numpy as np


# DutydFhsDecode: Decode fhs data
# dRaw: fhs data with coding form
# (return): fhs data with decoding form
def DutyFhsDecode(dRaw):
    lenRaw = len(dRaw)
    for i in range(lenRaw):
        dRaw[i] = dRaw[i] - 2048
    return dRaw

# DutyAccerationDecode: Decode acceration data
# dRaw: acceration data with coding form
# (return): acceration data with decoding form
def DutyAccerationDecode(dRaw):
    lenRaw = len(dRaw)
    for i in range(lenRaw):
        dRaw[i] = (dRaw[i] & 0x3FFF) - 2048
    return dRaw
    

# DutyGetData: Obtain fhs(Fetal heart signal) and acceration signal from the file of fnRaw
# fnRaw: filename
# dFhs: fhs signal, fs = 500Hz, 1 channel
# dAcc: acceration signal, fs = 25Hz, 3 channels
# cntLost: number of lost acceration packet
def DutyGetData(fnRaw):
    import os
    fExist = os.path.exists(fnRaw)
    dFhs = np.array([], dtype=np.short)
    dAcc = np.array([], dtype=np.short)    
    if(not fExist):
        return (dFhs, dAcc)
    else:
        fsAcc = 75
        fsFhs = 500
        dRaw = np.loadtxt(fnRaw, dtype=np.short)
        lenRaw = len(dRaw)
        #print(lenRaw)
        curStart = 0    # the first index of the current access data
        while curStart < lenRaw:    # find the index of the first fhs data
            if dRaw[curStart] < 10000:
                break
            curStart += 1                
        curEnd = 0      # the last index of the current access data
        cntFhs = 0      # counter for fhs data
        cntAcc = 0      # counter for acceration data
        cntLost = 0     # counter for lost acceration data
        while curStart <= lenRaw:
            if dRaw[curStart] < 10000:  # fhs data
                curEnd = curStart+fsFhs
                if curEnd >= lenRaw:    # EXCEPTION: not a complete packet
                    break
                cntFhs += 1
                tmpFhs = DutyFhsDecode(dRaw[curStart:curEnd])
                dFhs = np.hstack([dFhs, tmpFhs])
                curStart = curEnd+1
            else:                       # acceration data
                curEnd = curStart+fsAcc
                if curEnd >= lenRaw:    # EXCEPTION: not a complete packet
                    break
                cntAcc += 1
                nLost = cntFhs - cntAcc
                if nLost > 0:           # at least one acceration data packet lost 
                    dAcc = np.hstack([dAcc, np.zeros(fsAcc*nLost, dtype=np.short)])     #fill with 0
                    cntLost += nLost
                tmpAcc = DutyAccerationDecode(dRaw[curStart:curEnd])
                dAcc = np.hstack([dAcc, tmpAcc])
                cntAcc = cntFhs
                curStart = curEnd  
        nLost = cntFhs - cntAcc     # duration of fhs data and that of acceration data should be the same 
        if nLost > 0:               # at least one acceration data packet lost 
            dAcc = np.hstack([dAcc, np.zeros(fsAcc*nLost, dtype=np.short)])
            cntLost += nLost
    return (dFhs, dAcc, cntLost)