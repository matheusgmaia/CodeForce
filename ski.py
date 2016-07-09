
nobjetos = int(raw_input())
tiposSTR = raw_input()
tracksSTR = raw_input()

exemploF = ""
resultadoF = 0
pointer = 0
contador = [0]*(nobjetos+1)

tipos = []
tmp = ""
ums = []
contadorum = 0



for v in xrange(len(tiposSTR)):
    d = tiposSTR[v]
    if d == " ":
        tipos.append(int(tmp))
        if(tmp == "1"):
            ums.append(int(contadorum))
        tmp = ""
    else:
        tmp += d
        contadorum += 1
if tmp:
    tipos.append(int(tmp))
    if(d == "1"):
        if(tmp == "1"):
            ums.append(int(contadorum))
            contadorum += 1


tracks = []
tmp = ""
for c in tracksSTR:
    if c == " ":
        tracks.append(int(tmp))
        contador[int(tmp)] += 1
        tmp = ""
    else:
        tmp += c
if tmp:
    tracks.append(int(tmp))
    contador[int(tmp)] += 1

for x in ums:
    resultadoP = 1
    exemplo = ""
    exemplo = ("%d" % (int(x)))
    pointer = tracks[x-1]
    while(pointer != 0 and contador[pointer]<2):
        exemplo = ("%d " % pointer) + (exemplo)
        pointer = tracks[pointer-1]
        resultadoP += 1
    if(resultadoF < resultadoP):
        exemploF = exemplo
        resultadoF = resultadoP

print resultadoF
print exemploF
