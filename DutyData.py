# DutyData:
# All the data processing work for the project.

import numpy as np


# DutydFhsDecode: Decode fhs data
# dRaw: fhs data with coding form
# (return): fhs data with decoding form
def DutyDataFhsDecode(dRaw):
    lenRaw = len(dRaw)
    for i in range(lenRaw):
        dRaw[i] = dRaw[i] - 2048
    return dRaw

# DutyAccerationDecode: Decode acceleration data
# dRaw: acceleration data with coding form
# (return): acceleration data with decoding form
def DutyDataAccelerationDecode(dRaw):
    lenRaw = len(dRaw)
    for i in range(lenRaw):
        dRaw[i] = (dRaw[i] & 0x3FFF) - 2048
    return dRaw
    

# DutyGetData: Obtain fhs(Fetal heart signal) and acceleration signal from the file of fnRaw
# fnRaw: filename
# dFhs: fhs signal, fs = 500Hz, 1 channel
# dAcc: acceleration signal, fs = 25Hz, 3 channels
# cntLost: number of lost acceleration packet
def DutyDataDecode(fnRaw):
    import os
    fExist = os.path.exists(fnRaw)
    dFhs = np.array([], dtype=np.short)
    dAcc = np.array([], dtype=np.short)    
    if(not fExist):
        return (dFhs, dAcc)
    # The file exists, so decoding starts now.
    fsAcc = 75
    fsFhs = 500
    dRaw = np.loadtxt(fnRaw, dtype=np.short)
    lenRaw = len(dRaw)
    # The first packet is a fhs packet or an acceleration packet, which is almost impossible to be complete.
    # So, the first complete fhs packet should be identified before decoding. 
    curStart = 0    # the first index of the current access data
    if dRaw[0] < 10000:  #
        tmpInd = 1
        while dRaw[tmpInd] < 10000:
            tmpInd += 1
        #tmpInd -= 1
        if tmpInd >= 500:
            while tmpInd >= 500:
                tmpInd -= 500
            curStart = tmpInd
        else:
            curStart = tmpInd + 75
    else:
        tmpInd = 1
        while dRaw[tmpInd] > 10000:
            tmpInd += 1
        curStart = tmpInd
    # curStart has been set to point the first complete fhs packet.
    #while curStart < lenRaw:    # find the index of the first fhs data
     #   if dRaw[curStart] < 10000:
      #      break
      #  curStart += 1                
    curEnd = 0      # the last index of the current access data
    cntFhs = 0      # counter for fhs packets
    cntAcc = 0      # counter for acceration packets
    cntLost = 0     # counter for lost acceleration packets
    while curStart <= lenRaw:
        if dRaw[curStart] < 10000:  # fhs data
            curEnd = curStart+fsFhs
            if curEnd >= lenRaw:    # EXCEPTION: not a complete packet
                break
            cntFhs += 1
            tmpFhs = DutyDataFhsDecode(dRaw[curStart:curEnd])
            dFhs = np.hstack([dFhs, tmpFhs])
            curStart = curEnd
        else:                       # acceleration data
            curEnd = curStart+fsAcc
            if curEnd >= lenRaw:    # EXCEPTION: not a complete packet
                break
            cntAcc += 1
            nLost = cntFhs - cntAcc
            if nLost > 0:           # at least one acceleration data packet lost 
                dAcc = np.hstack([dAcc, np.zeros(fsAcc*nLost, dtype=np.short)])     #fill with 0
                cntLost += nLost
            tmpAcc = DutyDataAccelerationDecode(dRaw[curStart:curEnd])
            dAcc = np.hstack([dAcc, tmpAcc])
            cntAcc = cntFhs
            curStart = curEnd  
    nLost = cntFhs - cntAcc     # duration of fhs data and that of acceleration data should be the same 
    if nLost > 0:               # at least one acceleration data packet lost 
        dAcc = np.hstack([dAcc, np.zeros(fsAcc*nLost, dtype=np.short)])
        cntLost += nLost
    return (dFhs, dAcc, cntLost)