import cv2
import numpy as np

img = cv2.imread("colorcolor.jpg")
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

karnel = np.ones((3, 3), np.uint8)
karnel2 = np.ones((5, 5), np.uint8)

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurImg = cv2.GaussianBlur(img, (7, 7), 5)
cannyImg = cv2.Canny(img, 150, 200)
dilateImg = cv2.dilate(cannyImg, karnel, iterations=2)
erodeImg = cv2.erode(dilateImg, karnel2, iterations=1)

cv2.imshow("Img", img)
cv2.imshow("Gray", grayImg)
cv2.imshow("Blur", blurImg)
cv2.imshow("Canny", cannyImg)
cv2.imshow("Dilate", dilateImg)
cv2.imshow("Erode", erodeImg)
cv2.waitKey(0)
