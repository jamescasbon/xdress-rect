import numpy as np

from rect.rectangle import Rectangle
from rect.dtypes import XDRectangle,xd_rectangle

# create two python proxies to C++ types
rect1 = Rectangle(1, 2, 3, 4)
rect2 = Rectangle(10, 20, 30, 40)

# using methods and attributes works fine
print 'areas', rect1.getArea(), rect2.getArea()
print rect1.x0

# put these inside an array
arr = np.array([rect1, rect2], dtype=xd_rectangle)
print 'array is', arr

# create a view on the array with a custom dtype knowing the layout of the c++ struct
my_dt = np.dtype(
    {'names': ['x0', 'y0', 'x1', 'y1'],
     'formats': ['i4', 'i4', 'i4', 'i4']
     })

# this prints the correct data, indicating the array has been populated correctly
print 'custom dtype view'
print arr.view(my_dt)


# inspect an object in the array - this comes back as a Rectangle
print arr[0]

# this segfaults
print arr[0].x0
