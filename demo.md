These are the packages I had to install to get the basic image
test to work. All were found in Synaptic for Mint, I assume Ubuntu would be the same,
since Mint is based on it.
* python3-numpy
* python3-scipy
* python3-matplotlib
* python3-pil.imagetk

[I got most of this from the tutorial here](http://scipy-lectures.github.io/advanced/image_processing/#opening-and-writing-to-image-files)

This code is available in demo.py
```python
import scipy
import scipy.misc 
import matplotlib.pyplot as plot

lena = scipy.misc.lena()

print ("Dimensions, type of each pixel.")
print(lena.shape, lena.dtype)

lena = lena.T #transpose

plot.imshow(lena, cmap=plot.cm.gray) #whats cmap?
plot.show()
```