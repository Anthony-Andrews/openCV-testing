import cv2
import numpy as np

def getColorMask(img):
    lowerBound = np.array([100, 45, 45])
    upperBound = np.array([130, 255, 255])

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return cv2.inRange(hsv, lowerBound, upperBound)

cap = cv2.VideoCapture(1)

while True:
    ret, img = cap.read()
    cv2.imshow('mask', getColorMask(img))
    cv2.imshow('image', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()