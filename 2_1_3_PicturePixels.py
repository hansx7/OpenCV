import cv2
import numpy as np

img = cv2.imread('figure1.jpg')
print img.size
print img.shape
img[100:120, 100:120] = [255, 255, 255]
cv2.imshow('figure2.jpg', img)
cv2.waitKey()
