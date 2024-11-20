import cv2
import mediapipe as mp
import time 

# Passing video feed to cv2 for image processing 
# cap = cv2.VideoCapture('videos/1.mp4')
cap = cv2.VideoCapture(0)


# By passing 0 as argument to cv2.videoCapture we can pass webcam feed to cv2 

# cap = cv2.VideoCapture(0)

# By this method we can set desired size of python window of face detection
# cv2.namedWindow("image", cv2.WINDOW_NORMAL)
# cv2.resizeWindow('image', 1920, 1080)

# Setting the variable pTime to 0
pTime = 0


mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(0.75)

# This will make our project to run for forever until we close it 
while True:
    success, img = cap.read()
    
    # Converting the image colors from BGR to RGB 
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Processing the image to detect faces in the particular frame 
    results = faceDetection.process(imgRGB)
    # print(results)
    if results.detections:
        # Proceeding with the detected face to draw boxes around them 
        for id,detection in enumerate(results.detections):
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            # Setting the box coordinates around the detected faces 
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                int(bboxC.width * iw), int(bboxC.height * ih)
            # Putting the box around the detected face in the frame  
            cv2.rectangle(img, bbox, (255,0,255), 2)
            # Putting the value of face possibility above the face 
            cv2.putText(img,f'Person: {int(detection.score[0]*100)}%',(bbox[0],bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 2)

    # getting the current time 
    cTime = time.time()
    # getitng the frames value in per second 
    fps = 1/(cTime-pTime)
    pTime = cTime
    # Showing the frames value in per second on the screen 
    cv2.putText(img,f'FPS: {int(fps)}',(20,70), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 2)
    cv2.imshow('image',img)
    # Waiting for a speicific time to check again in the frame 
    cv2.waitKey(10)