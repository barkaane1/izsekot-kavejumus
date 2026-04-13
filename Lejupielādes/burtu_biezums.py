def skaitit_burtus(teksts):
    """
    Saskaita burtu biežumu tekstā un atgriež rezultātu vārdnīcas formātā.
    """
    # TODO: Tavs kods šeit
    pass

def main():
    teksts = input("Ievadi jebkādu tekstu")
    burtu_analize = skaitit_burtus(teksts)
    if burtu_analize:
        for burts, skaits in burtu_analize.items():
            print(f"{burts} - {skaits}")
    else:
        print("Nav ko saskaitīt, vai funkcija skaitit_burtus nav atgriezusi prasīto vārdnīcu.")
        
if __name__ == "__main__":
    main()