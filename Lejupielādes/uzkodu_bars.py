# Šajā datnē ir jāpapildina divas funkcijas:
# 1. pievienot_produktus()
# 2. aprekinat_cenu()

# Pilns produktu saraksts iedvesmai:
# Burgeris: 9.50 €
# Vegāniskais burgeris: 11.00 €
# Hotdogs: 5.00 €
# Siera hotdogs: 7.00 €
# Frī kartupeļi: 5.00 €
# Siera frī kartupeļi: 6.00 €
# Svaigi spiesta sula: 7.00 €
# Aukstā kafija: 3.00 €
# Ūdens: 2.00 €
# Limonāde: 2.00 €

def pievienot_produktus():
    """
    Šai funkcijai ir jāatgriež ēdienkartes saraksts.
    Katrs saraksta elements ir vārdnīca (dict), kas satur produkta nosaukumu un cenu.
    Piemēram: {'nosaukums': 'Ūdens', 'cena': 2.00}
    TODO: Pievieno vismaz pirmos četrus produktus no saraksta.
    """
    edienkarte = [{"nosaukums" :"Burgeris" , "cena": 9.50} , { "nosaukums" : "Vegāniskais burgeris", "cena": 11.00 }, {"nosaukums" : "Hotdogs","cena" : 5.00}, {"nosaukums":"Siera hotdogs" , "cena": 7.00 }]

    # Šeit jāpievieno produkti sarakstam 'edienkarte'
    produkts = {"Burgeris" , "Vegāniskais burgeris" , "Hotdogs" ,"Siera hotdogs" }
    
    return edienkarte


def aprekinat_cenu(produkts, edienkarte):
    """
    Šai funkcijai ir jāatrod un jāatgriež produkta cena no ēdienkartes.
    Jāizmanto lineārā meklēšana, lai atrastu produktu sarakstā.
    Lineārā meklēšana – secīgi tiek pārbaudīts katrs datu struktūras elements, sākot no paša sākuma.
    Meklēšanai jābūt reģistrnejutīgai (case-insensitive).
    Ja produkts nav atrasts, jāatgriež 0.0.
    TODO: Realizē meklēšanas algoritmu.
    """
    produkts_lower = produkts.lower()
    for produkts in edienkarte:
        if produkts["nosaukums"].lower() == produkts_lower:  
            return produkts["cena"]
        else:
            return 0.0


def main():
    """
    Galvenā programmas daļa, kas apstrādā lietotāja ievadi un izvadi.
    Šī daļa jau ir pabeigta.
    """
    edienkarte = pievienot_produktus()

    print("\nLaipni lūgti pludmales uzkodu bārā!")
    print("Izvēlieties produktus no ēdienkartes. Kad pabeidzat, nospiediet Enter.\n")

    for produkts in edienkarte:
        print(f"{produkts['nosaukums']}: {produkts['cena']:.2f} €")
    
    print("\n")

    kopa = 0.0
    while True:
        ievade = input("Ievadiet produktu: ")
        if not ievade:
            print("\n")
            break
        
        kopa += aprekinat_cenu(ievade, edienkarte)

    print(f"Jūsu pasūtījuma kopējā cena: {kopa:.2f} €")


# Šī rinda nodrošina, ka main() funkcija tiek izsaukta tikai tad,
# kad fails tiek palaists tieši, nevis importēts.
if __name__ == "__main__":
    main()