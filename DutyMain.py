# This is a python prject, which is an attempt to acheive the functions of WallE
# Development Enviroment: Python 3.5.3, GCC 6.3.0, Linux debian9 4.9.0-3-amd64
    
import numpy as np
import matplotlib.pyplot as plt
from DutyData import *
from DutyPlot import *

if __name__ == '__main__':

    fnRaw = './y00004.txt'
    # Decoding and relevant infomation
    (dFhs, dAcc, accLost, fhsIncomplete, accIncomplete) = DutyDataDecode(fnRaw)
    t = len(dFhs)/500
    if(t <= 0):
        print('Nonexistent or empty file.')
        SystemExit(0)
    print('Decoding done:')
    print('  The test lasted for %ds.' %(t))
    if fhsIncomplete > 1:
        print('  %d fhs packets have been autocompleted.' %(fhsIncomplete))
    elif fhsIncomplete == 1:
        print('  A fhs packet has been autocompleted.')
    else:
        print('  All the fhs packets are complete.')    
    if accLost > 1:
        print('  %d acceleration packets lost.' %(accLost))
    elif accLost == 1:
        print('  An acceleration packet losts.')
    else:
        print('  No fhs packets lost.') 
    if accIncomplete > 1:
        print('  %d acceleration packets have been autocompleted.' %(accIncomplete))
    elif accIncomplete == 1:
        print('  An acceleration packet has been autocompleted.')
    else:
        print('  All the acceleration packets are complete.') 
    #Autocorrelation
    dCorr = DutyDataCorr(dFhs)
    
    
    
    #DutyPlotAll(dFhs, dAcc)
    
    #f = open("a.txt", "w")
    #for i in range(len(dFhs)):
        #f.write("%d\n" %(dFhs[i]))
    #f.close()

