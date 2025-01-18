from random import randrange

souradnice = [(0, 0), (1, 0), (2, 0)]
seznam_ovoce = [(2,3)]
counter = 1

def nakresli_mapu(zmena, ovoce):
    seznam = []
    for i in range(10):
        podseznam = []
        for j in range(10):
            podseznam.append('.')
        seznam.append(podseznam)
    for k in zmena:
        seznam[k[1]][k[0]] = 'X'
    for m in ovoce:
        seznam[m[1]][m[0]] = '?'
    for l in seznam:
        print(' '.join(l))

def pohyb(souradnice, svetova_strana, counter):
    posledni_souradnice = souradnice[-1]
    if svetova_strana == 'j':
        nova_souradnice = (posledni_souradnice[0], posledni_souradnice[1] + 1)
    elif svetova_strana == 'z':
        nova_souradnice = (posledni_souradnice[0] - 1, posledni_souradnice[1])
    elif svetova_strana == 's':
        nova_souradnice = (posledni_souradnice[0], posledni_souradnice[1] - 1)
    else:
        nova_souradnice = (posledni_souradnice[0] + 1, posledni_souradnice[1])

    if nova_souradnice[0] < 0 or nova_souradnice[0] >= 10 or nova_souradnice[1] < 0 or nova_souradnice[1] >= 10:
        raise ValueError('Had došel na kraj mapy. Dál už nemůže.Game over.')
    elif nova_souradnice in souradnice:
        raise ValueError('Sem had nemůže. Tam už stojí. Game over.')
    else:
        souradnice.append(nova_souradnice)
        if nova_souradnice in seznam_ovoce:
            seznam_ovoce.remove(nova_souradnice)
            seznam_ovoce.append((randrange(0,10),randrange(0,10)))
            print(seznam_ovoce)
        else: souradnice.pop(0)
    if counter == 30:
        seznam_ovoce.append((randrange(0,10),randrange(0,10)))
        counter = 1
    else:
        counter = counter + 1
    return counter

while True:
    try:
        svetova_strana = input('Zadej světovou stranu: j, v, z nebo s.')
        counter = pohyb(souradnice, svetova_strana, counter)
        nakresli_mapu(souradnice, seznam_ovoce)    
    except ValueError as chyba:
        print(chyba)