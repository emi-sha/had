from random import randrange

# Začáteční pozice hada (1 segment)
souradnice = [(0, 0)]  
# Začáteční pozice ovoce
seznam_ovoce = [(randrange(20), randrange(20))]
counter = 1

# Funkce pro vykreslení mapy
def nakresli_mapu(zmena, ovoce):
    seznam = []
    for i in range(20):
        podseznam = []
        for j in range(20):
            podseznam.append('.')
        seznam.append(podseznam)
    
    # Vykreslení hada (X)
    for k in zmena:
        seznam[k[1]][k[0]] = 'X'
    
    # Vykreslení ovoce (?)
    for m in ovoce:
        seznam[m[1]][m[0]] = '?'
    
    # Vytisknutí mapy
    for l in seznam:
        print(' '.join(l))

# Funkce pro pohyb hada
def pohyb(souradnice, smer, counter):
    posledni_souradnice = souradnice[-1]
    
    if smer == 'w':  # nahoru
        nova_souradnice = (posledni_souradnice[0], posledni_souradnice[1] - 1)
    elif smer == 'a':  # doleva
        nova_souradnice = (posledni_souradnice[0] - 1, posledni_souradnice[1])
    elif smer == 's':  # dolů
        nova_souradnice = (posledni_souradnice[0], posledni_souradnice[1] + 1)
    else:  # doprava
        nova_souradnice = (posledni_souradnice[0] + 1, posledni_souradnice[1])

    # Kontrola okrajů mapy
    if nova_souradnice[0] < 0 or nova_souradnice[0] >= 20 or nova_souradnice[1] < 0 or nova_souradnice[1] >= 20:
        raise ValueError('Had došel na kraj mapy. Dál už nemůže. Game over.')
    elif nova_souradnice in souradnice:
        raise ValueError('Sem had nemůže. Tam už stojí. Game over.')
    else:
        souradnice.append(nova_souradnice)
        
        # Pokud had sežral ovoce
        if nova_souradnice in seznam_ovoce:
            seznam_ovoce.remove(nova_souradnice)
            ovoce_x, ovoce_y = randrange(20), randrange(20)
            while (ovoce_x, ovoce_y) in souradnice:  # Opakuje, dokud se ovoce neobjeví na volném místě
                ovoce_x, ovoce_y = randrange(20), randrange(20)
            seznam_ovoce.append((ovoce_x, ovoce_y))
        else:
            souradnice.pop(0)  # Odstraní první segment, aby had zůstal stejně dlouhý

    # Po 30 krocích přidat nové ovoce
    if counter == 30:
        ovoce_x, ovoce_y = randrange(20), randrange(20)
        while (ovoce_x, ovoce_y) in souradnice:  # Opakuje, dokud se ovoce neobjeví na volném místě
            ovoce_x, ovoce_y = randrange(20), randrange(20)
        seznam_ovoce.append((ovoce_x, ovoce_y))
        counter = 1
    else:
        counter += 1

    return counter

# Hlavní smyčka hry
while True:
    try:
        smer = input('Zadej směr (w - nahoru, a - doleva, s - dolů, d - doprava): ')
        counter = pohyb(souradnice, smer, counter)
        nakresli_mapu(souradnice, seznam_ovoce)    
    except ValueError as chyba:
        print(chyba)
        break
