import sys

def err(msg):
    print("ERROR: "+msg+".")
    sys.exit()

if not 1 < len(sys.argv) < 4:
    err("Invalid number of arguments")


from math import *
import scipy
import scipy.misc 
import matplotlib.pyplot as plot

inFile = sys.argv[1]
try:
    img = scipy.misc.imread(inFile)
except (FileNotFoundError):
    err("The file "+inFile+" could not be found")

pos = 0
done = False
while not done:
    try:
        pos += inFile[pos:].index('/')+1
    except (ValueError):
        done = True

print(img.shape, img.dtype)

def stretch(fn, a, b, xam):
#fn(a) must be local minimum, fn(b) local max
    rat = (b-a)/xam #ratio from int range to fn domain
    c, d = fn(a), fn(b)
    rat2 = xam/(d-c) #ratio from fn range to int range
    return lambda x: int(round((fn(x*rat+a)-c)*rat2))

def filter_factory(pre, fn):
    def filta(img):
           new_img = scipy.vectorize(fn)(img)
           outFile = inFile[:pos]+pre+inFile[pos:]
           scipy.misc.imsave(outFile, new_img)
    return filta

brighten = filter_factory("bri_", stretch(log, 0.1, 1, 255))
waves = filter_factory("wav_", stretch (cos, pi, 4*pi, 255))
crazy = filter_factory("wut_", stretch (cos, pi, 7/2*pi, 255))
contrast = filter_factory("con_", stretch(atan, -pi/2, pi/2, 255))
inverse = filter_factory("inv_", lambda x: 255-x)
tan = filter_factory("tan_", stretch(tan, -5*pi/11, 5*pi/11, 255))

sys.path.append('/home/brenan/code/Integral')
import /home/brenan/code/

terms = magic(2, 1, 1, 3)

#brighten(img)
#waves(img)
#contrast(img)
#inverse(img)
#crazy(img)
tan(img)

#seq = range(255)
###lzta = [] 
#lztb = []
#lztc = []
#for i in seq:
 #   lzta.append(contrast2(i))
  #  lztb.append(blur(i))
   # lztc.append(div(i))

#plot.plot(seq, lzta)
#plot.plot(seq, lztb)
#plot.plot(seq, lztc)
#plot.plot(seq, seq)
#plot.show()

#print(blur(190))
#print(blur(255))


#scipy.misc.imsave(outFile, 255-img)


