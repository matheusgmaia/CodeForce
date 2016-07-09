quant = int(raw_input())
numeros = map(int, raw_input().split())

somas = range(quant)
soma = 0

for x in range(0,quant):
    somas[x] = soma + numeros[x]
    soma += numeros[x]
count = 0


for x in range(0,quant-1):
    if(somas[x] == somas[quant-1] - somas[x]):
        count += 1

print count
