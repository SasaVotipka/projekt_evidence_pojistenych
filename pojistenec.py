class Pojistenec:

    def __init__(self, jmeno, prijmeni, vek, tel_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.tel_cislo = tel_cislo

    def __str__(self):
        # Vrátí pojištence jako zformátovaný řádek tabulky
    
        return "{:<15} {:<15} {:<15} {:<10}".format(self.jmeno, self.prijmeni, self.tel_cislo, self.vek)    
