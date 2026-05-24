from abc import ABC


class Jarat(ABC):

    def __init__(
        self,
        jaratszam,
        legitarsasag,
        indulasi_repter,
        cel_repter,
        jegyar
    ):

        self.__jaratszam = jaratszam
        self.__legitarsasag = legitarsasag
        self.__indulasi_repter = indulasi_repter
        self.__cel_repter = cel_repter
        self.__jegyar = jegyar

    @property
    def jaratszam(self):
        return self.__jaratszam

    @property
    def legitarsasag(self):
        return self.__legitarsasag

    @property
    def indulasi_repter(self):
        return self.__indulasi_repter

    @property
    def cel_repter(self):
        return self.__cel_repter

    @property
    def jegyar(self):
        return self.__jegyar

    @jegyar.setter
    def jegyar(self, uj_ar):

        if uj_ar <= 0:
            raise ValueError("A jegyár nem lehet negatív vagy 0.")

        self.__jegyar = uj_ar

    def __str__(self):

        return (
            f"\nJáratszám: {self.__jaratszam}\n"
            f"Légitársaság: {self.__legitarsasag.nev}\n"
            f"Indulás: {self.__indulasi_repter.repter_nev}\n"
            f"Célállomás: {self.__cel_repter.repter_nev}\n"
            f"Jegyár: {self.__jegyar} Ft\n"
        )