import cv2
import numpy as np
import matplotlib.pyplot as plt

# Videos and Images are processed/analysed similarly

img = cv2.imread('wallpaper.jpg', cv2.IMREAD_GRAYSCALE)

# LOOK AT OTHER OPTIONS FOR "IMREAD_" => _COLOR, _UNCHANGED

# GRAYSCALE is easier to work with/analyse

# FULLCOLOR: BGRA
#   'A' stands for alpha => opacity

cv2.imshow('image', img) # shows the image in a window titled 'image'
cv2.waitKey(0) # waits for key press?
cv2.destroyAllWindows()
 