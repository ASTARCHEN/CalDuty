#from __future__ import with_statement

#import configparser
#config=configparser.ConfigParser()
#cfgfile = open('./cd.conf', 'r')
#config.readfp(cfgfile)
#b1=config.get('cfg', 'b3')
#a1=config.get('cfg', 'a3')
#print(a1)
#print(b1)
import DutyCfg
[b1, b2] = DutyCfg.load(['b1', 'b2'])
#print(b1*5)
print(b1[0])
print(b2[1])