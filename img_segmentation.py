import cv2
import numpy as np

img = cv2.imread('/home/pc001/Desktop/index.jpeg')
cv2.imshow('Contours',img)
cv2.waitKey(0)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Contours',gray)
cv2.waitKey(0)

edged = cv2.Canny(gray,30,120)
cv2.imshow('Contours',edged)
cv2.waitKey(0)


_, contours, hierarchy = cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('Canny Edges after Contouring',edged)
cv2.waitKey(0)


print("No of Contours found = " + str(len(contours)))

cv2.drawContours(img, contours[0] , -1, (0,255,0),3)
cv2.imshow('Contours',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
