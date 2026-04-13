# Aprēķini savu daļu no restorāna rēķina
# Datu tipi, operācijas, tipu pārveidošana, atgrieztā vērtība

def puse(rekins, dzeramnauda):
    # TODO: Pabeidziet funkciju
    return 0.0


def main():
    """Galvenā programmas funkcija."""
    rekins = float(input("Rēķins pirms dzeramnaudas: "))    
    dzeramnaudas_procenti = int(input("Dzeramnaudas procenti: "))

    print(f"Jums katram būs jāmaksā € {puse(rekins, dzeramnaudas_procenti):.2f}!")


# Šis nosacījums palaiž `main` funkciju, kad skripts tiek izpildīts.
if __name__ == "__main__":
    main()