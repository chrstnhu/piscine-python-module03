from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter

imp = ImageProcessor()

arr = imp.load("../resources/42AI.png")
# Output :
# Loading image of dimensions 200 x 200

# print(repr(arr))
# imp.display(arr)

from ColorFilter import ColorFilter

cf = ColorFilter()

filter = cf.invert(arr)

# filter = cf.to_green(arr)

# filter = cf.to_red(arr)

# filter = cf.to_blue(arr)

# filter = cf.to_celluloid(arr)

# filter = cf.to_grayscale(arr,'m')

# filter = cf.to_grayscale(arr, 'weight', g_weight=0.7, b_weight=0.3)

if filter is not None:
    imp.display(filter)
else:
    print("Error")