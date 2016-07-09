pessoas = 1
saida = ""
teste = 0
while(pessoas != 0):
    pessoas = int(raw_input())
    if(pessoas == 0):
        break
    teste += 1;
    entrada = map(int, raw_input().split())
    for i in entrada:
        if(i <= pessoas):
            if(entrada[i-1] == i):
                saida += ("Teste %d\n%d\n\n" % (teste,i))

print saida
