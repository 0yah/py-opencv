import cv2
from matplotlib import pyplot as plt
import numpy as np

#Load an image then convert it to greyscale
img = cv2.imread("1.jpg",cv2.IMREAD_GRAYSCALE)

cv2.imshow("image",img)

#Wait for any key press then exit
cv2.waitKey(0)
cv2.destroyAllWindows()