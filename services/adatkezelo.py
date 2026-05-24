import csv

from models.legitarsasagok import Legitarsasag
from models.repterek import repterek
from models.jaratok import jaratok


class AdatKezelo:

    @staticmethod
    def legitarsasagok_beolvasasa(fajlnev):

        legitarsasagok = []

        with open(fajlnev, mode="r", encoding="utf-8") as fajl:

            olvaso = csv.DictReader(fajl)

            for sor in olvaso:

                legitarsasag = Legitarsasag(
                    sor["nev"],
                    sor["rovidites"],
                    sor["hasznalt_gepek"]
                )

                legitarsasagok.append(legitarsasag)

        return legitarsasagok

    @staticmethod
    def repterek_beolvasasa(fajlnev):

        repterek = []

        with open(fajlnev, mode="r", encoding="utf-8") as fajl:
             
             olvaso = csv.DictReader(fajl)

            for sor in olvaso:

                repterek = repterek(
                    sor["repter_azonosíto"],
                    sor["orszag"],
                    sor["varos"],
                    sor["repter_nev"]
                )

                repterek.append(repterek)
        return repterek
    
    @staticmethod
    def celallomasok_beolvasasa(fajlnev):

        celallomasok = []

        with open(fajlnev, mode="r", encoding="utf-8") as fajl:
             
             olvaso = csv.DictReader(fajl)

            for sor in olvaso:

                jaratok = jaratok(
                    sor["jaratszam"],
                    sor["legitarsasag"],
                    sor["indulasi_ido"],
                    sor["indulasi_hely"],
                    sor["celallomas"],
                    sor["jegyar"]
                )

                jaratok.append(jaratok)
        return celallomasok