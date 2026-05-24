import csv

from models.legitarsasag import Legitarsasag
from models.repter import Repter
from models.jarat import Jarat


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

                repter = Repter(
                    sor["repter_azonosito"],
                    sor["orszag"],
                    sor["varos"],
                    sor["repter_nev"]
                )

                repterek.append(repter)

        return repterek
    
    @staticmethod
    def jaratok_beolvasasa(fajlnev):

        jaratok = []

        with open(fajlnev, mode="r", encoding="utf-8") as fajl:

            olvaso = csv.DictReader(fajl)

            for sor in olvaso:

                jarat = Jarat(
                    sor["jaratszam"],
                    sor["indulasi_ido"],
                    sor["legitarsasag_rovidites"],
                    sor["indulasi_hely"],
                    sor["celallomas"],
                    sor["jegyar"]
                )

                jaratok.append(jarat)

        return jaratok