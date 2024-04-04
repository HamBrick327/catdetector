import cv2
import numpy as np
from time import time, sleep, strftime
from os import getcwd

''' GET WEBCAM IMAGE CODE BLOCK (not in use right now because I'm just using the test images)
cam = cv2.VideoCapture(0)
_, image = camera.read() <-- _, is important because othewise the tuple isn't an image and freaks out
'''
delayTime = 15

## use this in final deployment to get the image from the webcam connected to the raspi
def capImage(cam: int = 0): ## argument is the desired camera from the opencv list of connected cameras to the device; usually zero
    camera = cv2.VideoCapture(cam)

    _, image = camera.read() ## <-- _, is important because touple breaks otherwise

    print(type(image))

    cv2.imwrite(filename="cameracapture.jpg", img=image)

    print(strftime("%d.%m:%k%M%S"), " captured new image")


def detectCat(img):
    start = time() ## record the time the main function started, used later when calculating the runtime
    image = cv2.imread(img) ## <-- call the capImage function instead to use the webcam
    size = image.shape[:2] ## practicing python slicing, takes everything from the beginning to the second element, exclusive

    ## crop image
    cat = image[0:int((size[0]*.45)), 0:size[-1]] ## now it hypothetically get the top 45% of the image and stores that as 'cat'
    ### youtube tutorial and (some) code from https://github.com/techwithtim/OpenCV-Tutorials/blob/main/tutorial5.py ###

    ## grayscale now because the final deployment will be running on a device with 512megs of ram and the less numbers the better
    upperBound = 38
    lowerBound = 0

    ## get input image, then convert it to grayscale
    gray = cv2.cvtColor(cat, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("gray", gray)

    ## generate a binary image to be compared to the grayscale image
    mask = cv2.inRange(gray, lowerBound, upperBound)

    ## quick test to see how long it'll take my laptop to loop through the image took an hour for the raspi
    ## takes about 90 seconds for lower-res webcam images
    totalPixels = mask.shape[0] * mask.shape[1]
    totalWhite = 0
    for i in range(mask.shape[0] - 1): ## for every width
        for j in range(mask.shape[1] - 1): ## for every height
            print(mask[i, j])
            if mask[i, j] == 255: totalWhite += 1
    print(f"done in {time() - start}")

    ## if 15% of the image is white, and therefore the desired color, return true, otherwise, return false.
    if totalWhite / totalPixels >= .15:
        return True
    else:
        return False

## TODO crop the image and find out if A) cat is present and B) is there food in the bowl (but not yet because I don't have an image for that)

### end techwithtim adapted code ###
'''
- and then from here we need to delete the taken image
- store the time cat was last seen
- send push notifications?
'''
launchTime = int(time())
## this get the time since the program launched, and checks if it has been an even multiple of delayTime since then
if (int(time()) - launchTime) % delayTime == 0:
    detectCat("cameracapture.jpg")

## records the last time the cat was seen (but not really, there needs to be more logic)
# lastSeen = time()
# cv2.waitKey() ## imshow only works with waitkey() KEEP THIS WHEN SHOWING AN IMAGE!!!!!!!!!!1 ############
