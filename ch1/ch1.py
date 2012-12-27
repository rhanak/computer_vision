from PIL import Image
from pylab import *

im = array(Image.open('Air_India_plane.jpg'))

imshow(im)

x = [100, 100, 400, 400]
y = [200, 500,200, 500]

plot(x,y, 'r*')

plot(x[:2],y[:2])
title("Plotting: 'A319-I-ASDD-L.jpeg'")
show()
