# Pomocné funkce pro zobrazení uživateli na obrazovce

def pokracuj_libovolnou_klavesou():
    input("\nPokračujte libovolnou klávesou...")

def ukoncit_program():
    print("Nashledanou")
    pokracuj_libovolnou_klavesou()

def nespravna_akce():
    print("\nZadali jste nesprávnou akci. Zvolte možnost 1 - 4")
    pokracuj_libovolnou_klavesou()

def pojistenec_neni_v_seznamu(jmeno, prijmeni):
    print("\n{0} {1} není v seznamu pojištěných".format(jmeno, prijmeni))

def data_ulozena():
    print("\nData byla uložena.")

def seznam_je_prazdny():
    print("\nV seznamu není žádný záznam")

def zobraz_hlavicku_tabulky_pojistencu():
    print("\n{:<15} {:<15} {:<15} {:<10}".format("Jméno", "Příjmení", "Tel. č.", "Věk"))