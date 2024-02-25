import cv2
import numpy as np 

image= cv2.imread('123.jpg', cv2.IMREAD_GRAYSCALE)
threshold=128
bw_image= cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('BW image', bw_image)
cv2.waitKey(0)