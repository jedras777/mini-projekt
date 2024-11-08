class Menu:
    def __init__(self):
        self.opcja1 = "--------Menu----------"
        self.opcja2 = "1.zakoduj zdanie wpisane przez siebie"
        self.opcja3 = "2.zdekoduj zdanie wpisane przez siebie"
        self.opcja5 = "3.pokaz historie"
        self.opcja8 = "4.zapisz historię do pliku"
        self.opcja6 = "5.zdekoduj plik json"
        self.opcja4 = "6.zakoncz"

        self.opcja7 = ".zakoduj plik json" # zapytac czy tez to dodac


        self.rot13_wubor = "1.rot13"
        self.rot47_wubor = "2.rot47"


    def __repr__(self)-> str:
        return f"{self.opcja1}\n{self.opcja2}\n{self.opcja3}\n{self.opcja5}\n{self.opcja8}\n{self.opcja6}\n{self.opcja4}\n"

    def repr_szyfry(self)-> str:
        return f"{self.rot13_wubor}\n{self.rot47_wubor}"

    def wybierz(self)-> str:
        wybor = input("wybierz akcje: ")
        return wybor

    def podaj_zdanie_do_zakodowania_dekodowania(self)-> str:
        zdanie_do_zakodowania = input("wpisz zdanie: ")
        return zdanie_do_zakodowania

    def podaj_sciezke_do_pliku(self)-> str:
        sciezka = input("podaj scieżke: ")
        return f'{sciezka}'

    def dodaj_zdanie_do_pliku(self, zdanie: str)-> None:
        sciezka = r"C:\Users\jendr\Desktop\plik_do_zapisywania_zdan.txt"
        with open(sciezka, "w", encoding="utf-8") as plik:
            plik.write(zdanie)

# menu = Menu()
# sciezka = menu.podaj_sciezke_do_pliku()
# print(sciezka)


