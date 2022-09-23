import cv2
import time
cap = cv2.VideoCapture('testvideo.mp4')

if not cap.isOpened():
    print("Video could not opened")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("No frame")
        break
    time.sleep(1/30)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
