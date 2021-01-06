import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("2-1.jpg")

mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

#Extract Rectangle - Encompasses the region specified
#(start_x,start_y,width,height)
rect = (300,300,150,150)

#Params(input_image,mask,rectangle,background,foreground,iterations,mode_used)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()
