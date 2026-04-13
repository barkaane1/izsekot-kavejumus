# koordinates.py

# 1. TODO: Izveidojiet vārdnīcu `pilsetu_koordinates`.
# Atslēgām jābūt pilsētu nosaukumiem (piem., "Rīga", "Ventspils").
# Vērtībām jābūt kortežiem ar diviem skaitļiem (platums, garums).
# Pievienojiet vārdnīcai vismaz 3 Latvijas pilsētas.
# Dati iedvesmai:
# Rīga: (56.9496, 24.1052)
# Liepāja: (56.5110, 21.0135)
# Daugavpils: (55.8747, 26.5359)
# Citu pilsētu koordinātes meklē balticmaps.eu vai Google Maps
pilsetu_koordinates = {}


# 2. TODO: Papildiniet programmu, lai tā lūdz lietotājam ievadīt pilsētas nosaukumu.
# Atrodiet ievadītās pilsētas koordinātas vārdnīcā un izdrukājiet tās.
# Izmantojiet .get() metodi, lai izvairītos no kļūdas, ja pilsēta nav atrasta.
# Ja pilsēta ir atrasta, izdrukājiet tās koordinātas; ja nav - atbilstošu paziņojumu.
meklejamais_nosaukums = input("Ievadiet pilsētas nosaukumu: ")