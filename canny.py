import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:

    ret,frame=cap.read()
    img=cv2.Laplacian(frame,cv2.CV_64F)
    frame=cv2.Canny(frame,200,250)

    cv2.imshow("laplacian",img)
    cv2.imshow("canny",frame)
    if cv2.waitKey(20) & 0xff==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
