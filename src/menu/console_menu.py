from exceptions.cipher_exceptions import (
    FileNotExistError,
    FileOperationError,
    InvalidCipherTextError,
    InvalidMenuChoice,
)
from facade.cipher_facade import CipherFacade
from file_handlers.json_handler import *
from settings.settings import Settings
from tools.logger import logger


class Menu:
    def __init__(self) -> None:
        """
        A menu-driven interface for cipher operations.

        Attributes:
        fasade (CipherFacade): Facade for managing cipher operations.
        """
        self.fasade = CipherFacade()

    def show_menu(self) -> None:
        """
        Displays the main menu and handles user interactions.

        This method provides a loop-based menu system for various cipher operations
        including encryption, decryption, history management, and file operations.
        """

        menu_text = [
            "--------Menu----------",
            "1.zakoduj zdanie wpisane przez siebie",
            "2.zdekoduj zdanie wpisane przez siebie",
            "3.pokaz historie",
            "4.zapisz historię do pliku",
            "5.zdekoduj plik json",
            "6.zakoncz",
        ]

        cipher_menu = ["1.rot13", "2.rot47"]

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
                            encrypted = self.fasade.encrypt(
                                self.podaj_tekst(), algorytm_rot13
                            )
                            print(encrypted)
                        case "2":
                            encrypted = self.fasade.encrypt(
                                self.podaj_tekst(), algorytm_rot47
                            )
                            print(encrypted)
                        case _:
                            error = InvalidMenuChoice(wybor_algo)
                            print(error)

                case "2":
                    print("\n".join(cipher_menu))
                    wybor_algo = self.wybierz()
                    match wybor_algo:
                        case "1":
                            decrypted = self.fasade.decrypt(
                                self.podaj_tekst(), algorytm_rot13
                            )
                            print(decrypted)
                        case "2":
                            decrypted = self.fasade.decrypt(
                                self.podaj_tekst(), algorytm_rot47
                            )
                            print(decrypted)
                        case _:
                            error = InvalidMenuChoice(wybor_algo)
                            print(error)
                case "3":
                    historia = self.fasade.historia.pokaz_historie()
                    print(historia)
                case "4":
                    dzialanie = self.fasade.historia.zapisz_historie(Settings.save_history_path)
                    print(dzialanie)

                case "5":
                    try:
                        encrypted = self.fasade.odkoduj_z_pliku()
                        print(encrypted)
                    except (
                        InvalidCipherTextError,
                        FileOperationError,
                        FileNotExistError,
                    ) as e:
                        logger.error(e)

                case "6":
                    exit(0)
                case _:
                    error = InvalidMenuChoice(wybor)
                    logger.error(error)

    def podaj_tekst(self) -> str:
        """
        Prompts user to input text.

        Returns:
            str: Text input by the user.
        """
        tekst = input("podaj tekst: ")
        return tekst

    def wybierz(self) -> str:
        """
        Prompts user to select an action.

        Returns:
            str: User's selected action.
        """
        wybor = input("wybierz akcje: ")
        return wybor


if __name__ == "__main__":
    elo = Menu()
    elo.show_menu()
