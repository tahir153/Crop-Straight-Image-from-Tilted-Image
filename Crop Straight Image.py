import cv2
import numpy as np

img = cv2.imread("marvel.jpg")

width, height = 270,450
pts1 = np.float32([[313,75],[543,58],[311,507],[543,525]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutPut = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("image",img)
cv2.imshow("final output",imgOutPut)
# cv2.imwrite('final croped.png',imgOutPut)

cv2.waitKey(0)


