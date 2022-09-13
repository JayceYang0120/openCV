import numpy as np
import cv2

cap = cv2.VideoCapture(0)

penColorHSV = [[90, 120, 130, 105, 255, 255],
               [65, 80, 85, 80, 135, 255],
               [0, 130, 175, 179, 220, 255]]

penColorBGR = [[255, 0, 0], [0, 255, 0], [0, 0, 255]]

drawPoints = []

def findPen(img):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for i in range(len(penColorHSV)):
        lower = np.array(penColorHSV[i][:3])
        upper = np.array(penColorHSV[i][3:6])

        mask = cv2.inRange(hsv, lower, upper)
        result = cv2.bitwise_and(frame, frame, mask=mask)
        penX, penY = findContour(mask)
        cv2.circle(imgContour, (penX, penY), 10, penColorBGR[i], cv2.FILLED)

        if penY != -1:
            drawPoints.append([penX, penY, i])

def findContour(img):
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    x, y, w, h = -1, -1, -1, -1
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            vertices = cv2.approxPolyDP(cnt, peri * 0.02, True)
            x, y, w, h = cv2.boundingRect(vertices)

    return x + w // 3, y

def draw(drawPoints):
    for point in drawPoints:
        cv2.circle(imgContour, (point[0], point[1]), 10, penColorBGR[point[2]], cv2.FILLED)

while True:

    ret, frame = cap.read()
    if ret:
        imgContour = frame.copy()
        cv2.imshow("Img", frame)
        findPen(frame)
        draw(drawPoints)
        cv2.imshow("Contour", imgContour)
    else:
        break
    if cv2.waitKey(10) == ord('q'):
        break
