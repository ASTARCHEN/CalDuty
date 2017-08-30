# DutyPlot:
# All the plotting work for the project.

import numpy as np
import matplotlib.pyplot as plt

# DutyPlotFhs: Decode fhs data
# dFhs: fhs data
def DutyPlotFhs(dFhs):
    lenFhs = len(dFhs)
    ind = np.arange(0, lenFhs)
    plt.figure()
    plt.plot(ind, dFhs)
    plt.show()
    return