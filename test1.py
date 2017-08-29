from DutyData import *
import numpy as np
a = np.loadtxt('./y00002.txt', dtype=np.short)
b = DutyAccerationDecode(a)
print(b)