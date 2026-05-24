from datetime import datetime

from models.belfoldi_jarat import BelfoldiJarat
from models.nemzetkozi_jarat import NemzetkoziJarat
from models.legitarsasag import Legitarsasag
from models.jegy_foglalas import JegyFoglalas


class FoglalasiRendszer:

    def __init__(self):

        self.__foglalasok = []

        self.__legitarsasag = Legitarsasag("Python Air")

        self.__legitarsasag.jarat_hozzaadas(
            BelfoldiJarat("B101", "Debrecen")
        )

        self.__legitarsasag.jarat_hozzaadas(
            BelfoldiJarat("B102", "Pécs")
        )

        self.__legitarsasag.jarat_hozzaadas(
            NemzetkoziJarat("N201", "London")
        )

    def jaratok_listazasa(self):

        print("\n--- Elérhető járatok ---")

        self.__legitarsasag.jaratok_listazasa()

    def jegy_foglalas(self):

        try:

            self.jaratok_listazasa()

            jaratszam = input("\nAdd meg a járatszámot: ")
            utas_nev = input("Add meg a neved: ")
            datum = input("Add meg a dátumot (ÉÉÉÉ-HH-NN): ")

            datum_obj = datetime.strptime(datum, "%Y-%m-%d")

            if datum_obj < datetime.now():
                raise ValueError("A dátum nem lehet múltbeli!")

            kivalasztott_jarat = None

            for jarat in self.__legitarsasag.jaratok:

                if jarat.jaratszam == jaratszam:
                    kivalasztott_jarat = jarat
                    break

            if kivalasztott_jarat is None:
                raise ValueError("Nincs ilyen járat!")

            foglalas = JegyFoglalas(
                utas_nev,
                kivalasztott_jarat,
                datum
            )

            self.__foglalasok.append(foglalas)

            print(
                f"\nSikeres foglalás!"
                f"\nÁr: {kivalasztott_jarat.jegyar} Ft"
            )

        except ValueError as hiba:
            print(f"Hiba: {hiba}")

    def foglalasok_listazasa(self):

        print("\n--- Aktív foglalások ---")

        if not self.__foglalasok:
            print("Nincs foglalás.")
            return

        for foglalas in self.__foglalasok:
            print(foglalas)

    def foglalas_lemondasa(self):

        try:

            foglalasi_id = int(
                input("Add meg a foglalási azonosítót: ")
            )

            for foglalas in self.__foglalasok:

                if foglalas.foglalasi_id == foglalasi_id:

                    self.__foglalasok.remove(foglalas)

                    print("Foglalás sikeresen törölve.")
                    return

            raise ValueError("Nincs ilyen foglalás!")

        except ValueError as hiba:
            print(f"Hiba: {hiba}")

    def menu(self):

        while True:

            print("\n=== Repülőjegy Foglalási Rendszer ===")
            print("1 - Járatok listázása")
            print("2 - Jegy foglalása")
            print("3 - Foglalás lemondása")
            print("4 - Foglalások listázása")
            print("0 - Kilépés")

            valasztas = input("Választás: ")

            if valasztas == "1":
                self.jaratok_listazasa()

            elif valasztas == "2":
                self.jegy_foglalas()

            elif valasztas == "3":
                self.foglalas_lemondasa()

            elif valasztas == "4":
                self.foglalasok_listazasa()

            elif valasztas == "0":
                print("Kilépés...")
                break

            else:
                print("Érvénytelen menüpont!")