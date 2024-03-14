import numpy as np
import cv2

def colorMask(img):
    upperBound = np.array([42, 42, 42])
    lowerBound = np.array([0, 0, 0])

    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    return cv2.inRange(hsv, lowerBound, upperBound)


image = cv2.imread('input_image.jpg')

cv2.imshow('image', colorMask(image))

while True:
    pass