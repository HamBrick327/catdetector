import cv2
import os

camera = cv2.VideoCapture(0)

_, image = camera.read()

print(type(image))

cv2.imwrite(filename="cameracapture.jpg", img=image)

print("captured image")
