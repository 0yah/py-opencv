import cv2
import numpy as np


#Both images have the same size (800*800)
img1 = cv2.imread('2-1.jpg',cv2.IMREAD_COLOR)
img2 = cv2.imread('2-2.png',cv2.IMREAD_COLOR)


#Messy Addition of Images
add= img1+img2
#cv2.imshow("Image Addition",add)

#Using inbuilt Addition function
#Pixels colours from the first image are added to the second image the maximum sum is 255.
add = cv2.add(img1,img2)

cv2.imshow("Image Addition",add)
cv2.waitKey(0)
cv2.destroyAllWindows()
