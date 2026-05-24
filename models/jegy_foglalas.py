from datetime import datetime


class JegyFoglalas:

    def __init__(self, utas_nev, jarat, datum):
        self.__utas_nev = utas_nev
        self.__jarat = jarat
        self.__datum = datum
        self.__foglalasi_id = id(self)

    @property
    def foglalasi_id(self):
        return self.__foglalasi_id

    @property
    def datum(self):
        return self.__datum

    @property
    def jarat(self):
        return self.__jarat

    def __str__(self):
        return (
            f"Foglalás ID: {self.__foglalasi_id} | "
            f"Név: {self.__utas_nev} | "
            f"Járat: {self.__jarat.jaratszam} | "
            f"Cél: {self.__jarat.celallomas} | "
            f"Dátum: {self.__datum}"
        )