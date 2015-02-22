import sys                      
import scipy as sp
import scipy.misc as pil
import matplotlib.pyplot as plot

filepath = sys.argv[1]
im = pil.imread(filepath)

RMAX = 255
RMIN = 140

GMAX = 140
GMIN = 30

#green*3 >= red

BMAX = 80
BMIN = 0

def query(mx, mn):
    return (mn, mx-mn)

crange = [query(RMAX,RMIN), query(GMAX,GMIN), query(BMAX,BMIN)]

#determine size of each block
#should this be based on size of image?

d = 25

def block(box): 
    """Analyze block with center at (x,y)"""
    avg = []
    for i in range(3):
        avg.append(sp.average(box[...,i])) #sp.around , decimals=0
        #right now this is truncating, might want to think about edge cases more

    return sp.array(avg, dtype='uint8') #return avg, but as an array

def inColorRange(c): 
    """checks if average of block is in the "fire range"""

    for i in range(3):
        if not (crange[i][0] <= c[i] <= crange[i][0]+crange[i][1]):
            return False
    return True

def isFire(img): 
    """Checks for fire: MAIN FUNCTION"""

#  Find middle of image (initial block center)
    xmax = im.shape[0]
    ymax = im.shape[1]
    x = xmax//2
    y = ymax//2

    fedex = sp.array([],dtype='uint8')

    c = 0 #count, how many i's are there? 
    i = 0 #iteration, which i are we on? 

    while True:
        xd = x+d
        yd = y+d

#Clipping code (needs refactoring)
        if xd > xmax:
            if x < xmax:
                xd = xmax
            else:
                return False

        if x < 0:
            if x+d > 0:
                x = 0
            else:
                return False

        if yd > ymax:
            if y < ymax:
                yd = ymax
            else:
                return False

        if y < 0:
            if y+d > 0:
                y = 0
            else:
                return False

        box = im[x:xd, y:yd, :]
        avg = block(box)
        box[:] = avg[None,None,:] #sets box to average color #sp.newaxis

        if inColorRange(avg):
            plot.imshow(box)
            plot.show()
            return True
        else:
            if i==0:
                i = c//2 + 1
                c+=1

            if c%2 == 0:
                x = x+d if c%4 == 0 else x-d

            else:
                y = y+d if c%4 == 3 else y-d
            
            i -= 1
        #change x,y to point to next block
        #have end case when we've checked whole image?

plot.imshow(im)
plot.show()

if isFire(im):
    print("fire colors were detected")
else:
    print("no fire colors were detected")

plot.imshow(im)
plot.show()

# numpy.empty_like (b)

#how to make shapes with pixelated data...
#color range needs to be fixed
#slope>1
#instead of returning True, add it to an array (index array)
#read page on numpy advanced indexing  
#paging sytem: for example 50 chunks per array




