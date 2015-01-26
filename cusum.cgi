#!/Library/Frameworks/Python.framework/Versions/3.3/bin/python3.3
from __future__ import division, print_function

import cgitb
import cgi
cgitb.enable()

print()

import numpy as np
import matplotlib.pyplot as plt
import sys
from detect_cusum import detect_cusum
form = cgi.FieldStorage()

# Get data from fields
path = form.getvalue('file')
picname = form.getvalue('pic')
print(path)
print(picname)
foct = open('/Applications/MAMP/htdocs/ntu/files/'+path, 'r')
x = []
count = 0
avg = 0
line = foct.readline()
line = foct.readline()
count = count + 1
threshold = 1000
drift = 100


while line:
    arr = line.split(',')
    if count % 24 ==0:
        avg = (avg + (float)(arr[8]))/24
        x = x+ [avg]
        avg = 0

    else:
        avg = (avg + (float)(arr[8]))
        
                                    
    line = foct.readline()
    
    count = count +1
foct.close()
ta, tai, taf, amp = detect_cusum(x,picname, threshold, drift, True, True)
print(ta)
print(tai)
print(taf)
print(amp)
print("same")