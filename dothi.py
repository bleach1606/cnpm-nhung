import csv
from matplotlib import pyplot as pl
import numpy as np
with open('dungyen.csv', 'r') as f:
    data = csv.reader(f)
    a = []
    for row in data:
        print(row)
        x = float(row[1])
        y = float(row[2])
        z = float(row[3].split(']')[0])
        # _, x, y, z = map(float, row)
        a.append(np.sqrt(x*x + y*y + z*z))
        if len(a) > 100:
            break
pl.plot(np.arange(0, len(a)), a)
pl.xlabel('milisecond (100)')
pl.ylabel('gia to')
pl.show()
# import time
# import datetime
#
# t1 = datetime.datetime.fromtimestamp(1594111986.707231)
# print(t1)