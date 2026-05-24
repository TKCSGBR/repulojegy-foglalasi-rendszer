from models.jegy_foglalas import JegyFoglalas


class FoglalasiRendszer:
   
    def __init__(self):

        self.__foglalasok = []
    @property
    def foglalasok(self):
        return self.__foglalasok
    
    def foglalas_letrehozasa(
        self,
        foglalas_id,
        utas_nev,
        jarat
    ):

        uj_foglalas = JegyFoglalas(
            foglalas_id,
            utas_nev,
            jarat
        )

        self.__foglalasok.append(uj_foglalas)

        return jarat.jegyar

    def foglalas_lemondasa(self, foglalas_id):

        for foglalas in self.__foglalasok:

            if foglalas.foglalas_id == foglalas_id:

                self.__foglalasok.remove(foglalas)

                return True

        raise ValueError(
            "Nincs ilyen foglalás!"
        )

    def foglalasok_listazasa(self):

        if not self.__foglalasok:

            print("Nincs aktív foglalás.")
            return

        for foglalas in self.__foglalasok:
            print(foglalas)