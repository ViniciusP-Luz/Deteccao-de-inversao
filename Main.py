from funcoes import *
import copy
from ultralytics import YOLO
import cv2
model = YOLO("yolo11n-pose.pt")


def main():
    #results = model.track(source='frame_233.jpg', stream=False)
    results = model.track(source='131.mp4', stream=True)
        
    #idendificar quantas pessoas possui no vídeo/imagem
    if (results):
        #imagem
        #classes = results[0].boxes.cls
        #video
        classes = next(results).boxes.cls
        pessoas = (classes == 0).sum()
        print(f"tem {int(pessoas)} no video")


    for i, r in enumerate(results):
        #Pular um x número de frames para agilizar a execução 
        if i < 230:
            continue 
        frame = r.plot(kpt_radius=0, kpt_line= False,boxes=False, conf=False, labels=False, masks=False)
        corpo = r.keypoints.xy
        flyer = FindFlyer(r, corpo)
        
        #Plotar apenas as marcas de corpo para a flyer 
        '''
        r_copy = copy.deepcopy(r)
        r_copy.keypoints = r.keypoints[flyer:flyer+1]
        #frame = r_copy.plot(kpt_radius=5, kpt_line=True,boxes=False, conf=False, labels=False, masks=False) '''

        bodyParts(frame, corpo, flyer)
        CriaEixo(frame)
        frame = cv2.resize(frame, (600, 800))

        cv2.imwrite('Teste.png', frame)

        cv2.imshow("YOLO Pose", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()