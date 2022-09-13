import cv2
import numpy as np

img = cv2.imread("qq.jpg")

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier("face_detect.xml")
faceRect = faceCascade.detectMultiScale(grayImg, 1.1, 5)
print(len(faceRect))

for (x, y, w, h) in faceRect:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Img", img)
cv2.waitKey(0)
