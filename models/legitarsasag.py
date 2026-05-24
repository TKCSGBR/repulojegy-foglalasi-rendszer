class Legitarsasag:

    def __init__(self, nev, rovidites, hasznalt_gepek):
        self.__nev = nev
        self.__rovidites = rovidites
        self.__hasznalt_gepek = hasznalt_gepek

    @property
    def nev(self):
        return self.__nev

    @property
    def rovidites(self):
        return self.__rovidites

    @property
    def hasznalt_gepek(self):
        return self.__hasznalt_gepek
    
    def __str__(self):
        return (
            f"{self.__nev} "
            f"({self.__rovidites}) - "
            f"Gépek: {self.__hasznalt_gepek}"
        )