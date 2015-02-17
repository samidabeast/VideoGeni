import sys
import scipy.misc as pil
import matplotlib.pyplot as plot

filepath = sys.argv[1]
im = pil.imread(filepath)

print(im.shape)

RMAX = 255
RMIN = 200

GMAX = 255
GMIN = 0

BMAX = 70
BMIN = 0

def query(mx, mn):
    return (mn, mx-mn)

crange = [query(RMAX,RMIN), query(GMAX,GMIN), query(BMAX,BMIN)]

#determine size of each block
#should this be based on size of image?
dx = 50
dy = 50

def block(x,y): 
    """Analyze block with center at (x,y)"""
    testBox = im[x-dx:x+dx, y-dy:y+dy, :]
    print(testBox.shape)
    return [201,60,50]

#CALL GETAVERAGECOLOR ON BOX
#    plot.imshow(testBox)
#    plot.show()

def inColorRange(c): 
    """checks if average of block is in the "fire range"""

    for i in range(3):
        if not (crange[i][0] <= c[i] <= crange[i][0]+crange[i][1]):
            return False
    return True
        

def isFire(img): 
    """Checks for fire: MAIN FUNCTION"""

#  Find middle of image (initial block center)
    x = im.shape[0]/2
    y = im.shape[1]/2

    while not inColorRange(block(x,y)):
        pass
        #change x,y to point to next block
        #have end case when we've checked whole image?

#stick the box in (would ideally like to store it in an array/arrayList then paste...ideas?)

isFire(im)
