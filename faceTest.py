import cv2
import mediapipe as mp
import time

mpfaceDetector =  mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
FaceDetection = mpfaceDetector.FaceDetection()

cap = cv2.VideoCapture(0)

pTime = 0

while True:
    success,img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = FaceDetection.process(imgRGB)
    if results.detections:
        for id,detection in enumerate(results.detections):
            boundingBox = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            Box = int(boundingBox.xmin * iw), int(boundingBox.ymin * ih), \
                int(boundingBox.width *iw), int(boundingBox.height * ih)
            cv2.rectangle(img,Box,(255,255,255),1)
            cv2.putText(img,f"Person:{int(detection.score[0]*100)}%",(Box[0],Box[1]-20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1.4,(255,255,255),1)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,f"FPS:{int(fps)}",(20,70),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),2)
    cv2.imshow('image',img)
    cv2.waitKey(10)