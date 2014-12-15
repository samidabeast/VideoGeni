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

for x in scipy.nditer(img, op_flags=['readwrite']):
    x[...] = 255 - x
#img *= -1
#img += 255

scipy.misc.imsave(outFile, img)

