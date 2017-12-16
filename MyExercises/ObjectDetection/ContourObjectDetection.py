import numpy as np
import cv2

img = cv2.imread("detect_blob.png",1)
img = cv2.resize(img,(0,0), fx=0.5, fy=0.5)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,115,1)

cv2.imshow("Original", img)
cv2.imshow("Binary", thresh)


cv2.waitKey(0)
cv2.destroyAllWindows()
