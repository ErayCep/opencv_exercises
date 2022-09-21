import cv2

img = cv2.imread('./images/364917a8bc4abdfe92f7bfa4cda8cf30.jpg')

while True:

  cv2.imshow('CV2_WINDOW', img)

  if cv2.waitKey(1) & 0xFF == 27:
    break

cv2.destroyAllWindows()
