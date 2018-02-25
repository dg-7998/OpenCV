import cv2
import numpy as np

def sketch(image):
    #converting image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #removing noise or cleaning up the image using Gaussian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray,(5,5),0)

    #Extracting the edges
    canny_edges = cv2.Canny(img_gray_blur,10,70)

    #Inverting the image
    ret,mask = cv2.threshold(canny_edges,70,255,cv2.THRESH_BINARY_INV)
    return mask


        #main function
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    cv2.imshow('Live Sketcher', sketch(frame))
    if cv2.waitKey(1) == 13: #13 is Enter Key
        break

cap.release()
cv2.destroyAllWindows()
