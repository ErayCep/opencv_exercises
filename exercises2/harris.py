import cv2
import numpy as np

img = cv2.imread('../DATA/chessboard_mat.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

dst = cv2.dilate(dst, None)

img[dst>0.01*dst.max()] = [0,0,255]
cv2.namedWindow('dst')
while True:
    cv2.imshow('dst', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows() 


