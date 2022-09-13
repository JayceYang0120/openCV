""" - openCV Note: -

1. 電腦辨識圖片 : 白色標記1，黑色標記0
2. 黑白圖片:2 levels 六種顏色:6 levels 16種顏色:16 levels -> 
    用0, 1, 2, 3, 4, 5, etc.來表示顏色
3. 灰階圖像(Gray Scale Image) : 8 Bits = 2^8 = 256 levels"4. 彩色圖片(RBG Image)可以紅綠藍(RGB)合成，每一個各有256levels，
    0是黑色，255是最紅(綠, 藍)"5. RGB尺寸表示 : RGB 480 x 720 x 3 -> width480 x height720 x channel3 
    channel(通道):共有紅綠藍通道 480x720每一格皆用[R, G, B]來表示顏色
"""

""" - openCV Step: - 
1. terminal -> pip install openCV-python

一、Image Read:
1. cv2.imread() : 與圖片需在同一層資料夾
2. imshow(param1 : 標題, param2 : 目標圖片)
3. waitKey(param1 : 等待時間(毫秒)) 
    -> waitKey(0) : 無限久直到主動關閉(click x or Press any button) -> 在等按鍵的編號直到時間到
4. resize(param1 : 目標圖片, param2 : (width, height)) 
    or resize(param1, param2 : (0, 0), param3 : fx = 縮放倍率, param4 : fy = 縮放倍率)

二、Video Read:
1. VideoCapture() : 捕捉影片中的每一禎。
    cv2.VideoCapture(0) : 為視訊鏡頭，若有2個以上鏡頭就VideoCapture(1)、cap = cv2.VideoCapture(2)..以此類推
2. read() : 會回傳兩個數值 -> ret : 是否有下一禎(boolean) frame : 下一禎圖片(image)，前提是ret是true
"""

import cv2

img = cv2.imread("colorcolor.jpg")

# img = cv2.resize(img, (500, 700))
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
cv2.imshow("img", img)
cv2.waitKey(1000)

cap = cv2.VideoCapture("thumb.mp4")
# cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0, 0), fx=0.4, fy=0.4)
    if ret:
        cv2.imshow("video", frame)
    else:
        break
    if cv2.waitKey(10) == ord('q'):
        break
