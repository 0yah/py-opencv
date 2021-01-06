from typing import cast
import cv2
import numpy as np 

cap =cv2.VideoCapture(0)
"""
Filter based on a specific colour

Convert image to a Hue Saturation Value 

This script will only display the targeted colour

Use trial and error till the desired colour is found
"""
while True:
    #Get feed from webcam frame by frame
    _, frame =cap.read()
    hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #Target Red
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])

    mask = cv2.inRange(hsv,lower_red,upper_red)
    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)
    cv2.imshow("Res",res)

    #Bind to keyboard and listen for click after every millisecond
    if cv2.waitKey(1) & 0xFF == ord('q'):#Prevents binary code difference if NumLock is enabled
        
        break

cv2.destroyAllWindows()
#Release the webcam for other programs
cap.release()