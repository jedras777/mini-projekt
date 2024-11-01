class Menu:
    def __init__(self):
        self.opcja1 = "--------Menu----------"
        self.opcja2 = "1.zakoduj zdanie wpisane przez siebie"
        self.opcja3 = "2.zdekoduj zdanie wpisane przez siebie"
        self.opcja4 = "4.zakoncz"
        self.opcja5 = "3.pokaz historie"
        self.opcja6 = "5.zdekoduj plik json"
        self.opcja8 = "6.zapisz historię do pliku"
        self.opcja7 = ".zakoduj plik json" # zapytac czy tez to dodac


        self.rot13_wubor = "1.rot13"
        self.rot47_wubor = "2.rot47"


    def __repr__(self):
        return f"{self.opcja1}\n{self.opcja2}\n{self.opcja3}\n{self.opcja5}\n{self.opcja6}\n{self.opcja8}\n{self.opcja4}\n"

    def repr_szyfry(self):
        return f"{self.rot13_wubor}\n{self.rot47_wubor}"
    def wybierz(self):
        wybor = input("wybierz akcje: ")
        return wybor

    def podaj_zdanie_do_zakodowania_dekodowania(self):
        zdanie_do_zakodowania = input("wpisz zdanie: ")
        return zdanie_do_zakodowania

    def podaj_sciezke_do_pliku(self):
        sciezka = input("podaj scieżke: ")
        return f'{sciezka}'

# menu = Menu()
# sciezka = menu.podaj_sciezke_do_pliku()
# print(sciezka)


