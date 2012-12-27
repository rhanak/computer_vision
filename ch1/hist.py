from PIL import Image
from pylab import *

im = array(Image.open('Air_India_plane.jpg'))

imshow(im)

figure()

hist(im.flatten(), 128)

show()
