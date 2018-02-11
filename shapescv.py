import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
img=cv2.line(img,(0,0),(511,511),(255,0,0),5)
img=cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
img=cv2.circle(img,(447,63),63,(0,0,255),-1)
img=cv2.ellipse(img,(256,256),(100,50),0,0,360,255,-1)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Deep',(0,256),font,2,(255,255,255),2,cv2.LINE_AA)
cv2.imshow('image',img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('shapes.png',img)
    cv2.destroyAllWindows()
