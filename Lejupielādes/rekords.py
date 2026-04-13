import random

def atrast_augstako_rezultatu(rezultatu_saraksts):
    """
    Atrod un atgriež lielāko skaitli dotajā sarakstā.
    Piemēram: ja saraksts ir [1.65, 1.78, 1.72], funkcijai jāatgriež 1.78.
    
    TODO: Izveido algoritmu, kas atrod lielāko elementu.
    """
    # Pārbaude, vai saraksts nav tukšs
    if not rezultatu_saraksts:
        return None # Atgriežam None, ja nav rezultātu
        
    # Šeit raksti savu kodu
    pass


def main():
    """Galvenā funkcija programmas darbināšanai."""
    # Ģenerē 10 nejaušus rezultātus no 1.50 līdz 2.10 metriem
    rezultati = [round(random.uniform(1.50, 2.10), 2) for _ in range(10)]
    
    print(f"Sacensību rezultāti: {rezultati}")
    
    augstakais_rezultats = atrast_augstako_rezultatu(rezultati)
    
    if augstakais_rezultats is not None:
        print(f"Labākais sasniegtais rezultāts: {augstakais_rezultats} m")
    else:
        print("Rezultātu saraksts ir tukšs.")


if __name__ == "__main__":
    main()