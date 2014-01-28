import numpy as np

from rect.rectangle import Rectangle
from rect.dtypes import XDRectangle,xd_rectangle

rect1 = Rectangle(1, 2, 3, 4)
rect2 = Rectangle(10, 20, 30, 40)
print 'areas', rect1.getArea(), rect2.getArea()
print rect1.x0

arr = np.array([rect1, rect2], dtype=xd_rectangle)
print 'array is', arr

my_dt = np.dtype(
    {'names': ['x0', 'y0', 'x1', 'y1'],
     'formats': ['i4', 'i4', 'i4', 'i4']
     })
print 'custom dtype view'
print arr.view(my_dt)


print arr[0]
print arr[0].x0
