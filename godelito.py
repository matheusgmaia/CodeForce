lista = [3]
#40 vs
for x in xrange(40):
    saida = ""
    #todas as letras dao elemento anterior da lista
    y = 0
    """if(x > 5):
        saida += str(lista[x -2])
        y = (len(str(lista[x -3])))"""
    while (y < len(str(lista[x]))):
        counter = 0
        #contar se repete e adiciona
        for z in xrange(y, len(str(lista[x]))-1):
            if(str(lista[x])[z] == str(lista[x])[z+1]):
                counter +=1
            else:
                break
        saida += str(counter+1)
        saida += str(lista[x])[y]
        y += counter+1
    lista.append((saida))

f = open("filename.txt",'w')
print >>f, lista
