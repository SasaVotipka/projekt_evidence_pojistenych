import sys
import vypisy
from pojistenci import Pojistenci

class Akce:

    def __init__(self):
         self.pojistenci = Pojistenci()


    def __str__(self):
        return "\nVyberte si akci:\n1 - Přidat nového pojištěného \n2 - Vypsat všechny pojištěné \n3 - Vyhledat pojištěného \n4 - Konec\n"


    def vrat_akci(self, akce):
        if akce == "1":
            return self.pridej_pojistence
        elif akce == "2":
            return self.zobraz_vsechny_pojistence
        elif akce == "3":
            return self.vyhledej_pojistence
        elif akce == "4":
            return self.konec


    def pridej_pojistence(self):

        jmeno = input("\nZadejte jméno pojištěného:\n")
        prijmeni = input("Zadejte příjmení:\n")
        tel_c = int(input("Zadejte telefonní číslo:\n"))
        vek = int(input("Zadejte věk:\n"))

        self.pojistenci.pridej_pojistence(jmeno, prijmeni, vek, tel_c)

        vypisy.data_ulozena()
        vypisy.pokracuj_libovolnou_klavesou()


    def zobraz_vsechny_pojistence(self):
        
        vsichni_pojistenci = self.pojistenci.seznam_pojistencu

        vypisy.zobraz_hlavicku_tabulky_pojistencu()
       
        if len(vsichni_pojistenci) > 0:
            for pojistenec in vsichni_pojistenci:
                print(pojistenec)

            vypisy.pokracuj_libovolnou_klavesou()
        else:
            vypisy.seznam_je_prazdny()
            vypisy.pokracuj_libovolnou_klavesou()


    def vyhledej_pojistence(self):

        jmeno = input("\nZadejte jméno pojištěného:\n")
        prijmeni = input("Zadejte příjmení:\n")

        nalezeni_pojistenci = []

        for pojistenec in self.pojistenci.seznam_pojistencu:
            if jmeno == pojistenec.jmeno and prijmeni == pojistenec.prijmeni:
                nalezeni_pojistenci.append(pojistenec)

        if len(nalezeni_pojistenci) > 0:
            vypisy.zobraz_hlavicku_tabulky_pojistencu()

            for pojistenec in nalezeni_pojistenci:
                print(pojistenec)

            vypisy.pokracuj_libovolnou_klavesou()
        else:
            vypisy.pojistenec_neni_v_seznamu(jmeno, prijmeni)
            vypisy.pokracuj_libovolnou_klavesou()


    def konec(self):

        vypisy.ukoncit_program()
        sys.exit(0)