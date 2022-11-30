import cv2
import numpy as np

def getColorMask(img):
    lowerBound = np.array([0, 180, 255])
    upperBound = np.array([20, 255, 255])

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return cv2.inRange(hsv, lowerBound, upperBound)


cv2.namedWindow('image')
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    cv2.imshow('image', img)