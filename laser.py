height = 1
lenght = 1
counter = 0
saida = ""
while True:
    height, lenght = map(int, raw_input().split())
    if(height == 0 and lenght == 0):
        break
    heights = map(int, raw_input().split())

    maior = heights[0]
    for x in xrange(0,(len(heights)-1)):
        if (heights[x+1] > maior and heights[x] <= maior):

            counter += abs(heights[x+1] - maior)
            maior = heights[x+1]
        elif(heights[x+1] < maior and heights[x] > heights[x+1]):
            counter += abs(heights[x] - heights[x+1])
    counter += (height - maior)
    saida += "%d\n" % counter
    counter = 0


print saida[:-1]
