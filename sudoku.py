testes = int(raw_input())
subs = [[0,1,2],[3,4,5],[6,7,8]]
numeros = (1,2,3,4,5,6,7,8,9)
for x in xrange(testes):
    print "Instancia %d" % int(x+1)
    matriz = []
    for x in xrange(9):
        matriz.append(map(int, raw_input().split()))
    ok = True
    """Verifica linhas"""
    for linha in xrange(9):
        for x in numeros:
            if x not in matriz[linha]:
                ok = False


    """Verifica colunas"""
    for linha in xrange(9):
        soma = 0
        for coluna in xrange(9):
            soma += int(matriz[coluna][linha])
        if(soma != 45):
            ok = False
    """Verifica submatrizes"""
    for x in xrange(3):
        for z in xrange(3):
            soma = 0
            for y in subs[x]:
                for w in subs[z]:
                    soma += int(matriz[y][w])
            if soma != 45:
                ok = False
    if(ok == False):
        print "NAO\n"
    else:
        print "SIM\n"
