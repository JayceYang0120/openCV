import cv2
import mediapipe as mp
import time
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
handLmsStyle = mpDraw.DrawingSpec(color=(0, 0, 255), thickness=5)
handConStyle = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=7)

pTime = 0
cTime = 0

while True:
    ret, frame = cap.read()
    if ret:
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(imgRGB)
        print(result.multi_hand_landmarks)
        imgHeight = frame.shape[0]
        imgWidth = frame.shape[1]

        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                mpDraw.draw_landmarks(
                    frame, handLms, mpHands.HAND_CONNECTIONS, handLmsStyle, handConStyle)
                for i, lm in enumerate(handLms.landmark):
                    xPos = int(lm.x * imgWidth)
                    yPos = int(lm.y * imgHeight)
                    cv2.putText(frame, str(i), (xPos - 25, yPos + 5),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
                    if i == 4:
                        cv2.circle(frame, (xPos, yPos), 10,
                                   (166, 56, 56), cv2.FILLED)
                    print(i, xPos, yPos)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(frame, f"FPS : {int(fps)}", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)

        cv2.imshow("Img", frame)
    else:
        break
    if cv2.waitKey(1) == ord('q'):
        break
