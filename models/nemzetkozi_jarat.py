from models.jarat import Jarat


class NemzetkoziJarat(Jarat):

    def __init__(self, jaratszam, celallomas):
        super().__init__(jaratszam, celallomas, 65000)