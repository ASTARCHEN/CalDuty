# This is a python prject, which is an attempt to acheive the functions of WallE
# Development Enviroment: Python 3.5.3, GCC 6.3.0, Linux debian9 4.9.0-3-amd64
# Make sure that SCIPY, NUMPY, MATPLOTLIB and CONFIGPARSER have been installed
    
import numpy as np
import matplotlib.pyplot as plt
import DutyData
import DutyPlot
import DutyCfg

if __name__ == '__main__':

    # Load configuration file
    [fnFhs, fnFhr] = DutyCfg.loadstr(['fnFhs', 'fnFhr'])
    # Decoding
    (dFhr, dError, dFhs, dAcc, statError, infoDec) = DutyData.decode(fnFhs, fnFhr)
    [fhsLost, accLost, fhsIncomplete, accIncomplete] = infoDec
    t = dFhr.size
    if(t <= 0):
        print('Nonexistent or empty files.')
        SystemExit(0)
    print('Decoding done:')
    # Fhr info
    print('  The test lasts for %ds.' %(t))
    if(statError.size > 0):
        [ec] = DutyCfg.loadnum(['ec'])
        [ecm] = DutyCfg.loadstr(['ecm'])
        print('  Error codes num: %d' %(statError[1].sum()))
        print('      code      times      meaning')
        for i in range(statError[0].size-1):
            if(statError[1][i] > 0):
                tmpCode = statError[0][i]
                tmpTimes = statError[1][i]
                [tmpIndex] = np.argwhere(ec == tmpCode)
                tmpMeaning = ecm[tmpIndex[0]]
                print('       %d        %d       %s' %(tmpCode, tmpTimes, tmpMeaning))
        if(statError[1][statError[0].size-1] > 0):
            print('    undefined     %d      undefined' %(statError[1][statError[0].size-1]))
    else:
        print('  No error code appears')
    # Fhs info
    print('  fhs length: %d' %(dFhs.size))
    if fhsLost > 1:
        print('    %d fhs packages lost.' %(accLost))
    elif fhsLost == 1:
        print('    1 fhs package losts.')
    else:
        print('    No fhs packages lost.') 
    if fhsIncomplete > 1:
        print('    %d incomplete fhs packages have been set to 0.' %(fhsIncomplete))
    elif fhsIncomplete == 1:
        print('    1 incomplete fhs package has been set to 0.')
    else:
        print('    All the fhs packages are complete.')    
    # Acc info
    print('  acc length: %d' %(dAcc.size))
    if accLost > 1:
        print('    %d acceleration packages lost.' %(accLost))
    elif accLost == 1:
        print('    1 acceleration package losts.')
    else:
        print('    No fhs packages lost.') 
    if accIncomplete > 1:
        print('    %d incomplete acceleration packages have been set to 0.' %(accIncomplete))
    elif accIncomplete == 1:
        print('    1 incomplete acceleration package has been set to 0.')
    else:
        print('    All the acceleration packages are complete.') 
    # Autocorrelation
    freqFhs = DutyData.freq(dFhs)
    (exlEnergy, lEnergy, hEnergy) = DutyData.multiband(dFhs)
    exlCorr = DutyData.corr(exlEnergy)
    lCorr = DutyData.corr(lEnergy)
    hCorr = DutyData.corr(hEnergy)

      
    DutyPlot.plot(dFhr, dFhs, dAcc, dError, freqFhs, exlEnergy, lEnergy, hEnergy)
    SystemExit(0)
    #f = open("a.txt", "w")
    #for i in range(len(dFhs)):
        #f.write("%d\n" %(dFhs[i]))
    #f.close()
    #print(exlEnergy.size)
    #print(lEnergy.size)
    #print(hEnergy.size)

