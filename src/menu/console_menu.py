from src.exceptions.cipher_exceptions import InvalidCipherTextError, FileOperationError, InvalidMenuChoice
from src.facade.cipher_facade import CipherFacade
from src.file_handlers.json_handler import *
from src.history.history_memory import History_Of_Coding_Decoding


class Menu:
    def __init__(self):
        self.fasade = CipherFacade()
        self.history = History_Of_Coding_Decoding()
        self.plik = Plik()

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

        cipher_menu = [
            "1.rot13",
            "2.rot47"
                       ]

        algorytm_rot13 = "ROT13"
        algorytm_rot47 = "ROT47"

        while True:

            print("\n".join(menu_text))
            wybor = self.wybierz()
            match wybor:

                case "1":
                    print("\n".join(cipher_menu))
                    wybor_algo = self.wybierz()
                    match wybor_algo:
                        case "1":
                            encrypted = self.fasade.encrypt(self.podaj_tekst(), algorytm_rot13)
                            print(f"{encrypted}")
                            format_do_zapisu = (encrypted, algorytm_rot13, self.history.dodaj_czas())
                            self.history.dodaj(self.plik.json_maker(format_do_zapisu))
                            self.dodaj_zdanie_do_pliku(encrypted)
                        case "2":
                            encrypted = self.fasade.encrypt(self.podaj_tekst(), algorytm_rot47)
                            print(f"{encrypted}")
                            format_do_zapisu = (encrypted, algorytm_rot47, self.history.dodaj_czas())
                            self.history.dodaj(self.plik.json_maker(format_do_zapisu))
                            self.dodaj_zdanie_do_pliku(encrypted)

                case "2":
                    print("\n".join(cipher_menu))
                    wybor_algo = self.wybierz()
                    match wybor_algo:
                        case "1":
                            encrypted = self.fasade.decrypt(self.podaj_tekst(), algorytm_rot13)
                            print(f"{encrypted}")
                            format_do_zapisu = (encrypted, algorytm_rot13, self.history.dodaj_czas())
                            self.history.dodaj(self.plik.json_maker(format_do_zapisu))
                            self.dodaj_zdanie_do_pliku(encrypted)
                        case "2":
                            encrypted = self.fasade.decrypt(self.podaj_tekst(), algorytm_rot47)
                            print(f"{encrypted}")
                            format_do_zapisu = (encrypted,algorytm_rot47, self.history.dodaj_czas())
                            self.history.dodaj(self.plik.json_maker(format_do_zapisu))
                            self.dodaj_zdanie_do_pliku(encrypted)

                case "3":
                    self.history.pokaz_historie()

                case "4":
                    sciezka = r"C:\Users\jendr\Desktop\historia_mini_projektu.txt"
                    self.history.zapisz_historie(sciezka)
                    print("historia została zapisana poprwanie")
                case "5":
                    try:
                        self.odkoduj_z_pliku()
                    except (InvalidCipherTextError, FileOperationError) as e:
                        print(e)

                case "6":
                    break

                case _:
                    raise InvalidMenuChoice(wybor)





    def podaj_tekst(self):
        tekst = input("podaj tekst: ")
        return tekst

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
    def odkoduj_z_pliku(self):
        sciezka = r"C:\Users\jendr\Desktop\json_test.tt"
        plik = self.plik.json_loader(sciezka)
        if plik:
            slownik_pliku = self.plik.json_handler(plik)
            zdanie_zakodowane = slownik_pliku[0]
            algorytm = slownik_pliku[1]
            timestamp = slownik_pliku[2]
            # ALGORYTM_ROT13 = "ROT13"
            # ALGORYTM_ROT47= "ROT47"
            match algorytm:

                case "ROT13":
                    encrypted = self.fasade.encrypt(zdanie_zakodowane, "ROT13")
                    print(f"\n-------------------\n|kod : {encrypted}|\n-------------------\n")
                    format_do_zapisu = (encrypted, "ROT13", timestamp)
                    self.history.dodaj(self.plik.json_maker(format_do_zapisu))

                case "ROT47":
                    encrypted = self.fasade.encrypt(zdanie_zakodowane, "ROT47")
                    print(f"\n-------------------\n|kod : {encrypted}|\n-------------------\n")
                    format_do_zapisu = (encrypted, "ROT47", timestamp)

                    self.history.dodaj(self.plik.json_maker(format_do_zapisu))

                case _:
                    raise InvalidCipherTextError(algorytm)
        else:
            raise FileOperationError(sciezka)




menu = Menu()
menu.show_menu()
# sciezka = menu.podaj_sciezke_do_pliku()
# print(sciezka)


