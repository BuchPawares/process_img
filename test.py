import numpy as np
import matplotlib.pyplot as plt
import imageio.v3 as imr 
def rgbtogray(im):
    gray = 0.299*im[:,:,0]+0.587*im[:,:,1]+0.114*im[:,:,2]
    return gray
imarray=imr.imread('123.jpg')
im=np.array(imarray)
gray=rgbtogray(im)
plt.imshow(gray,cmap='gray')
plt.show()