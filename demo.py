import scipy
import scipy.misc 
import matplotlib.pyplot as plot

lena = scipy.misc.lena()

print ("Dimensions, type of each pixel.")
print(lena.shape, lena.dtype)

lena = lena.T #transpose

plot.imshow(lena, cmap=plot.cm.gray) #whats cmap?
plot.show()


