import cv2

img = cv2.imread('assets/test.png')
img = cv2.resize(img, (800, 400))

cv2.imshow('Wow this works?', img)
cv2.waitKey(0)
cv2.destroyAllWindows()