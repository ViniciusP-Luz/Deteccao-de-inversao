from .Inversao import Inversao

def bodyParts(frame, corpo, flyer):

    head = corpo[flyer][0]
    HX = int(head[0])
    HY = int(head[1])

    Lfeet = corpo[flyer][16]
    LFX = int(Lfeet[0])
    LFY = int(Lfeet[1])

    Rfeet = corpo[flyer][15]
    RFX = int(Rfeet[0])
    RFY = int(Rfeet[1])

    RShoulder = corpo[flyer][6]
    RSX = int(RShoulder[0])
    RSY = int(RShoulder[1])

    LShoulder = corpo[flyer][5]
    LSX = int(LShoulder[0])
    LSY = int(LShoulder[1])

    shoulderX = int((LSX + RSX)/2)

    LHip = corpo[flyer][10]
    LHX = int(LHip[0])
    LHY = int(LHip[1])

    RHip = corpo[flyer][11]
    RHX = int(RHip[0])
    RHY = int(RHip[1])

    hipX = int((RHX + LHX)/2)

    # 0 =y
    # 1 = x

    # cv2.ellipse(frame,(hipX,RHY),(100,20),0,0,360,color=(0,0,255),thickness=5)
    # cv2.putText(frame,str(RHY),(RHX,RHY),5,5,(0,0,255),thickness=3)
    # cv2.ellipse(frame,(shoulderX,LSY),(100,20),0,0,360,color=(0,0,255),thickness=5)
    # cv2.putText(frame,str(RSY),(RSX,RSY),5,5,(0,0,255),thickness=3)
    # cv2.circle(frame,(LFX,LFY),25,(0,0,255),5)
    # cv2.putText(frame,str(LFY),(LFX,LFY),5,5,(0,0,255),thickness=3)
    # cv2.circle(frame,(RFX,RFY),25,(0,0,255),5)
    # cv2.putText(frame,str(RFY),(RFX,RFY),5,5,(0,0,255),thickness=3)
    # cv2.circle(frame,(HX,HY),25,(0,0,255),5)
    # cv2.putText(frame,str(HY),(HX,HY),5,5,(0,0,255),thickness=3)

    Inversao(HX, HY, LHY, LSY, LFY, LFY, RFY, frame)
