import numpy as np
import cv2

bw = cv2.imread("detect_blob.png", 0)
height, width = bw.shape[0:2]
cv2.imshow("Original BW", bw)

binary = np.zeros([height, width,1], 'uint8')

thresh = 85

for row in range(0, height):
    for column in range(0,width):
        if bw[row][column]>thresh:
            binary[row][column] = 255

cv2.imshow("Slow Binary", binary)
cv2.waitKey(0)

cv2.destroyAllWindows()

