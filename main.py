from services.adatkezelo import AdatKezelo
from services.foglalasi_rendszer import FoglalasiRendszer
from datetime import datetime

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

    foglalasi_rendszer = FoglalasiRendszer()
    foglalasi_rendszer.foglalasok_betoltese(jaratok)  
    
    print("\n--- Légitársaságok ---")

    for legitarsasag in legitarsasagok:
        print(legitarsasag)

    print("\n--- Repterek ---")

    for repter in repterek:
        print(repter)

    print("\n--- Járatok ---")

    for jarat in jaratok:
        print(jarat)

    while True:

        print("\n===== MENÜ =====")
        print("1 - Jegy foglalása")
        print("2 - Foglalás lemondása")
        print("3 - Foglalások listázása")
        print("0 - Kilépés")

        valasztas = input("Választás: ")

        # JEGY FOGLALÁS
        if valasztas == "1":

            try:

                utas_nev = input("Utas neve: ")
                keresett_jarat = input("Járatszám: ")
                kivalasztott_jarat = None
              
                for jarat in jaratok:

                    if jarat.jaratszam == keresett_jarat:
                        kivalasztott_jarat = jarat
                        break

                if kivalasztott_jarat is None:
                    raise ValueError("Nincs ilyen járat! Inni, érdemes az utazás megkezdése után. Mértékkel.")
                
                indulasi_datum = datetime.strptime(
                    kivalasztott_jarat.indulasi_ido, "%Y.%m.%d"
                )
                if indulasi_datum < datetime.now():
                    raise ValueError("Ez a járat már régmúlt, és bár megértjük, hogy akkor akarnál utazni, mikor még olcsó volt, de sajnos már nem lehet rá foglalni!")
                
                foglalas_id = len(
                    foglalasi_rendszer.foglalasok
                ) + 1

                ar = foglalasi_rendszer.foglalas_letrehozasa(
                    foglalas_id,
                    utas_nev,
                    kivalasztott_jarat
                )

                print(f"\nSikeres foglalás!")

                print( f"Fizetendő: {ar} Ft")

            except ValueError as e:
                print(f"Hiba: {e}")
        # LEMONDÁS
        elif valasztas == "2":

            try:

                foglalas_id = int(
                    input("Foglalás ID: ")
                )
            except ValueError:
                print("Hiba: Az azonosító csak szám lehet!")
                continue
            
            try:        
                if foglalas_id not in [f.foglalas_id for f in foglalasi_rendszer.foglalasok]:
                    raise ValueError("Nincs ilyen foglalás")
                foglalas = next(f for f in foglalasi_rendszer.foglalasok if f.foglalas_id == foglalas_id)
                
                indulasi_datum = datetime.strptime(
                    foglalas.jarat.indulasi_ido, "%Y.%m.%d"
                )
                if indulasi_datum < datetime.now():
                    raise ValueError("Múltbéli járatra vonatkozó foglalást nem lehet törölni!")

                foglalasi_rendszer.foglalas_lemondasa(
                    foglalas_id
                )
                
                print(
                    "Foglalás törölve."
                )
            except ValueError as e:
                print(f"Hiba: {e}")
            

        # LISTÁZÁS
        elif valasztas == "3":

            foglalasi_rendszer.foglalasok_listazasa()

        # KILÉPÉS
        elif valasztas == "0":

            print("Kilépés...")
            break

        else:
            print("Érvénytelen menüpont!")


if __name__ == "__main__":
    main()