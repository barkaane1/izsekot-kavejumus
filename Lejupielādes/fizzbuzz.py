def fizzbuzz_saraksts(n):
    """
    Izveido un atgriež sarakstu ar FizzBuzz virkni līdz skaitlim n ieskaitot.
    """
    # TODO: Jūsu kods šeit
    pass


def main():
    try:
        n = int(input("Ievadi veselu skaitli"))
        fzbzz = fizzbuzz_saraksts(n)
        print(fzbzz)
    except:
        print("Kaut kas nogāja greizi.")
        
if __name__ == "__main__":
    main()