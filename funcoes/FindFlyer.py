def FindFlyer(r, corpo):
    YHead = 100000000000
    flyer = 0
    XHead = 0
    for i in range(len(r)):
        HHHead = corpo[i][0]
        HHX = int(HHHead[0])
        HHY = int(HHHead[1])
        if (HHY < YHead):
            YHead = HHY
            XHead = HHX
            flyer = i
    print(f"A FLYER È A PESSOA {flyer}")

    return (flyer)
