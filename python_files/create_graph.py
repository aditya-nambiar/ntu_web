import matplotlib.pyplot as plt
import matplotlib
import datetime
import random
import time

f = open('../data/April Data.csv', 'r')
line = f.readline()
line = f.readline()

## If the file is not empty keep reading line one at a time
## till the file is empty
dates = []
vals = []
while line:
    arr = line.split(',');
    dates = dates +[arr[2]]
    vals = vals + [arr[8]]
    line = f.readline()
    
f.close()
plt.xlabel('Time')
plt.ylabel('Power Consumed')
plt.title('Graph')
plt.legend()

xdates = [datetime.datetime.strptime(date,"%d-%b-%y %H:%M:%S") for date in dates]
plt.plot_date(xdates,vals,linestyle='-', color='r',)
plt.show()
#xdates = [time.strptime(date,'%d-%b-%y %T') for date in dates]
#struct_time = time.strptime(dates[1], "%d-%b-%y %T")
#struct_time = time.strptime("04-Nov-14 06:59:59", "%d-%b-%y %H:%M:%S")

#print(xdates)
#print(vals)