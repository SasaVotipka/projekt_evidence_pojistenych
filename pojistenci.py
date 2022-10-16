from pojistenec import Pojistenec


class Pojistenci: 
    def __init__(self):
        self.seznam_pojistencu = []
       
    def pridej_pojistence(self, jmeno, prijmeni, vek, tel_cislo):
        novy_pojistenec = Pojistenec(jmeno, prijmeni, vek, tel_cislo)
        self.seznam_pojistencu.append(novy_pojistenec)