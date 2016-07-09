while True:
    one, two = map(str, raw_input().split())
    if((one == "0" and two == "0")):
        break
    while True:
        if((len(one) == 1 and len(two) == 1)):
            break
        if(len(one) > 1):
            temp = 0
            for x in xrange(len(one)):
                temp += (int(one[x]))
            one = str(temp)


        if(len(two) > 1):
            temp = 0
            for x in xrange(len(two)):
                temp += (int(two[x]))
            two = str(temp)
    if(int(one) > int(two)):
        print "1"
    elif(int(one) < int(two)):
        print "2"
    else:
        print 0

