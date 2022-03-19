import numpy as np

with open("yq_in.txt", 'r') as fd:
    data = fd.readlines()
data = np.array(data)
dataout = []
now = ''
for i in data:
    last = now
    now = i[0:3] #省份
    if now == last:
        dataout.append(i[4:])
        print(i[4:])

    else:
        dataout.append('\n' + i[0:3] + '\n')
        dataout.append(i[4:])
with open('yq_out.txt', 'w') as fd:
    fd.writelines(dataout)
