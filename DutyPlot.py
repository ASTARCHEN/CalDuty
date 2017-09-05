# DutyPlot:
# All the plotting work for the project.

import numpy as np
import matplotlib.pyplot as plt
import DutyCfg

# DutyPlotFhs: Plot fhs data
# dFhr: fhs data
def plotfhr(dFhr, dError, idFig):
    lenFhr = len(dFhr)
    f = plt.figure(idFig)
    p1 = f.add_subplot(2, 1, 1)
    line1, = p1.plot(dFhr, label='fetal heart rate curve')
    p1.axis([0, lenFhr, 100, 200])
    p1.yaxis.set_ticks(np.arange(100, 201, 20))
    p1.grid(True)
    p1.legend(handles=[line1])
    p2 = f.add_subplot(2, 1, 2)
    line2, = p2.plot(dError[0], dError[1], 'r*', label='error codes')
    p2.axis([0, lenFhr, 239, 256])
    p2.yaxis.set_ticks(np.arange(240, 256, 2))
    p2.grid(True)
    p2.legend(handles=[line2])
    return


# DutyPlotFhs: Plot fhs data
# dFhs: fhs data
def plotfhs(dFhs, idFig):
    [fsFhs] = DutyCfg.loadnum(['fsFhs'])
    lenFhs = len(dFhs)
    ind = np.arange(0, lenFhs)/fsFhs
    f = plt.figure(idFig)
    plt.plot(ind, dFhs)
    plt.axis([0, lenFhs/fsFhs, -2100, 2100])
    plt.title('fetal heart signal')
    ax = f.gca()
    ax.yaxis.set_ticks(np.arange(-2000, 2048, 500))
    ax.grid(True)    
    return

# DutyPlotAcc: Plot acceleration data
# dAcc: acceleration data
def plotacc(dAcc, idFig):
    [fsAccUnit] = DutyCfg.loadnum(['fsAccUnit'])
    x = dAcc[0::3]
    y = dAcc[1::3]
    z = dAcc[2::3]
    lenX = len(x)
    ind = np.arange(0, lenX)/25
    f = plt.figure(idFig)    
    # X axis
    p1 = f.add_subplot(3, 1, 1)
    plt.title("acceleration")
    line1, =p1.plot(ind, x, label='X-axis')
    p1.axis([0, lenX/25, -1000, 1000])
    p1.yaxis.set_ticks(np.arange(-1000, 1001, 500))
    p1.grid(True)
    p1.legend(handles=[line1])
    # Y axis
    p2 = f.add_subplot(3, 1, 2)
    line2, =p2.plot(ind, y, label='Y-axis')
    p2.axis([0, lenX/25, -1000, 1000])
    p2.yaxis.set_ticks(np.arange(-1000, 1001, 500))
    p2.grid(True)
    p2.legend(handles=[line2])
    # Z axis
    p3 = f.add_subplot(3, 1, 3)
    line3, =p3.plot(ind, z, label='Z-axis')
    p3.axis([0, lenX/25, -1000, 1000])
    p3.yaxis.set_ticks(np.arange(-1000, 1001, 500))
    p3.grid(True)
    p3.legend(handles=[line3])
    return


def plot(dFhr, dFhs, dAcc, dError):
    plotfhr(dFhr, dError,1)
    plotfhs(dFhs, 2)
    plotacc(dAcc, 3)
    plt.show()
    return