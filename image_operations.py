import cv2
import numpy as np


img =cv2.imread("1.jpg",cv2.IMREAD_COLOR)

#Reference a pixel from the loaded image
px = img[250:550,330:630]



#Change pixel colour for the range specified
img[250:550,330:630] = [255,255,255]

print(img.shape)
print(img.size)
print(img.dtype)

watch_face = px
img[0:300,0:300] = watch_face

cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
