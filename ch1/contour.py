from PIL import Image
from pylab import *

im = Image.open('Air_India_plane.jpg').convert('L')

figure()

gray()

contour(im, origin='image')
axis('equal')
axis('off')

show()
