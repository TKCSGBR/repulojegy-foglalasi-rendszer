class Celallomas:

    def __init__(
        self,
        orszag,
        varos,
        repter_nev,
        hasznalt_repulogepek
    ):

        self.__orszag = orszag
        self.__varos = varos
        self.__repter_nev = repter_nev
        self.__hasznalt_repulogepek = hasznalt_repulogepek

    @property
    def orszag(self):
        return self.__orszag

    @property
    def varos(self):
        return self.__varos

    @property
    def repter_nev(self):
        return self.__repter_nev

    @property
    def hasznalt_repulogepek(self):
        return self.__hasznalt_repulogepek

    def __str__(self):
        return (
            f"{self.__varos}, {self.__orszag} - "
            f"{self.__repter_nev}"
        )