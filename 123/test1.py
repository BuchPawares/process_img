import cv2
img= cv2.imread('123/01.jpg')
img= cv2.resize(img,(500,500))
edges = cv2.Laplacian(img,ddepth=cv2.CV_8U,ksize=3)
cv2.imshow("img",edges)
cv2.waitKey()