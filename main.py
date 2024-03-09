import cv2
import numpy as np

# Read the image
image = cv2.imread('input_image.jpg')
print(image[375][95])

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define a threshold value and apply thresholding
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a mask
mask = np.zeros_like(image)

# Draw contours on the mask
cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

# Apply the mask to the original image
masked_image = cv2.bitwise_and(image, mask)

# Display the original image and masked image
cv2.imshow('Original Image', image)
cv2.imshow('Masked Image', masked_image)

# Wait for key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
