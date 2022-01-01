import cv2
import numpy as np
from matplotlib import pyplot as plt
from numpy.core.fromnumeric import shape

#contoh 1

# imggambar = cv2.imread("contoh.png",1)
# cv2.imshow('hasil',imggambar)

# cv2.waitKey(0)
# cv2.destroyAllWindows

#contoh 2

# imggambar = cv2.imread("contoh.png",0)
# imggambar = cv2.cvtColor(imggambar,cv2.THRESH_BINARY)
# kernel = np.ones((35,35),np.uint8)
# imgclosing = cv2.morphologyEx(imggambar,cv2.MORPH_CLOSE,kernel)
# plt.subplot(2,2,3), plt.imshow(imgclosing, 'gray')
# plt.savefig('hasil.jpg')
# plt.show()

# cv2.waitKey(0)
# cv2.destroyAllWindows

#no 1

# imggambar = cv2.imread("contoh.png",1)
# tampil_hor=np.concatenate((imggambar,imggambar),axis=1)
# cv2.imshow('hasil',tampil_hor)
# cv2.waitKey(0)
# cv2.destroyAllWindows

#no 2

# imggambar = cv2.imread("contoh.png",1)
# imgmedian=cv2.medianBlur(imggambar,15)
# tampil_hor=np.concatenate((imggambar,imgmedian),axis=1)
# cv2.imshow('hasil',tampil_hor)
# cv2.waitKey(0)
# cv2.destroyAllWindows

#no 3

# imggambar = cv2.imread("contoh.png",1)
# height , width = imggambar.shape[: 2]
# qheight , qwidth = height/4, width/4
# T = np.float32([[1,0, qwidth],[0,1,  qheight]])
# img_translation = cv2.warpAffine(imggambar, T,(width,height))
# tampil_hor=np.concatenate((imggambar,img_translation),axis=1)
# cv2.imshow('hasil',tampil_hor)
# cv2.waitKey(0)
# cv2.destroyAllWindows

#no 4

# imggambar = cv2.imread("contoh.png",1)

# rows,cols = imggambar.shape[: 2]
# M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
# imgrotasi = cv2.warpAffine(imggambar,M,(cols,rows))
# tampil_hor=np.concatenate((imggambar,imgrotasi),axis=1)
# cv2.imshow('hasil',tampil_hor)
# cv2.waitKey(0)
# cv2.destroyAllWindows

# no 5

# img=cv2.imread("contoh.png",0)
# img=cv2.medianBlur(img,5)

# ret,th1 = cv2.threshold(img,70,255,cv2.THRESH_BINARY)

# plt.subplot(2,2,1),plt.imshow(img,'gray')
# plt.subplot(2,2,2),plt.imshow(th1,'gray')
# plt.show()

#no 6
# img=cv2.imread("contoh.png",0)

# img=cv2.medianBlur(img,5)

# th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,6)
# plt.subplot(2,2,3), plt.imshow(th2,'gray')
# plt.show()