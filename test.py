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

inFile = sys.argv[1]
try:
    img = pil.imread(inFile)
except (FileNotFoundError):
    err("The file "+inFile+" could not be found")

print(img.shape, img.dtype)
plot.imshow(img)
plot.show()

for i in img:
    for j in i:
        if j[0]<150:
            j[0]=0
            j[1]=0
            j[2]=0

plot.imshow(img)
plot.show()

