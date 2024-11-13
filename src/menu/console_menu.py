from src.facade.cipher_facade import algorytm, CipherFacade


class Menu:
    def __init__(self):
        self.opcja7 = ".zakoduj plik json" # zapytac czy tez to dodac

        self.fasade = CipherFacade()
        self.rot13_wubor = "1.rot13"
        self.rot47_wubor = "2.rot47"

    def show_menu(self):
        menu_text = [
            "--------Menu----------",
            "1.zakoduj zdanie wpisane przez siebie",
            "2.zdekoduj zdanie wpisane przez siebie",
            "3.pokaz historie",
            "4.zapisz historię do pliku",
            "5.zdekoduj plik json",
            "6.zakoncz"
        ]
        while True:
            print("\n".join(menu_text))
            wybor = self.wybierz()
            match wybor:
                case "1":
                    text = input("wpisz tekst:")
                    algorytm = input("wybiierz ")
                    encrypted = self.fasade.encrypt(text, algorytm)


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


