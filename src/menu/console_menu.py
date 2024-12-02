from src.exceptions.cipher_exceptions import (
    FileNotExistError,
    FileOperationError,
    InvalidCipherTextError,
    InvalidMenuChoice,
)
from src.facade.cipher_facade import CipherFacade
from src.file_handlers.json_handler import *
from src.settings.settings import Settings
from src.tools.logger import logger


class Menu:
    def __init__(self)-> None:
        self.fasade = CipherFacade()


    def show_menu(self)-> None:
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

                            encrypted = self.fasade.encrypt(self.podaj_tekst(),
                                                            algorytm_rot13)
                            print(encrypted)
                        case "2":
                            encrypted = self.fasade.encrypt(self.podaj_tekst(),
                                                            algorytm_rot47)
                            print(encrypted)
                        case _:
                            error = InvalidMenuChoice(wybor_algo)
                            print(error)

                case "2":
                    print("\n".join(cipher_menu))
                    wybor_algo = self.wybierz()
                    match wybor_algo:
                        case "1":
                            decrypted = self.fasade.decrypt(self.podaj_tekst(),
                                                            algorytm_rot13)
                            print(decrypted)
                        case "2":
                            decrypted = self.fasade.decrypt(self.podaj_tekst(),
                                                            algorytm_rot47)
                            print(decrypted)
                        case _:
                            error = InvalidMenuChoice(wybor_algo)
                            print(error)
                case "3":
                    self.fasade.historia.pokaz_historie()
                case "4":
                    self.fasade.historia.zapisz_historie(Settings.save_history_path)
                    print("historia została zapisana poprwanie")

                case "5":
                    try:
                        encrypted = self.fasade.odkoduj_z_pliku()
                        print(encrypted)
                    except (InvalidCipherTextError, FileOperationError,
                            FileNotExistError) as e:
                        logger.error(e)

                case "6":
                    exit(0)
                case _:
                    error = InvalidMenuChoice(wybor)
                    logger.error(error)


    def podaj_tekst(self)-> str:
        tekst = input("podaj tekst: ")
        return tekst

    def wybierz(self)-> str:
        wybor = input("wybierz akcje: ")
        return wybor



if __name__ == "__main__":
    elo = Menu()
    elo.show_menu()



