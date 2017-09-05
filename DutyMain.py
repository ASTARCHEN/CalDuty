# This is a python prject, which is an attempt to acheive the functions of WallE
# Development Enviroment: Python 3.5.3, GCC 6.3.0, Linux debian9 4.9.0-3-amd64
    
import numpy as np
import matplotlib.pyplot as plt
from DutyData import *
import DutyPlot
import DutyCfg

if __name__ == '__main__':

    # Load configuration file
    [fnFhs, fnFhr] = DutyCfg.loadstr(['fnFhs', 'fnFhr'])
    # Decoding and relevant infomation
    (dFhr, dFhs, dAcc, infoDec) = DutyDataDecode(fnFhs, fnFhr)
    [fhsLost, accLost, fhsIncomplete, accIncomplete] = infoDec
    t = dFhr.size
    if(t <= 0):
        print('Nonexistent or empty files.')
        SystemExit(0)
    print('Decoding done:')
    print('  The test lasted for %ds.' %(t))
    if fhsLost > 1:
        print('  %d fhs packages lost.' %(accLost))
    elif fhsLost == 1:
        print('  1 fhs package losts.')
    else:
        print('  No fhs packages lost.') 
    if fhsIncomplete > 1:
        print('  %d incomplete fhs packages have been set to 0.' %(fhsIncomplete))
    elif fhsIncomplete == 1:
        print('  1 incomplete fhs package has been set to 0.')
    else:
        print('  All the fhs packages are complete.')    
    if accLost > 1:
        print('  %d acceleration packages lost.' %(accLost))
    elif accLost == 1:
        print('  1 acceleration package losts.')
    else:
        print('  No fhs packages lost.') 
    if accIncomplete > 1:
        print('  %d incomplete acceleration packages have been set to 0.' %(accIncomplete))
    elif accIncomplete == 1:
        print('  1 incomplete acceleration package has been set to 0.')
    else:
        print('  All the acceleration packages are complete.') 
    #Autocorrelation
    #dCorr = DutyDataCorr(dFhs)
    print('fhr len: %d; fhs len: %d; acc len: %d' %(dFhr.size, dFhs.size, dAcc.size))
    
    SystemExit(0)
    DutyPlot.plot(dFhr, dFhs, dAcc)
    
    #f = open("a.txt", "w")
    #for i in range(len(dFhs)):
        #f.write("%d\n" %(dFhs[i]))
    #f.close()

