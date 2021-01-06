"""

Converts everything to white or black, based on a value.
Anything that is less than the threshold value is converted to 0(black) while everything above the value is converted to 255(white)

"""
import cv2
import numpy as np 

img = cv2.imread("bookpage.jpg")

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
threshold = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

cv2.imshow("Original",img)
cv2.imshow("Threshold",threshold)
cv2.waitKey()
cv2.destroyAllWindows()