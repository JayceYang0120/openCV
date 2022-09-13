import cv2
import numpy as np

img = np.zeros((600, 600, 3), np.uint8)

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 2)

cv2.rectangle(img, (0, img.shape[0] // 2), (img.shape[1] // 2, img.shape[0]), (0, 0, 255), cv2.FILLED)

cv2.circle(img, (int(img.shape[1] * 0.75), int(img.shape[0] * 0.25)), 100, (255, 0, 0), 2)

cv2.putText(img, "Hello", (int(img.shape[1] * 0.5, ), int(img.shape[0] * 0.25)), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)

cv2.imshow("Img", img)
cv2.waitKey(0)
