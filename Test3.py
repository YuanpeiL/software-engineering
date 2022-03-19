import numpy as np
import pandas as pd
import sys


data = pd.read_csv("yq_in.txt", encoding='gbk', header=0)
data = np.array(data)
lastLabel = ''
nowLabel = ''
outData = []
lenArgv = len(sys.argv)
if lenArgv==3:
    for i in data:
        lastLabel = nowLabel
        nowLabel = i[0][0:3]
        if nowLabel != lastLabel:
            outData.append('\n'+nowLabel+'\n')
        outData.append(i[0][4:]+'\n')
elif lenArgv==4:
    outData.append('\n' + sys.argv[3] + '\n')
    for i in data:
        nowLabel = i[0][0:3]
        if nowLabel==sys.argv[3]:
            outData.append(i[0][4:]+'\n')
fd = open(sys.argv[2], 'w')
fd.writelines(outData)
fd.close()