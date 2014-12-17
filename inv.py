import sys

if 1 < len(sys.argv) < 4:
    pass
else:
    print("ERROR: Invalid number of arguments.")

from math import *
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


outFile = inFile[:pos]+'dawg_'+inFile[pos:]
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

def extreme(x):
    return 0 if x<128 else 255

def blur(x):
    x -= 127.5
    x *= .005
    x += 127.5
    return int(round(x))

def div(x): 
    return int(round(x*.25))

span = pi/2#0.5*pi #from 0 to end, also extends other way
z = atan(span)

def contrast2(x):
    x *= 2*span/255
    x -= span #have x in trig range
    return int(round((atan(x) + z)*255/(2*z))) #atan

def contrast_factory(fn, a, b, xam):
#fn must have a positive derivative at all points
    rat = (b-a)/xam #ratio from int range to fn domain
    c, d = fn(a), fn(b)
    rat2 = xam/(d-c) #ratio from fn range to int range
    def thing(x):
        x *= rat #stretch to right size
        x += a #shift to correct position
        return int(round((fn(x)-c)*rat2))
    return thing


#fn = scipy.vectorize(contrast_factory(log, 0.1, 1, 255)) #brightens
#fn = scipy.vectorize(contrast_factory(cos, pi, 4*pi, 255)) #crazy waves
#fn = scipy.vectorize(contrast_factory(atan, -pi/2, pi/2, 255)) #contrast
fn = scipy.vectorize(contrast_factory(lambda x: log(1+x%15), 0, 44, 255)) #dunno

scipy.misc.imsave(outFile, fn(img))

seq = range(255)
lzta = [] 
lztb = []
lztc = []
for i in seq:
    lzta.append(contrast2(i))
    lztb.append(blur(i))
    lztc.append(div(i))

#plot.plot(seq, lzta)
#plot.plot(seq, lztb)
#plot.plot(seq, lztc)
#plot.plot(seq, seq)
#plot.show()

#print(blur(190))
#print(blur(255))


#scipy.misc.imsave(outFile, 255-img)


