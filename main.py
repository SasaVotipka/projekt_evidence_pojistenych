
from akce import Akce
import vypisy

class Main:

    def __init__(self):
        self.akce = Akce()


    def __str__(self):
        return "\n---------------------------\n    Evidence pojištěných\n---------------------------"


    def spust_program(self):
          
        print(self)

        while True:
            print(self.akce)
            akce = input()
            zvolena_akce = self.akce.vrat_akci(akce)
            if zvolena_akce:
                zvolena_akce()
            else:
                vypisy.nespravna_akce()  


main = Main()
main.spust_program()    
