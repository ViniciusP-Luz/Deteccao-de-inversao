import cv2
def CriaEixo(frame):
    #Cria linha X
    cv2.line(frame,(0,10),(frame.shape[1],10),color=(0,0,0),thickness=3)
    #Cria Linha Y
    cv2.line(frame,(10,0),(10,frame.shape[0]),color=(0,0,0),thickness=3)
    X = 0
    Y = 0
    #Cria eixo X
    while(X < frame.shape[1]):
        if( X % 50 == 0):
            cv2.putText(frame,f'{X}',(X-15,40),1,1,color=(0,0,0),thickness=2)
            cv2.line(frame,(X,5),(X,20),color=(0,0,0),thickness=2)
        else:
            cv2.line(frame,(X,5),(X,15),color=(0,0,0),thickness=2)
        X += 10
    while(Y < frame.shape[0]):
        if( Y % 50 == 0):
            cv2.putText(frame,f'{Y}',(23,Y+5),1,1,color=(0,0,0),thickness=2)
            cv2.line(frame,(3,Y),(17,Y),color=(0,0,0),thickness=2)
        else:
            cv2.line(frame,(5,Y),(15,Y),color=(0,0,0),thickness=2)
        Y += 10