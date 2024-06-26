#Face Detection using haarcascade file 
import cv2
import numpy

image=cv2.imread("capture0.png")
gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #convert into gray 
face=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #for detecting face

# parameters(img,scale_factor[reduce image size],min_neighbour)
faces = face.detectMultiScale(gray,1.2,3)   #for  faces

for(x,y,w,h) in faces:
    
    image=cv2.rectangle(image,(x,y),(x+w,y+h),(127,0,205),3)
    
    
image = cv2.resize(image,(800,600))
cv2.imshow("Face Detected",image)
cv2.waitKey(0)
cv2.destroyAllWindows()    


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       