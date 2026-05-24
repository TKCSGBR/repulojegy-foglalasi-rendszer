from models.jarat import Jarat


class BelfoldiJarat(Jarat):

    def __init__(self, jaratszam, celallomas):
        super().__init__(jaratszam, celallomas, 15000)