#!/Library/Frameworks/Python.framework/Versions/3.3/bin/python3.3


# enable debugging
import cgitb
cgitb.enable()

print("Content-Type: text/plain;charset=utf-8")
print()

def lol():
    print("Hi")

lol()
print("Hello World!")

import matplotlib.pyplot as plt, mpld3
plt.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
mpld3.show()