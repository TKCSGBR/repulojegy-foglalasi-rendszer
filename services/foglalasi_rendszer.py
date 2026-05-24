import json
import os
from models.jegy_foglalas import JegyFoglalas

FOGLALASOK_FAJL = "data/foglalasok.json"

class FoglalasiRendszer:

    def __init__(self):
        self.__foglalasok = []

    @property
    def foglalasok(self):
        return self.__foglalasok

    def foglalasok_betoltese(self, jaratok):
        """Betölti a foglalásokat JSON fájlból."""
        if not os.path.exists(FOGLALASOK_FAJL):
            return
        with open(FOGLALASOK_FAJL, "r", encoding="utf-8") as f:
            adatok = json.load(f)
        for adat in adatok:
            jarat = next(
                (j for j in jaratok if j.jaratszam == adat["jaratszam"]),
                None
            )
            if jarat is None:
                print(f"Figyelem: a '{adat['jaratszam']}' járat nem található, foglalás kihagyva.")
                continue
            foglalas = JegyFoglalas(
                adat["foglalas_id"],
                adat["utas_nev"],
                jarat
            )
            self.__foglalasok.append(foglalas)

    def __foglalasok_mentese(self):
        """Elmenti az összes foglalást JSON fájlba."""
        adatok = [
            {
                "foglalas_id": f.foglalas_id,
                "utas_nev": f.utas_nev,
                "jaratszam": f.jarat.jaratszam
            }
            for f in self.__foglalasok
        ]
        with open(FOGLALASOK_FAJL, "w", encoding="utf-8") as fajl:
            json.dump(adatok, fajl, ensure_ascii=False, indent=2)

    def foglalas_letrehozasa(self, foglalas_id, utas_nev, jarat):
        uj_foglalas = JegyFoglalas(foglalas_id, utas_nev, jarat)
        self.__foglalasok.append(uj_foglalas)
        self.__foglalasok_mentese()
        return jarat.jegyar

    def foglalas_lemondasa(self, foglalas_id):
        for foglalas in self.__foglalasok:
            if foglalas.foglalas_id == foglalas_id:
                self.__foglalasok.remove(foglalas)
                self.__foglalasok_mentese()
                return True
        raise ValueError("Nincs ilyen foglalás!")

    def foglalasok_listazasa(self):
        if not self.__foglalasok:
            print("Nincs aktív foglalás.")
            return
        for foglalas in self.__foglalasok:
            print(foglalas)