import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import datetime
import random
import time
import operator
import sys
arg = sys.argv[1]
arg2 = sys.argv[2]
f = open('../data/April Data.csv', 'r')
if arg2 == "nov" :
	f = open('../data/Nov Data.csv', 'r')
elif arg2 == "oct" :
	f = open('../data/Oct Data.csv', 'r')
line = f.readline()
line = f.readline()
vals = []
arg1 =-1
if arg == "mon":
    arg1 = 0
elif arg == "tue":
    arg1 = 1
elif arg == "wed":
    arg1 = 2
elif arg == "thur":
    arg1 = 3
elif arg == "fri":
    arg1 = 4
elif arg == "sat":
    arg1 = 5
elif arg == "sun":
    arg1 = 6
xdates = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    
input_vector = []
input_vector2 = []
output_vector = []
output_vector2 = []
yo1 = []
yo2 = []

vals = []
lc_cnt =2
while line:
    arr = line.split(',')
    if lc_cnt <= 361:
        dt =datetime.datetime.strptime(arr[2],"%m/%d/%y %H:%M")
        #timeInSec = time.mktime(dt.timetuple())
        temp = arr[10]
        holiday = int(arr[11])
        features = []
        yo1 = yo1 + [dt.toordinal()]
        features = features + [dt.weekday()]
        features = features + [dt.hour]
        features = features + [int(temp)]
        features = features + [int(holiday)]
        input_vector = input_vector + [features]
        output_vector = output_vector + [arr[8]]
    else:
        dt =datetime.datetime.strptime(arr[2],"%m/%d/%y %H:%M")
        temp = arr[10]
        holiday = int(arr[11])
        features = []
        yo2 = yo2 + [dt.toordinal()]
        features = features + [dt.weekday()]
        features = features + [dt.hour]
        features = features + [int(temp)]
        features = features + [int(holiday)]
        input_vector2 = input_vector2 + [features]
        output_vector2 = output_vector2 + [arr[8]]
    
    lc_cnt = lc_cnt +1
    line = f.readline()
    
f.close()
svr_rbf = SVR(kernel='rbf', C=500, gamma=0.1)
print(input_vector2)
y_rbf = svr_rbf.fit(input_vector, output_vector).predict(input_vector2)
i =0
j=0
imp = {}
for a in input_vector2 :
    cd =datetime.datetime.fromordinal(int(yo2[i]))
    curr_date = cd.date()
    diff = float(y_rbf[i]) - float(output_vector2[i])
    diff = diff * diff
    if curr_date in imp:
        imp[curr_date] = imp[curr_date] + diff
    else :
        imp[curr_date] = diff

    if cd.weekday() == arg1 :
        vals = vals + [y_rbf[i]]
        j = j+1
    
    if j == 24:
        j=0
        print (len(vals))
        plt.plot(xdates,vals,linestyle='-', color=np.random.rand(3,1),label=str(curr_date))
        vals = []
    
    i = i+1
    
    
sorted_x = sorted(imp.items(), key=operator.itemgetter(1))
for key in sorted_x:
    print(key)
plt.legend()
plt.show()