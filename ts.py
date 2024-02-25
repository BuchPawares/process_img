import cv2
import numpy
img= cv2.imread('123.jpg')
edges = cv2.Sobel(img,ddepth=cv2.CV_8U,dx=1,dy=0,ksize=3)
#i= cv2.imread(edges)
cv2.imshow("img",edges)
cv2.waitKey(0)