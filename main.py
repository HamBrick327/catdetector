import cv2
import numpy as np
from time import time, sleep

'''before this happens we need to get image from webcam'''
image = cv2.imread('./input_image.jpg')

## youtube tutorial and (some) code from https://github.com/techwithtim/OpenCV-Tutorials/blob/main/tutorial5.py

## grayscale now because the final deployment will be running on a device with 512megs of ram and the less numbers the better
upperBound = 38
lowerBound = 0

## get input image, then convert it to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray", gray)

## generate a binary image to be compared to the grayscale image
mask = cv2.inRange(gray, lowerBound, upperBound)

## TODO crop the image and find out if A) cat is present and B) is there food in the bowl (but not yet because I don't have an image for that)

'''
and then from here we need to delete the taken image
- store the time cat was last seen
- send push notifications?
'''