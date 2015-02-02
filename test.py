import sys

def err(msg):
    print("ERROR: "+msg+".")
    sys.exit()

if len(sys.argv) != 2:
    err("Invalid number of arguments")

from math import *
import scipy
import scipy.misc as pil
import matplotlib.pyplot as plot

def outName(orig, pre):
    """Creates an output name, by adding a prefix onto the original
    input name. Works for names outside of current directory"""
    pos = 0
    while True:
        try:
            pos += orig[pos:].index('/')+1
        except (ValueError):
            break
    return orig[:pos]+pre+orig[pos:]

inFile = sys.argv[1]
try:
    img = pil.imread(inFile)
except (FileNotFoundError):
    err("The file "+inFile+" could not be found")

print(img.shape, img.dtype)
"""
m = scipy.array_split(img,3)

def fn(r,g,b):
    if r>g>b:
        return scipy.array([r,g,b], dtype=img.dtype)
    else:
        return scipy.array([0,0,0], dtype=img.dtype)
 
plot.imshow(img)
plot.show()
fnct = scipy.vectorize(fn)
img = fnct(m[0],m[1],m[2])
"""
plot.imshow(img)
plot.show()

for i in img:
    for j in i:
#        if not (j[0]>j[1]>j[2]):
        if j[0]<150:# and 
            j[0]=0
            j[1]=0
            j[2]=0

plot.imshow(img)
plot.show()

