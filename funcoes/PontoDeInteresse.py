import cv2
from .MediaPipeInversao import MediaPipeInversao

def PontoDeInteresse(frame, HX, HY, FX, FY):

    print(HX, HY, FX, FY)

    X1 = max(min(HX-150,FX-150),0)
    X2 = min(max(HX+150,FX+150),frame.shape[1])

    Y1 = max(min(HY-150, FY-150),0)
    Y2 = min(max(HY+150,FY+150),frame.shape[0])

    frameFLyer = frame[Y1:Y2,X1:X2]
    cv2.imwrite('C:\\Users\\vinic\\Desktop\\TCC\\Codigos\\Yolo\\Teste2.png', frameFLyer)

    MediaPipeInversao('C:\\Users\\vinic\\Desktop\\TCC\\Codigos\\Yolo\\Teste2.png')