valor = int(raw_input())
print valor
notasValores = [100,50,20,10,5,2,1]
notas = {100:0 ,50:0 ,20:0 ,10:0 ,5:0 ,2:0 ,1:0}

while(valor != 0):
    for x in notasValores:
        while(valor - x >= 0):
            notas[x] = notas[x]+1
            valor = valor - x

for x in notasValores:
    print("%d nota(s) de R$ %d,00" % (notas[x], x));
            
