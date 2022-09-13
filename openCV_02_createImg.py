import cv2
import numpy as np
import random

img = cv2.imread("colorcolor.jpg")
print(type(img))
print(img.shape)

img2 = np.empty((300, 300, 3), np.uint8)

for row in range(300):
    for col in range(300):
        img2[row][col] = [random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255)]

cv2.imshow("Image", img2)
cv2.waitKey(1000)

for row in range(300):
    for col in range(img.shape[1]):
        img[row][col] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow("Image", img)
cv2.waitKey(1000)

newImg = img[865:1015, 500:700]  # 右下
newImg2 = img[865:1015, :200]  # 左下
cv2.imshow("img", img)
cv2.imshow("newimg", newImg)
cv2.imshow("newimg2", newImg2)
cv2.waitKey(0)
