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

#for x in scipy.nditer(img, flags=['external_loop'], op_flags=['readwrite']):
 
#   print (x.size)

if r>g>b:
    return[r,g,b]
else:
    return[0,0,0]

img2 = img
plot.imshow(img)
plot.show()


plot.imshow(img2*scipy.array([1,1,0],dtype=img2.dtype))
plot.show()


