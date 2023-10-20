#This code is implemented as part of CFC 2023 for Project Nutribuddy
#The purpose of the code is to capture the image of the plant

import cv2
from time import sleep
videoCaptureObject = cv2.VideoCapture(0)
result = True
count=1
fps = int(videoCaptureObject.get(cv2.CAP_PROP_FPS))
while(result):
    ret,frame = videoCaptureObject.read()
    if count%(3*fps) == 0 :
        cv2.imwrite("image.jpg",frame)
        result = False
    count+=1
print(count)   
videoCaptureObject.release()
#cv2.destroyAllWindows()

