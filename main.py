from services.adatkezelo import AdatKezelo


def main():

    legitarsasagok = AdatKezelo.legitarsasagok_beolvasasa(
        "data/legitarsasagok.csv"
    )

    repterek = AdatKezelo.repterek_beolvasasa(
        "data/repterek.csv"
    )
    
    jaratok = AdatKezelo.jaratok_beolvasasa(
        "data/jaratok.csv"
    )

    print("\n--- Légitársaságok ---")

    for legitarsasagok in legitarsasagok:
        print(legitarsasagok)

    print("\n--- Repterek ---")

    for repterek in repterek:
        print(repterek)
        
    print("\n--- Jaratok ---")

    for jaratok in jaratok:
        print(jaratok)


if __name__ == "__main__":
    main()