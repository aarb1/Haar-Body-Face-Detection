import cv2
import numpy as np

# Acquired from https://github.com/Itseez/opencv/blob/master/data/haarcascades
ub_cas = cv2.CascadeClassifier('haarcascade_upperbody.xml')
lb_cas = cv2.CascadeClassifier('haarcascade_lowerbody.xml')
fb_cas = cv2.CascadeClassifier('haarcascade_fullbody.xml')
ff_cas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cas = cv2.CascadeClassifier('haarcascade_eye.xml')

wc_feed = cv2.VideoCapture(0)

isReading = True

while isReading:
    # Reading a frame and storing into feed
    _,feed = wc_feed.read()
    # Converting the frame into grayscale as it is easier to detection on a single channel image
    gsFeed = cv2.cvtColor(feed, cv2.COLOR_BGR2GRAY)
    
    ff = ff_cas.detectMultiScale(gsFeed)
    #ff = ff_cas.detectMultiScale(gsFeed, 1.3, 5)
    #ff = ub_cas.detectMultiScale(gsFeed)
    #ff = ff_cas.detectMultiScale(gsFeed, 1.01, 5)
    #ff = fb_cas.detectMultiScale(gsFeed)
         
    for (x,y,width, length) in ff:
        cv2.rectangle(feed,(x,y),(x + width,y + length),(0,50,200),2)
        
    cv2.imshow('Detection Window', feed)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release capture when closing application
wc_feed.release()
cv2.destroyAllWindows()