# DutyPlot:
# All the plotting work for the project.

import numpy as np
import matplotlib.pyplot as plt
import DutyCfg

# plotfhr: Plot fhs data
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


# plotfhs: Plot fhs data
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

# plotacc: Plot acceleration data
# dAcc: acceleration data
def plotacc(dAcc, idFig):
    [fsAccUnit] = DutyCfg.loadnum(['fsAccUnit'])
    x = dAcc[0::3]
    y = dAcc[1::3]
    z = dAcc[2::3]
    lenX = len(x)
    ind = np.arange(0, lenX)/fsAccUnit
    f = plt.figure(idFig)    
    # X axis
    p1 = f.add_subplot(3, 1, 1)
    plt.title("acceleration")
    line1, =p1.plot(ind, x, label='X-axis')
    p1.axis([0, lenX/fsAccUnit, -1000, 1000])
    p1.yaxis.set_ticks(np.arange(-1000, 1001, 500))
    p1.grid(True)
    p1.legend(handles=[line1])
    # Y axis
    p2 = f.add_subplot(3, 1, 2)
    line2, =p2.plot(ind, y, label='Y-axis')
    p2.axis([0, lenX/fsAccUnit, -1000, 1000])
    p2.yaxis.set_ticks(np.arange(-1000, 1001, 500))
    p2.grid(True)
    p2.legend(handles=[line2])
    # Z axis
    p3 = f.add_subplot(3, 1, 3)
    line3, =p3.plot(ind, z, label='Z-axis')
    p3.axis([0, lenX/fsAccUnit, -1000, 1000])
    p3.yaxis.set_ticks(np.arange(-1000, 1001, 500))
    p3.grid(True)
    p3.legend(handles=[line3])
    return

# plotfreq: plot frequency spretrum
# dFreq: frequency spretrum
#def plotfreq(dFreq, idFig):
    #nFig = len(dFreq)
    #for i in range(nFig):
        #f = plt.figure(idFig+i)
        #plt.plot(dFreq[i])
        #ax = f.gca()
        #ax.grid(True)     
    #return
def plotfreq(dFreq, idFig):
    f = plt.figure(idFig)
    tmpFreq = np.mean(dFreq, 0)
    plt.plot(tmpFreq)
    plt.axis([-1, len(tmpFreq), 0, max(tmpFreq)*1.1])
    ax = f.gca()
    ax.grid(True)     
    return

# plotfreq: plot energy signals
# exlEnergy, lEnergy, hEnergy: energy signals
def plotenergy(exlEnergy, lEnergy, hEnergy, idFig):
    [fsFhs] = DutyCfg.loadnum(['fsFhs'])
    lenEnergy = len(exlEnergy)
    fsEnergy = fsFhs/2
    ind = np.arange(0, lenEnergy)/fsEnergy
    f = plt.figure(idFig)    
    # extreme low frequency band
    p1 = f.add_subplot(3, 1, 1)
    plt.title("energy")
    line1, =p1.plot(ind, exlEnergy, label='extreme low frequency band')
    p1.axis([0, lenEnergy/fsEnergy, -100, max(exlEnergy)])
    p1.grid(True)
    p1.legend(handles=[line1])
    # low frequency band
    p2 = f.add_subplot(3, 1, 2)
    line2, =p2.plot(ind, lEnergy, label='low frequency band')
    p2.axis([0, lenEnergy/fsEnergy, -100, max(lEnergy)])
    p2.grid(True)
    p2.legend(handles=[line2])
    # high frequency band
    p3 = f.add_subplot(3, 1, 3)
    line3, =p3.plot(ind, hEnergy, label='high frequency band')
    p3.axis([0, lenEnergy/fsFhs, -100, max(hEnergy)])
    p3.grid(True)
    p3.legend(handles=[line3])    
    return

def plotcorr(lCorr, idFig):
    f = plt.figure(idFig) 
    plt.pcolor(lCorr.transpose(), shading='flat')

def plot(dFhr, dFhs, dAcc, dError, dFreq, exlEnergy, lEnergy, hEnergy, lCorr):
    plotfhr(dFhr, dError,1)
    #plotfhs(dFhs, 2)
    #plotacc(dAcc, 3)
    #plotfreq(dFreq, 4)
    #plotenergy(exlEnergy, lEnergy, hEnergy, 5)
    plotcorr(lCorr, 6)
    plt.show()
    return