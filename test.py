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

#could probably use a boolean bitmap here

funk = scipy.vectorize(lambda r,g,b: 1 if r > 150 else 0, otypes=[scipy.uint8])

mat = funk(img[...,0], img[...,1], img[...,2])
print(mat.shape, mat.dtype)

plot.imshow(img*mat[...,scipy.newaxis])
plot.show()
