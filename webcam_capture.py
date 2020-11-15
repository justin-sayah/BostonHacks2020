'''
Opens a webcam window, and awaits user to input 'q' to quit.
|
Saves a screenshot every half second in running dir
'''
import cv2
import time

camera = cv2.VideoCapture(0)
lastCapture = time.time()

#method to check if a second has passed
def checkTime(curTime,image):
    if(time.time() - curTime > 0.5):
        #overwrites the previous image captured
        cv2.imwrite('Active_Captures/frame.jpg',image)
        lastCapture = time.time()

def getVideoFrame():
    while(1):
        return_value,image = camera.read()
        cv2.imshow('image',image)
        checkTime(lastCapture,image)
        #quits with the key q
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    camera.release()
    cv2.destroyAllWindows()

getVideoFrame()