def pirmskaitlis(skaitlis):
    """Pārbauda, vai skaitlis ir pirmskaitlis."""
    # TODO: Pabeidziet funkcijas loģiku
    return False


def main():
    """Galvenā programmas funkcija, kas atrod pirmskaitļus norādītajā diapazonā."""
    # Pieprasa minimālo robežu, nodrošinot, ka tā ir vismaz 1
    while True:
        try:
            min_vertiba = int(input("Minimums: "))
            if min_vertiba >= 1:
                break
        except ValueError:
            print("Lūdzu, ievadiet derīgu veselu skaitli.")

    # Pieprasa maksimālo robežu, nodrošinot, ka tā ir lielāka par minimālo
    while True:
        try:
            max_vertiba = int(input("Maksimums: "))
            if max_vertiba > min_vertiba:
                break
        except ValueError:
            print("Lūdzu, ievadiet derīgu veselu skaitli.")
            
    # Iterē cauri visiem skaitļiem no min_vertiba līdz max_vertiba (ieskaitot)
    for i in range(min_vertiba, max_vertiba + 1):
        if pirmskaitlis(i):
            print(i)


# Šis nosacījums palaiž `main` funkciju, kad skripts tiek izpildīts.
if __name__ == "__main__":
    main()