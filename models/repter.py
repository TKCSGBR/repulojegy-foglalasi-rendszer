class Repter:

    def __init__(
        self,
        repter_azonosito,
        orszag,
        varos,
        repter_nev
    ):

        self.__repter_azonosito = repter_azonosito
        self.__orszag = orszag
        self.__varos = varos
        self.__repter_nev = repter_nev

    @property
    def repter_azonosito(self):
        return self.__repter_azonosito

    @property
    def orszag(self):
        return self.__orszag

    @property
    def varos(self):
        return self.__varos

    @property
    def repter_nev(self):
        return self.__repter_nev

    def __str__(self):

        return (
            f"{self.__repter_nev} "
            f"({self.__varos}, {self.__orszag})"
        )