def kartosana(saraksts):
    # Ārējais cikls iet cauri sarakstam, sākot no otrā elementa
    for i in range(1, len(saraksts)):
        
        ievietosanas_indekss = i
        
        # TODO 1: Paskaidro, ko dara šī koda rinda.
        pasreizeja_vertiba = saraksts.pop(i)
        
        # Iekšējais cikls meklē pareizo vietu sakārtotajā daļā
        for j in range(i - 1, -1, -1):
            if saraksts[j] > pasreizeja_vertiba:
                ievietosanas_indekss = j
        
        # TODO 2: Paskaidro, kas notiek šajā rindā.
        saraksts.insert(ievietosanas_indekss, pasreizeja_vertiba)
        
    return saraksts

saraksts = [4, 1, 3, 2, 3, 9, 0, -1, 6]
sakartots = kartosana(saraksts)
print(sakartots)
