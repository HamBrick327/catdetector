import cv2
import os

camera = cv2.VideoCapture(0)

image = camera.read()

cv2.imwrite("cameracapture.jpg", image)

print("captured image")