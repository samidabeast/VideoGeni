These are the packages I had to install to get the basic image
test to work. All were found in Synaptic for Mint, I assume Ubuntu would be the same,
since Mint is based on it.
* python3-numpy
* python3-scipy
* python3-matplotlib
* python3-pil.imagetk

[I got most of this from the tutorial here](http://scipy-lectures.github.io/advanced/image_processing/#opening-and-writing-to-image-files)

This code is available in [demo.py](demo.py). If we all can get this to work, we'll at
least have things to set-up to think about the algorithm.

The Python Imaging Library (which is included in scipy once you have downloaded
it) treats images as matrices of pixels. In Python, matrix and array operations
are only available in the numpy and scipy packages. Since scipy builds on top
of numpy, you will not normally have to explicitly import numpy.

```python
import scipy
import scipy.misc 
import matplotlib.pyplot as plot

lena = scipy.misc.lena()  #Produces stock image for testing

print ("Dimensions, type of each pixel.")
print(lena.shape, lena.dtype)

lena = lena.T #transpose the matrix of pixels

#plot.imshow(lena, cmap=plot.cm.gray) #plot the image, treat as gray-scale
plot.show() #actually display the plot
```