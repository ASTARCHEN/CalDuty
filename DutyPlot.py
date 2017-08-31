# DutyPlot:
# All the plotting work for the project.

import numpy as np
import matplotlib.pyplot as plt

# DutyPlotFhs: Decode fhs data
# dFhs: fhs data
def DutyPlotFhs(dFhs, idFig):
    lenFhs = len(dFhs)
    ind = np.arange(0, lenFhs)/500
    plt.figure(idFig)
    plt.plot(ind, dFhs)
    plt.axis([0, lenFhs/500, -2100, 2100])
    plt.title('fetal heart signal')
    return

# DutyPlotAcc: Decode acceleration data
# dAcc: acceleration data
def DutyPlotAcc(dAcc, idFig):
    x = dAcc[0::3]
    y = dAcc[1::3]
    z = dAcc[2::3]
    lenX = len(x)
    ind = np.arange(0, lenX)/25
    plt.figure(idFig)   
    p1 = plt.subplot(3, 1, 1)
    plt.title("acceleration")
    p2 = plt.subplot(3, 1, 2)
    p3 = plt.subplot(3, 1, 3)
    p1.plot(ind, x)
    p2.plot(ind, y)
    p3.plot(ind, z)
    p1.axis([0, lenX/25, -1000, 1000])
    p2.axis([0, lenX/25, -1000, 1000])
    p3.axis([0, lenX/25, -1000, 1000])
    
    return


def DutyPlotAll(dFhs, dAcc):
    DutyPlotFhs(dFhs, 1)
    DutyPlotAcc(dAcc, 2)
    plt.show()
    return