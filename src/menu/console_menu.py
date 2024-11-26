from dbm import error
from src.tools.logger import logger
from src.exceptions.cipher_exceptions import InvalidCipherTextError, FileOperationError, InvalidMenuChoice, FileNotExistError
from src.facade.cipher_facade import CipherFacade
from src.file_handlers.json_handler import *
from src.history.history_memory import History_Of_Coding_Decoding
from src.settings.settings import Settings

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
                            self.fasade.encrypt(self.podaj_tekst(), algorytm_rot13)
                        case "2":
                            self.fasade.encrypt(self.podaj_tekst(), algorytm_rot47)
                        case _:
                            error = InvalidMenuChoice(wybor)
                            print(error)

                case "2":
                    print("\n".join(cipher_menu))
                    wybor_algo = self.wybierz()
                    match wybor_algo:
                        case "1":
                            encrypted = self.fasade.decrypt(self.podaj_tekst(), algorytm_rot13)
                        case "2":
                            encrypted = self.fasade.decrypt(self.podaj_tekst(), algorytm_rot47)
                        case _:
                            error = InvalidMenuChoice(wybor)
                            print(error)
                case "3":
                    self.fasade.historia.pokaz_historie()

                case "4":
                    self.fasade.historia.zapisz_historie(Settings.save_history_path)
                    print("historia została zapisana poprwanie")

                case "5":
                    try:
                        self.fasade.odkoduj_z_pliku()
                    except (InvalidCipherTextError, FileOperationError, FileNotExistError) as e:
                        logger.error(e)

                case "6":
                    exit(0)
                case _:
                    error = InvalidMenuChoice(wybor)
                    logger.error(error)





    def podaj_tekst(self):
        tekst = input("podaj tekst: ")
        return tekst

    def wybierz(self)-> str:
        wybor = input("wybierz akcje: ")
        return wybor

#nie uzywane
    # def podaj_zdanie_do_zakodowania_dekodowania(self)-> str:
    #     zdanie_do_zakodowania = input("wpisz zdanie: ")
    #     return zdanie_do_zakodowania
    #
    # def podaj_sciezke_do_pliku(self)-> str:
    #     sciezka = input("podaj scieżke: ")
    #     return f'{sciezka}'


# # todo facade
#     def odkoduj_z_pliku(self):
#         # sciezka = r"C:\Users\jendr\Desktop\json_test.txt"
#
#         plik = self.plik.json_loader(Settings.decode_filepath)
#         slownik_pliku = self.plik.json_handler(plik)
#         zdanie_zakodowane = slownik_pliku[0]
#         algorytm = slownik_pliku[1]
#         timestamp = slownik_pliku[2]
#
#         match algorytm:
#
#             case "ROT13":
#                 encrypted = self.fasade.encrypt(zdanie_zakodowane, "ROT13")
#                 print(f"\n-------------------\n|kod : {encrypted}|\n-------------------\n")
#                 format_do_zapisu = (encrypted, "ROT13", timestamp)
#                 self.history.dodaj(self.plik.json_maker(format_do_zapisu))
#
#             case "ROT47":
#                 encrypted = self.fasade.encrypt(zdanie_zakodowane, "ROT47")
#                 print(f"\n-------------------\n|kod : {encrypted}|\n-------------------\n")
#                 format_do_zapisu = (encrypted, "ROT47", timestamp)
#
#                 self.history.dodaj(self.plik.json_maker(format_do_zapisu))
#
#             case _:
#                 raise InvalidCipherTextError(algorytm)
#
#


elo = Menu()
elo.show_menu()



