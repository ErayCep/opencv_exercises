import numpy as np
import cv2

cap = cv2.VideoCapture('../DATA/hand_move.mp4')

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("No frame. Exiting..")
        exit()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
