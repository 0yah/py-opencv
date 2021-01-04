import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("1.jpg",cv2.IMREAD_COLOR)


#Draws A line
cv2.line(img,(5,20),(150,150),(255,255,255),5)

#Draws a rectangle
cv2.rectangle(img,(15,25),(200,200),(20,20,20),10)

#Draw a circle
cv2.circle(img,(30,80),10,(40,40,40),1)

#Draw Text
font =cv2.FONT_HERSHEY_SIMPLEX # Select Font
cv2.putText(img,"Text",(10,500),font,5,(50,50,50),5,cv2.LINE_AA)

cv2.imshow("image",img)

#Wait for any key press then exit
cv2.waitKey(0)
cv2.destroyAllWindows()