um, dois, tres = map(int, raw_input().split())
if(dois < um):
    temp = dois
    dois = um
    um = temp

if(tres < dois):
    temp = tres
    tres = dois
    dois = temp

if(dois < um):
    temp = dois
    dois = um
    um = temp

larguraLivre = 0

if(um > 0):
    larguraLivre += um

if(um+200 < dois):
    larguraLivre += (dois - (um+200))

if(dois+200 < tres):
    larguraLivre += (tres - (dois+200))

if(tres+200 != 600):
    larguraLivre += (600-(tres+200))

print larguraLivre*100
