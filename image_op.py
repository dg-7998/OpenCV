import cv2
import numpy as np

img = cv2.imread('/home/pc001/DBS Wallpapers/Screenshot (3).png',0)

rows,cols = img.shape[:2]

x,y=rows/2,cols/2

    #for translation operation
#T = np.float32([[1,0,x], [0,1,y]])  
#img_translation = cv2.warpAffine(img, T, (rows,cols))
#cv2.imshow('Translation',img_translation)


    #for rotating an image
#R = cv2.getRotationMatrix2D((x,y),90,.5)
#rotated_img = cv2.warpAffine(img, R, (rows,cols))
#rotated_img = cv2.transpose(img) #2nd method for rotating an image
#cv2.imshow('Rotated Image', rotated_img)

    #for sharpening an image
#cv2.imshow('Original',img)
#kernel_sharpening = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
#sharpened = cv2.filter2D(img, -1, kernel_sharpening)
#cv2.imshow('Sharpened',img)

    #for blurring an image USING FILTER2D
#kernel_7x7 = np.ones((7,7), np.float32) / 49
#blurred = cv2.filter2D(img, -1, kernel_7x7)
#cv2.imshow('Blurred', blurred)

    #for blurring using GAUSSIAN BLUR
#gaussian = cv2.GaussianBlur(img, (5,5), 0)
#cv2.imshow('Gaussian blur', gaussian)

    #THRESHOLDING AN IMAGE
#ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#cv2.imshow('image',thresh1)
#ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
#cv2.imshow('image',thresh2)
#ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
#cv2.imshow('image',thresh3)
#ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
#cv2.imshow('img',thresh4)
#ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
#cv2.imshow('img',thresh5)
#thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)
#cv2.imshow('adaptive thresholding', thresh)
#_,th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#cv2.imshow('otsu', th2)
#_,th3 = cv2.threshold(gaussian, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#cv2.imshow('gaussian otsu', th3)

    #EDGE DETECTION
#canny = cv2.Canny(img,60,150)
#cv2.imshow('Canny',canny)


cv2.waitKey(0)
cv2.destroyAllWindows()
