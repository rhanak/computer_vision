from PIL import Image
from pylab import *

im = array(Image.open('Air_India_plane.jpg'))

imshow(im)

print 'Please Click 3 points'
x = ginput(3)
print 'you have clicked:', x
show()
