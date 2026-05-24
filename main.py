from services.adatkezelo import AdatKezelo


def main():

    legitarsasagok = AdatKezelo.legitarsasagok_beolvasasa(
        "data/legitarsasagok.csv"
    )

    celallomasok = AdatKezelo.celallomasok_beolvasasa(
        "data/repterek.csv"
    )
    
    jaratok = AdatKezelo.jaratok_beolvasasa(
        "data/jaratok.csv"
    )

    print("\n--- Légitársaságok ---")

    for legitarsasag in legitarsasagok:
        print(legitarsasag)

    print("\n--- Repterek ---")

    for repterek in repterek:
        print(repterek)
        
    print("\n--- Jaratok ---")

    for jaratok in jaratok:
        print(jaratok)


if __name__ == "__main__":
    main()