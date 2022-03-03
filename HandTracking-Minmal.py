import cv2
import mediapipe as mp
import time

capture = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
PrevTime=0 #previous time
CurTime=0  #current time

while True:
    success,img = capture.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #Convert BGR to RGB 
    results = hands.process(imgRGB)

    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLMS in results.multi_hand_landmarks:
            for id,lm in enumerate(handLMS.landmark):
                h,w,c = img.shape # h-height , w-weight , c-channel
                cx,cy = int(lm.x*w),int(lm.y*h) # cx is center position in x-axis , cy is center position in y-axis
                print(id,":",cx,cy)

                if id==4 or id==8 or id==12 or id==20 or id==16:
                    cv2.circle(img,(cx,cy),12,(0,255,0),cv2.FILLED)

            mpDraw.draw_landmarks(img,handLMS,mpHands.HAND_CONNECTIONS)

    CurTime = time.time()
    fps = 1/(CurTime-PrevTime)
    PrevTime = CurTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_SIMPLEX,3,(255,0,0),3) # to show text on image
    cv2.imshow("Image",img)
    cv2.waitKey(1)