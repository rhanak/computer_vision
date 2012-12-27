from PIL import Image
from pylab import *
from numpy import *

im = array(Image.open('Air_India_plane.jpg').convert('L'))

im1 = (100.0/255) * im + 100

im = 255.0 * (im/255.0) ** 2


im2 = array(Image.fromarray(im))

#print(im[1000-1500])

imshow(im1)
imshow(im2)


show()
