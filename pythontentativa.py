numeroum, numerodois = map(int, raw_input().split())

if((numeroum == 0)|(numerodois == 0)):
   print "Sao Multiplos"
elif((numerodois%numeroum == 0) |(numeroum % numerodois == 0)):
    print "Sao Multiplos"
else:
    print "Nao sao Multiplos"
