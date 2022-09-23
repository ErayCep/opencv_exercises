import cv2



def draw_rectangle(event, x, y, flags, param):
    global pt1,pt2,topClicked,botClicked
    
    if event == cv2.EVENT_LBUTTONDOWN:
        if topClicked & botClicked:
            pt1=(0,0)
            pt2=(0,0)
            topClicked = False
            botClicked = False
        if topClicked == False:
            pt1=(x,y) 
            topClicked = True
        elif botClicked == False:
            pt2=(x,y) 
            botClicked = True

pt1 = (0,0)
pt2 = (0,0)
topClicked=False
botClicked=False
cap = cv2.VideoCapture(0)
cv2.namedWindow('draw')
cv2.setMouseCallback('draw', draw_rectangle)

if not cap.isOpened():
    print("File could not opened")
    exit()

while True:
    ret,frame = cap.read()
    
    if topClicked:
        cv2.circle(frame, center=pt1, radius=4, color=(0,0,255), thickness=-1)
    if topClicked & botClicked:
        cv2.rectangle(frame, pt1, pt2, color=(0,0,255), thickness=4)
        
    cv2.imshow('draw', frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
