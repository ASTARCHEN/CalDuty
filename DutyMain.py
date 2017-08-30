# This is a python prject, which is an attempt to acheive the functions of WallE
    
import numpy as np
import matplotlib.pyplot as plt
from DutyData import *


if __name__ == '__main__':

    fnRaw = './y00004.txt'
    (dFhs, dAcc, nLost) = DutyGetData(fnRaw)
    t = len(dFhs)/500
    if(t <= 0):
        print('Nonexistent or empty file.')
        SystemExit(0)
    print('Accelation data has been seperated from fhs data.')
    print('The test lasted %ds' %(t))
    print('%d accelation data packets lost' %(nLost))

