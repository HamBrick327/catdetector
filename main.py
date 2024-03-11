import cv2
import numpy as np

def colormask(img, upperBound, lowerBound): ## bounds need to be np arrays for opencv to be able to process them
    ## convert the bounds to hsv values
    upperBound = cv2.cvtColor([[upperBound]], cv2.COLOR_BGR2HSV) ## assumes inserted nparray is in BGR format, and converts it to HSV format for processing
   
    ## get input image, then convert it to hsv
    hsv = cv2.cvtColor(img, cv2.COL0R_BGR2HSV)

    ## make the mask to later apply to the input_image
    mask = cv2.inRange(hsv, upperBound, lowerBound) ## --> binary image to be compared to input_image


    return cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("output", colormask(image))