from abc import ABC


class Jarat(ABC):

    def __init__(
        self,
        jaratszam,
        indulasi_ido,
        legitarsasag_rovidites,
        indulasi_hely,
        celallomas,
        jegyar
    ):

        self.__jaratszam = jaratszam
        self.__indulasi_ido = indulasi_ido
        self.__legitarsasag_rovidites = legitarsasag_rovidites
        self.__indulasi_hely = indulasi_hely
        self.__celallomas = celallomas
        self.__jegyar = jegyar

    @property
    def jaratszam(self):
        return self.__jaratszam

    @property
    def indulasi_ido(self):
        return self.__indulasi_ido
    
    @property
    def legitarsasag_rovidites(self):
        return self.__legitarsasag_rovidites

    @property
    def indulasi_hely(self):
        return self.__indulasi_hely

    @property
    def celallomas(self):
        return self.__celallomas

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
            f"Indulási idő: {self.__indulasi_ido}\n"
            f"Légitársaság: {self.__legitarsasag_rovidites}\n"
            f"Indulás: {self.__indulasi_hely}\n"
            f"Célállomás: {self.__celallomas}\n"
            f"Jegyár: {self.__jegyar} Ft\n"
        )