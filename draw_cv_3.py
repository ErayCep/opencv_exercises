import cv2
import numpy as np

def draw_circle(event, x, y, flahs, param):
  if event == cv2.EVENT_LBUTTONDOWN:
    cv2.circle(img, (x,y), 100, (255,0,0), thickness=10) 

cv2.namedWindow(winname='drawimage')
cv2.setMouseCallback('drawimage', draw_circle)

img = cv2.imread('./images/364917a8bc4abdfe92f7bfa4cda8cf30.jpg')

while True:
  cv2.imshow('drawimage', img)

  if cv2.waitKey(20) & 0xFF == 27:
    break
cv2.destroyAllWindows()
