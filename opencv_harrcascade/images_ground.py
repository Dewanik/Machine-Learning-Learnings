import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

imge = cv2.VideoCapture(0)
while True:

    ret,img = imge.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
    	img = cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   

	



cv2.destroyAllWindows()