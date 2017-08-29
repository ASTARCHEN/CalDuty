# This is a python prject, which is an attempt to acheive the functions of WallE
    
import numpy as np
import matplotlib.pyplot as plt
from DutyData import *


if __name__ == '__main__':

    dFhs = []
    dAcc = []
    fnRaw = './y00001.txt'
    (dFhs, dAcc) = DutyGetData(fnRaw)
    if(~dFhs):
        print('Nonexistent or empty file.')
        return
    end
    print('Accelation data has been seperated from fhs data.')

