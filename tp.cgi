#!/Library/Frameworks/Python.framework/Versions/3.3/bin/python3.3


# enable debugging
import cgitb
import cgi
cgitb.enable()

print()


import matplotlib.pyplot as plt
import datetime
import random
import time
import numpy as np
import sys
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


form = cgi.FieldStorage()

# Get data from fields
path = form.getvalue('file')
picname = form.getvalue('pic')
arg = form.getvalue('day')
f = open('/Applications/MAMP/htdocs/ntu/files/'+path, 'r')

line = f.readline()
line = f.readline()
vals = []
xdates = []


flag = 0
plt.xlabel('Time')
plt.ylabel('Power Consumed (KW)')
plt.title(arg+' data analysis')
plt.legend()
st_dt = ""
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
while line:
    arr = line.split(',');
    dt =datetime.datetime.strptime(arr[2],"%m/%d/%y %H:%M")

    if dt.weekday() == arg1 and flag == 0:
        vals = vals + [arr[8]]
        flag = 1
        st_dt = dt.date()

    elif dt.weekday() == arg1 and flag == 1:
        vals = vals + [arr[8]]
    elif dt.weekday() != arg1 and flag == 1: #day stopped
        flag =0
        if len(vals) == 24:
            plt.plot(xdates,vals,linestyle='-', color=np.random.rand(3,1),label=st_dt)
            max1 =0.0
            pt1 =0
            diff =0
            pt2 =0
            pt3 =0
            for x in range(0,24):
               if x>0 :
                   prev1 = diff
                   diff = max(diff, float(vals[x])-float(vals[x-1]))
                   if prev1 != diff :
                       pt2 = x-1
                       pt3 = x
               prev = max1
               max1 = max(max1,float(vals[x]))
               if prev != max1:
                   pt1 =  x

            plt.plot([pt2,pt3],[vals[pt2],vals[pt3]],'bo')
            plt.plot([pt1],[max1],'ro')
            plt.annotate(str(int(max1)),
                         xy=(pt1, max1),
                         xycoords='data',
                         )

        vals =[]


    line = f.readline()

f.close()
print("adi lol")
#xdates = [datetime.datetime.strptime(date,"%d-%b-%y %H:%M:%S") for date in dates]
#plt.plot_date(xdates,vals,linestyle='-', color='r',)
plt.legend()
plt.xticks(np.arange(min(xdates), max(xdates)+1, 1.0))
plt.savefig("pics/"+picname+".png")
