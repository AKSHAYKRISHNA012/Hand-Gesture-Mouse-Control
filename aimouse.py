import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy
#######
wcam , hcam = 680,450
frameR = 100  #Frame Reduction
smoothening = 20
#######

pTime = 0
plocx, plocy = 0,0
clocx, clocy = 0,0

cap=cv2.VideoCapture(0)
#screen resolution
cap.set(3,wcam) #width 3 means it reffers width of the frame
cap.set(4,hcam) #height 4 means it reffers width of the frame
detector=htm.handDetector(maxHands=1)
wScr,hScr = autopy.screen.size() #wScr - width of the screen, hScr - hight of the screen
#print(wScr,hScr)

while True:
    # 1, Find hand Landmarks
    sucess, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    #print(lmList)

    cv2.rectangle(img,(frameR,frameR),(wcam-frameR,hcam-frameR),(255,0,255),2) #This will show a rectangle frame as
    # default even if the hand is not brought in the camera.

    #2, Get the tip of the index and middle finger
    if len(lmList) !=0:
        x1,y1 = lmList[8][1:]
        x2,y2 = lmList[12][1:]
        #print(x1,y1,x2,y2)
        #cv2.rectangle(img, (frameR, frameR), (wcam - frameR, hcam - frameR), (255, 0, 255), 2) This will show the
        # rectangle frame only if the hand is brought infront of the screen.
        #3 Check which fingers are up
        fingers = detector.fingersUp()
        #print(fingers)

        #4 Only Index Finger : Moving Mode
        if fingers[1] == 1 and fingers[2] == 0:

            #5 Convert Coordinates
            x3 = np.interp(x1, (frameR, wcam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hcam - frameR), (0, hScr))

            #6 Smooten Values
            clocx = plocx + (x3 - plocx) / smoothening
            clocy = plocy + (y3 - plocy) / smoothening

            autopy.mouse.move(wScr - clocx, clocy)
            cv2.circle(img, (x1, y1), 15, (255, 8, 255), cv2.FILLED)
            plocx, plocy = clocx, clocy

        # 8 Both Index and middle fingers are up : Clicking Up
        if fingers[1] == 1 and fingers[2] == 1:
            # 9 Find di
            #7 Move Mousestance between fingers
            length, img, lineinfo = detector.findDistance(8,12,img)
            print(length)
            #10 Click mouse if distance short
            if length < 45:
                autopy.mouse.click()
                cv2.circle(img,(lineinfo[4],lineinfo[5]),15,(0,255,0),cv2.FILLED)
    #11, Frame Rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

    #12, Display
    cv2.imshow("webcam",img)
    cv2.waitKey(1)