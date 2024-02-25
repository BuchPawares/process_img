import cv2
img= cv2.imread('123/01.jpg')
img= cv2.resize(img,(500,500))
edges = cv2.Canny(img, 100,200)
cv2.imshow("img",edges)
cv2.waitKey()