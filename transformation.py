import cv2
import numpy as np
from numpy.lib.twodim_base import mask_indices

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([30, 150, 50])
    upper_red = np.array([255, 255, 180])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mgradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
    top_hat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
    black_hat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)

    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Erosion', erosion)

    cv2.imshow('Dilation', dilation)#Opposite of erosion
    cv2.imshow('Opening', opening)#Erosion > Dilation

    cv2.imshow('Closing', closing)#Dilation > Erosion
    cv2.imshow('Morphological Gradient', mgradient)# Dilation - Erosion
    cv2.imshow('Top Hat', top_hat)#Source image - Opening 
    cv2.imshow('Black Hat', black_hat)#Source Image - Closing

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
cap.release()
