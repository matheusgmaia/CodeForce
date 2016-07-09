quantTestes = 1
saida = ""
while(quantTestes != 0):
    quantTestes = int(raw_input())
    if(quantTestes) == 0:
        break
    xLinha, yLinha = map(int, raw_input().split())
    for x in range(quantTestes):
        xCord, yCord = map(int, raw_input().split())
        if(xCord == xLinha or yCord == yLinha):
            saida += "divisa\n"

        elif(xCord > xLinha):
            if(yCord > yLinha):
                saida += "NE\n"
            else:
                saida += "SE\n"
        elif(xCord < xLinha):
            if(yCord < yLinha):
                saida += "SO\n"
            else:
                saida += "NO\n"
print saida[:-1]
