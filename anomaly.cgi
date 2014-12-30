#!/Library/Frameworks/Python.framework/Versions/3.3/bin/python3.3


# enable debugging
import cgitb
import cgi
cgitb.enable()

print()
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import datetime
import random
import time
import operator
import sys
form = cgi.FieldStorage()

all_files_train = form.getlist('train')
all_files_test = form.getlist('test')
num_err = 3
vals = []
arg1 =-1
arg = "mon"
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
for i in all_files_train:
    f = open('training/'+i,'U')
    line = f.readline()
    line = f.readline()
    while line:
        arr = line.split(',')
        if 0 == 0:
            dt =datetime.datetime.strptime(arr[2],"%m/%d/%y %H:%M")
            #timeInSec = time.mktime(dt.timetuple())
            temp = arr[10]
            holiday = int(arr[11])
            features = []
            features = features + [dt.weekday()]
            features = features + [dt.hour]
            features = features + [int(temp)]
            features = features + [int(holiday)]
            input_vector = input_vector + [features]
            output_vector = output_vector + [arr[8]]

        line = f.readline()

    f.close()
for i in all_files_test:
    f = open('testing/'+i,'U')
    line = f.readline()
    line = f.readline()
    while line:
        arr = line.split(',')
        if 0 == 0:
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
            input_vector2 = input_vector2 + [features]
            output_vector2 = output_vector2 + [arr[8]]

        line = f.readline()

    f.close()

svr_rbf = SVR(kernel='rbf', C=200, gamma=0.1)
y_rbf = svr_rbf.fit(input_vector, output_vector).predict(input_vector2)

i =0
j=0
imp = {}
for a in input_vector2 :
    cd =datetime.datetime.fromordinal(int(yo1[i]))
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
        #plt.plot(xdates,vals,linestyle='-', color=np.random.rand(3,1),label=str(curr_date))
        vals = []

    i = i+1

errors = set()
sorted_x = sorted(imp.items(), key=operator.itemgetter(1),reverse=True)
k =0
for key in sorted_x:
    if k == num_err :
        break
    k = k+1
    errors.add(key[0])
    print(key)

j=0
i=0


for a in output_vector2 :
    cd =datetime.datetime.fromordinal(int(yo1[i]))
    curr_date = cd.date()
    if curr_date in errors :
        vals = vals + [output_vector2[i]]
        j = j+1

    if j == 24:
        j=0
        plt.plot(xdates,vals,linestyle='-', color=np.random.rand(3,1),label=str(curr_date))
        vals = []

    i = i+1
plt.legend()
plt.xticks(np.arange(min(xdates), max(xdates)+1, 1.0))
plt.savefig("pics/anom.png")
