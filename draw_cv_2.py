import cv2
import numpy as np

ix, iy = -1,-1
drawing = False

def draw_rectangle(event,x,y,flash,param):
  global ix,iy,drawing

  if event == cv2.EVENT_LBUTTONDOWN:
    drawing = True
    ix,iy = x,y
  elif event == cv2.EVENT_MOUSEMOVE:
    if drawing == True:
      cv2.rectangle(img, (ix,iy), (x,y), (0,0,255), -1)
  elif event == cv2.EVENT_LBUTTONUP:
    drawing = False
    cv2.rectangle(img, (ix,iy), (x,y), (0,0,255), -1)
cv2.namedWindow(winname='drawing2')
cv2.setMouseCallback('drawing2',draw_rectangle)

img = np.zeros((512,512,3))

while True:
  cv2.imshow('drawing2', img)

  if cv2.waitKey(20) & 0xFF == 27:
    break
cv2.destroyAllWindows()
