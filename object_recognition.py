#This script finds identical sections in an image
import cv2
import numpy as np
 
img_rgb = cv2.imread("main-object.png")
img_gray = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)#All processing is done on the grayscale image

template = cv2.imread("template.png",0)

w,h = template.shape[::-1]#Returns the number of rows, columns and channels

res =cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

#If the object matches 80% of the template return a positive result
threshold = 0.8

loc = np.where(res>=threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2) #Draw a yellow box around matches

cv2.imshow('Detected',img_rgb)

#Wait for any key press then exit
cv2.waitKey(0)
cv2.destroyAllWindows()