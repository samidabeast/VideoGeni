import sys

def err(msg):
    print("ERROR: "+msg+".")
    sys.exit()

from math import *
from scipy import *
import scipy.misc as pil
import matplotlib.pyplot as plot

#Edit these!

RMAX = 255
RMIN = 140

GMAX = 140
GMIN = 30

BMAX = 80
BMIN = 0

def query(mx, mn):
    return (mn, mx-mn)

crange = [query(RMAX,RMIN), query(GMAX,GMIN), query(BMAX,BMIN)]

mx=0
dex = []
for x in range(3):
    c = crange[x]
    if c[1] > mx:
        dex.insert(0,x) #prepend
        mx = c[1]
    else:
        dex.append(x)

def lrange(i,whole=False):
    z = crange[dex[i]][1]
    return range(z) if whole else z

def lmin(i):
    return crange[dex[i]][0]
            
img = zeros((lrange(0),lrange(1)*lrange(2),3), dtype='uint8')

for x in lrange(0,True):
    for y in lrange(1,True):
        for z in lrange(2,True):
            
            load = [0,0,0]
            load[dex[0]] = x+lmin(0)
            load[dex[1]] = y+lmin(1)
            load[dex[2]] = z+lmin(2)

            img[x][y*lrange(2)+z] = array(load, dtype='uint8')

print(img.shape)

#Uncomment this to save an image (as yadda.jpg in current directory)
pil.imsave("yadda.jpg", img)

#Uncomment these to simply view the image (you can do both if you want)
plot.imshow(img)
plot.show()
