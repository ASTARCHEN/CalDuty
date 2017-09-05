# DutyCfg:
# Load configure file.

import configparser
import string
import numpy as np

# loadnum: Load numerical parameters
# inStr: names of parameters
# (return): values of parameters
def loadnum(inStr):
    lenStr = len(inStr)
    if(lenStr <= 0):
        return([])
    outPara = [];
    cf=configparser.ConfigParser()
    fid = open('./cd.conf', 'r')
    cf.readfp(fid)
    for i in range(lenStr):
        tmp = cf.get('num', inStr[i])
        tmp2 = tmp.split(',')
        len2 = len(tmp2)
        if(len2 > 1):
           tmp2a = tmp2[0]
           tmp2b = tmp2a.split('.')
           len2a = len(tmp2a)
           len2b = len(tmp2b)
           if(len2a == len2b):  #type is intger
               fTmp = np.zeros(len2, dtype = np.int)
               for j in range(len2):
                   fTmp[j] = int(tmp2[j])
           else:               #type is float
               fTmp = np.zeros(len2, dtype = np.float)    
               for j in range(len2):
                   fTmp[j] = float(tmp2[j])
        elif(len2 == 1):
            tmp3 = tmp.split('.')
            len3 = len(tmp3)
            if(len3 > 1):
                fTmp = float(tmp2[0])
            else:
                fTmp = int(tmp2[0])
        else:
            fTmp = []
        outPara.append(fTmp)
    return outPara


# loadstr: Load character parameters
# inStr: names of parameters
# (return): values of parameters    
def loadstr(inStr):
    lenStr = len(inStr)
    if(lenStr <= 0):
        return([])
    outPara = [];
    cf=configparser.ConfigParser()
    fid = open('./cd.conf', 'r')
    cf.readfp(fid)    
    for i in range(lenStr):
        tmp = cf.get('str', inStr[i])
        outPara.append(tmp)
    return(outPara)