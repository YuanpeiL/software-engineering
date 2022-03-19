import pandas as pd
import sys

data = pd.read_table(sys.argv[1], encoding='gbk', header=None)
dataLen = data.shape
city= []
provence = []
nowP = ''
count = 0
for i in range(dataLen[0]):
    lastP = nowP
    nowP = data[0][i]
    if nowP != lastP:
        city.sort(key=lambda x: x[1], reverse=True)
        provence.append([lastP, count, city])
        city= []
        count = 0
    else:
        count += data[2][i]
        city.append([data[1][i], data[2][i]])
provence.sort(key=lambda x: x[1], reverse=True)
provence.pop(-1)
city= []
for i in range(len(provence)):
    city.append('\n'+provence[i][0]+'\t'+str(provence[i][1])+'\n')
    for j in range(len(provence[i][2])):
        city.append(provence[i][2][j][0]+'\t'+str(provence[i][2][j][1])+'\n')
fd = open(sys.argv[2], 'w')
fd.writelines(city)
fd.close()