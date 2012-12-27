from PIL import Image
from numpy import *
from pylab import *

import imtools 

im = array(Image.open('AquaTermi_lowcontrast.jpg').convert('L'))
im2,cdf = imtools.histeq(im)

imshow(im2)
gray()
show()
