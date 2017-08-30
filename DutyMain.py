# This is a python prject, which is an attempt to acheive the functions of WallE
# Development Enviroment: Python 3.5.3, GCC 6.3.0, Linux debian9 4.9.0-3-amd64
    
import numpy as np
import matplotlib.pyplot as plt
from DutyData import *
from DutyPlot import *

if __name__ == '__main__':

    fnRaw = './y00004.txt'
    (dFhs, dAcc, nLost) = DutyDataDecode(fnRaw)
    t = len(dFhs)/500
    if(t <= 0):
        print('Nonexistent or empty file.')
        SystemExit(0)
    print('Acceleration data has been seperated from fhs data.')
    print('The test was %ds in length' %(t))
    print('%d acceleration packets lost' %(nLost))
    DutyPlotFhs(dFhs)
    #DutyPlotFhs(dAcc)

