import scipy
import scipy.misc 
import matplotlib.pyplot as plot

lena = scipy.misc.lena()  #Produces stock image for testing

print ("Dimensions, type of each pixel.")
print(lena.shape, lena.dtype)

lena = lena.T #transpose the matrix of pixels

plot.imshow(lena, cmap=plot.cm.gray) #plot the image, treat as gray-scale
plot.show() #actually display the plot
