import cv2

cap=cv2.VideoCapture(0)

while True:
    ret,img=cap.read()
    if ret:
        cv2.imshow('video',img)
    cv2.waitKey(1)
    