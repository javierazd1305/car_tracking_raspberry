import cv2
import numpy as np
import imutils
from imutils.video import VideoStream

#initialize variables
webcam = VideoStream(src=0).start() #usb camera
count = 0
text = "empty"
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows = True)

while 1:
    #start video
    img = webcam.read()
    img = imutils.resize(img, width=300)
    #subtract the background
    fgmask = fgbg.apply(img)
    #threshold the fgmask
    ret, fgmask_thresh = cv2.threshold(fgmask, 50, 250, cv2.THRESH_BINARY)
    #dilate for better image quality
    fgmask_dilate = cv2.dilate(fgmask_thresh, None, iterations = 2)
    #get the contours of the images
    image, contours, hierarchy = cv2.findContours(fgmask_thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #detect movement
    for cnt in contours:
        # we only detect the contours that are higher than 300
        if cv2.contourArea(cnt) > 300:
            x,y,w,h = cv2.boundingRect(cnt)
            #we resize the detecton area
            if x > 80 and x < 290 and y > 100 and y < 220
                text = "car"
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                #if the center point satisfies then counter +1
                if x > 142 and x < 217 and y > 181 and y < 188:
                    count += 1
                    print count, ' a'
                elif x > 150 and x < 230 and y > 121 and y < 129:
                    count += 1
                    print count, ' b'
            else:
                text = 'empty'

    #draw de limits with points
    cv2.circle(img, (142, 181), 3, (0,0,255),-1)
    cv2.circle(img, (217, 188), 3, (0,0,255),-1)
    cv2.circle(img, (150, 121), 3, (0,0,255),-1)
    cv2.circle(img, (230, 129), 3, (0,0,255),-1)

    cv2.circle(img, (80, 100), 3, (0,0,255),-1)
    cv2.circle(img, (290, 220), 3, (0,0,255),-1)

    #put dynamic text
    cv2.putText(img, "status: {}".format(text), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)

    #show images
    cv2.imshow('img', img)
    cv2.imshow('dilate' fgmask_dilate)

    #press esc to destroy the bucle
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

#end program
cv2.destroyAllWindows()
webcam.stop()
