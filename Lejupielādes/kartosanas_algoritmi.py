import time
import random
import sys

# Palielinām rekursijas limitu, lai sapludināšanas kārtošana strādātu ar lieliem sarakstiem
sys.setrecursionlimit(20000)

# ===================================================================================
# TRĪS KĀRTOŠANAS METODES
# TAVS UZDEVUMS: Noskaidrot, kura ir kura (burbuļkārtošana, atlases kārtošana, sapludināšanas kārtošana)
# ===================================================================================

def kartosanas_metode_A(saraksts):
    """
    Pievērs uzmanību tam, kā šī funkcija izsauc pati sevi,
    lai sadalītu problēmu mazākās daļās.
    """
    if len(saraksts) > 1:
        videjais_indekss = len(saraksts) // 2
        kreisa_puse = saraksts[:videjais_indekss]
        laba_puse = saraksts[videjais_indekss:]

        kreisa_puse = kartosanas_metode_A(kreisa_puse)
        laba_puse = kartosanas_metode_A(laba_puse)

        i = j = k = 0
        while i < len(kreisa_puse) and j < len(laba_puse):
            if kreisa_puse[i] < laba_puse[j]:
                saraksts[k] = kreisa_puse[i]
                i += 1
            else:
                saraksts[k] = laba_puse[j]
                j += 1
            k += 1

        while i < len(kreisa_puse):
            saraksts[k] = kreisa_puse[i]
            i += 1
            k += 1

        while j < len(laba_puse):
            saraksts[k] = laba_puse[j]
            j += 1
            k += 1
    return saraksts


def kartosanas_metode_B(saraksts):
    """
    Analizē iekšējo ciklu – kuri elementi tiek salīdzināti un mainīti vietām?
    Šīs metodes efektivitāte ir ļoti atkarīga no sākuma secības.
    """
    n = len(saraksts)
    cik_kartots = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if saraksts[j] > saraksts[j+1]:
                saraksts[j], saraksts[j+1] = saraksts[j+1], saraksts[j]
                cik_kartots += 1
        if cik_kartots == 0:
            break
    return saraksts


def kartosanas_metode_C(saraksts):
    """
    Pēti, kāda loma šajā algoritmā ir mainīgajam 'min_indekss'
    un kāpēc apmaiņa notiek tikai vienu reizi ārējā cikla ietvaros.
    """
    n = len(saraksts)
    for i in range(n):
        min_indekss = i
        for j in range(i+1, n):
            if saraksts[j] < saraksts[min_indekss]:
                min_indekss = j
        saraksts[i], saraksts[min_indekss] = saraksts[min_indekss], saraksts[i]
    return saraksts

# ===================================================================================
# TESTĒŠANAS VIDE
# ===================================================================================

def main():
    saraksta_izmers = 1000  # Maini, ja vēlies testēt ar mazāku/lielāku skaitu (piem., 10000)
    
    # Datu sagatavošana
    print(f"Tiek ģenerēti saraksti ar {saraksta_izmers} elementiem...")
    jaukts_saraksts = [random.randint(1, saraksta_izmers) for _ in range(saraksta_izmers)]
    apgriezts_saraksts = list(range(saraksta_izmers, 0, -1))
    sakartots_saraksts = list(range(saraksta_izmers))

    testejamie_dati = {
        "Jaukts saraksts": jaukts_saraksts,
        "Apgriezts saraksts": apgriezts_saraksts,
        "Jau sakārtots saraksts": sakartots_saraksts
    }

    metodes = {
        "Metode A": kartosanas_metode_A,
        "Metode B": kartosanas_metode_B,
        "Metode C": kartosanas_metode_C
    }

    print("-" * 40)
    # Testēšanas cikls
    for datu_nosaukums, dati in testejamie_dati.items():
        print(f"\nTESTĒŠANA AR DATU TIPU: '{datu_nosaukums}'")
        for metodes_nosaukums, metode in metodes.items():
            # Izveidojam kopiju, lai katra metode strādātu ar identiskiem sākuma datiem
            datu_kopija = dati[:]
            
            start_time = time.time()
            metode(datu_kopija) # Palaižam kārtošanu
            end_time = time.time()
            
            izpildes_laiks = end_time - start_time
            print(f"  - {metodes_nosaukums}: {izpildes_laiks:.4f} sekundes")
    print("-" * 40)


if __name__ == "__main__":
    main()