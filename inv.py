import sys

if 1 < len(sys.argv) < 4:
    pass
else:
    print("ERROR: Invalid number of arguments.")

import scipy
import scipy.misc 
import matplotlib.pyplot as plot

inFile = sys.argv[1]
done = False
pos = 0

while not done:
    try:
        pos += inFile[pos:].index('/')+1
    except (ValueError):
        done = True


outFile = inFile[:pos]+'b'+inFile[pos:]
print(outFile)

img = scipy.misc.imread(inFile)

print(img.shape, img.dtype)

def contrast(x):
    y =  x - 127
    if abs(y) < 60:
        x += y
    return x

def strange(x):
    b = x-127
    if b > 0:
        return b
    else:
        return 255+b

# fn = scipy.vectorize(strange)

# scipy.misc.imsave(outFile, fn(img))

scipy.misc.imsave(outFile, 255-img)


