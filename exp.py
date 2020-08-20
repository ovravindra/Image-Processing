
import cv2

'''
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)
while True:
    success, image = cap.read()
    cv2.imshow("Video", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''

img = cv2.imread('./iu.gif')
image= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("pic", image)

