import cv2

# Read the image from file
img = cv2.imread('..\Images\IMG_20230504_155035.jpg')

# Display the image
cv2.imshow('Image', img)
cv2.waitKey(0)
