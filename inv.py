import sys

if 1 < len(sys.argv) < 4:
    pass
else:
    print("ERROR: Invalid number of arguments.")

import scipy
import scipy.misc 
import matplotlib.pyplot as plot

inFile = sys.argv[1]
pos = inFile.index('/')+1
outFile = inFile[:pos]+'i'+inFile[pos:]
print(outFile)

img = scipy.misc.imread(inFile)

print(img.shape, img.dtype)

def contrast(x):
    y = 127 - x
    if not abs(y) > 60:
        x -= y
    return x

def strange(x):
    b = 127-x
    if b < 0:
        return -b
    else:
        return 255-b
    

fn = scipy.vectorize(strange)

scipy.misc.imsave(outFile, fn(img))

