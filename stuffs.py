import sys
import scipy.misc as pil
import matplotlib.pyplot as plot

filepath = sys.argv[1]
im = pil.imread(filepath)

print(im.shape)

#determine size of each block
#should this be based on size of image?
dx = 50
dy = 50

def block(x,y): 
    """Analyze block with center at (x,y)"""
    testBox = im[x-dx:x+dx, y-dy:y+dy, :]
    plot.imshow(testBox)
    plot.show()
    #CALL GETAVERAGECOLOR ON BOX
    #return  AVERAGECOLOR


#stick the box in (would ideally like to store it in an array/arrayList then paste...ideas?)

#  Find middle of image (initial block center)
x = im.shape[0]/2
y = im.shape[1]/2
block(x,y)
