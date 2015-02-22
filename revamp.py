import sys                      
import scipy as sp
import scipy.misc as pil
import matplotlib.pyplot as plot

sp.set_printoptions(threshold=sp.nan)

RMAX = 255
RMIN = 140

GMAX = 140
GMIN = 30

#green*3 >= red

BMAX = 80
BMIN = 0

s = 3 #size of side of grid unit
step = 2*s + 1

crange = [[RMIN, RMAX], [GMIN, GMAX], [BMIN, BMAX]]

def scalarColorRange(r,g,b): 
    return RMIN <= r <= RMAX and GMIN <= g <= GMAX and BMIN <= b <= BMAX 

inColorRange = sp.vectorize(scalarColorRange, otypes=[sp.bool_,])

def cull(v):
    x = 0 if v else 255
    return x,x,x

def fire(pic):
    grid = pic[s:pic.shape[0]:step, s:pic.shape[1]:step] #test points

    bool_mask =  inColorRange(*sp.split(grid, 3, axis=2))

    pfunc = sp.vectorize(cull, otypes=[sp.uint8,sp.uint8,sp.uint8])

    grid[:] = sp.dstack(pfunc(bool_mask))

    plot.imshow(pic)
    plot.show()

    return True

print(fire(pil.imread(sys.argv[1])))


#    plot.imshow(pic)
#   plot.show()
