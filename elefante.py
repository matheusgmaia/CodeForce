distancia = int(raw_input())

passos = [5,4,3,2,1]
count = 0
while(distancia != 0):
    for x in passos:
        while(distancia - x >= 0):
            distancia = distancia - x
            count += 1

print count
            
