import cv2
import numpy as np
from time import time, sleep
from os import getcwd

''' GET WEBCAM IMAGE CODE BLOCK (not in use right now because I'm just using the test images)
cam = cv2.VideoCapture(0)
_, image = camera.read() <-- _, is important because othewise the tuple 
'''
image = cv2.imread('testImageCat.jpg')
size = image.shape[:2] ## practicing python slicing, takes everything from the beginning to the second element, exclusive
cat = image[0:int((size[0]*.45)), 0:size[-1]] ## not it hypothetically get the top 45% of the image and stores that as 'cat'
print(size)
cv2.waitKey()
### youtube tutorial and (some) code from https://github.com/techwithtim/OpenCV-Tutorials/blob/main/tutorial5.py ###

## grayscale now because the final deployment will be running on a device with 512megs of ram and the less numbers the better
upperBound = 38
lowerBound = 0

## get input image, then convert it to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray", gray)

## generate a binary image to be compared to the grayscale image
mask = cv2.inRange(gray, lowerBound, upperBound)

## TODO crop the image and find out if A) cat is present and B) is there food in the bowl (but not yet because I don't have an image for that)

### end techwithtim adapted code ###
'''
- and then from here we need to delete the taken image
- store the time cat was last seen
- send push notifications?
'''

## records the last time the cat was seen (but not really, there needs to be more logic)
lastSeen = time()
# cv2.waitKey() ## imshow only works with waitkey() KEEP THIS WHEN SHOWING AN IMAGE!!!!!!!!!!1 ############
