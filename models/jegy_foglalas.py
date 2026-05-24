class JegyFoglalas:

    def __init__(
        self,
        foglalas_id,
        utas_nev,
        jarat
    ):

        self.__foglalas_id = foglalas_id
        self.__utas_nev = utas_nev
        self.__jarat = jarat

    @property
    def foglalas_id(self):
        return self.__foglalas_id

    @property
    def utas_nev(self):
        return self.__utas_nev

    @property
    def jarat(self):
        return self.__jarat

    def __str__(self):

        return (
            f"Foglalás ID: {self.__foglalas_id} | "
            f"Utas: {self.__utas_nev} | "
            f"Járat: {self.__jarat.jaratszam}"
        )