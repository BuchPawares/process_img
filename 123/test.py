import cv2
import numpy as np
import matplotlib.pyplot as plt
img= cv2.imread('123/01.jpg')
img= cv2.resize(img,(500,500))
Sobel = cv2.Sobel(img,ddepth=cv2.CV_8U,dx=1,dy=1,ksize=3)
Laplacian = cv2.Laplacian(img,ddepth=cv2.CV_8U,ksize=3)
Canny = cv2.Canny(img, 100,200)
cv2.imshow("img",img,)
cv2.imshow("Sobel",Sobel)
cv2.imshow("Laplacian",Laplacian)
cv2.imshow("Canny",Canny)
cv2.waitKey()
