from .PontoDeInteresse import PontoDeInteresse
import cv2


def Inversao(HeadX, HeadY, Hip, Shoulder, LfeetX, LfeetY, RFeet, frame):
    PontoDeInteresse(frame, HeadX, HeadY, LfeetX, LfeetY)
    if (HeadY > Shoulder > Hip > LfeetX or HeadY > Shoulder > Hip > RFeet):
        # foto = cv2.imwrite("frame.jpg",frame-5)
        cv2.putText(frame, "INVERSAO", (10, 400),5, 4, (0, 0, 255), thickness=3)
        cv2.putText(frame, "DETECTADA", (10, 480), 5, 3, (0, 0, 255), thickness=3)
        cv2.circle(frame, (HeadX, HeadY), 25, (0, 0, 255), 1)
        cv2.circle(frame, (Hip, Hip), 25, (0, 0, 255), 1)
        cv2.circle(frame, (LfeetX, LfeetY), 25, (0, 0, 255), 1)
        frame = cv2.resize(frame, (600, 800))
        cv2.imshow("YOLO Pose", frame)
        # time.sleep(5)
        # InteressPoint(Head,LfeetX,RFeet,frame)
