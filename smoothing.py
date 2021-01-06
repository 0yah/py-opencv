from typing import cast
import cv2
import numpy as np 

cap =cv2.VideoCapture(0)

while True:
    #Get feed from webcam frame by frame
    _, frame =cap.read()
    hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #Target Red
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])

    mask = cv2.inRange(hsv,lower_red,upper_red)
    res = cv2.bitwise_and(frame,frame,mask=mask)


    #Average per block of pixels (15x15)
    kernel = np.ones((15,15),np.float32)/255
    smoothed = cv2.filter2D(res,-1,kernel)

    #Bluring 
    blur =cv2.GaussianBlur(res,(15,15),0)
    cv2.imshow("Gaussian Blurring",blur)


    cv2.imshow("Original",frame)
    cv2.imshow("Averaging",smoothed)
    #Bind to keyboard and listen for click after every millisecond
    if cv2.waitKey(1) & 0xFF == ord('q'):#Prevents binary code difference if NumLock is enabled
        
        break

cv2.destroyAllWindows()
#Release the webcam for other programs
cap.release()