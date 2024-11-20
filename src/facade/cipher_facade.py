
#from src.ciphers.rot13_cipher import ROT13Cipher

# from src.menu.console_menu import *
#
#
#
# algorytm_rot_13 = "ROT13"
# algorytm_rot_47 = "ROT47"
# historia = History_Of_Coding_Decoding()
#
# while True:
#
#     menu = Menu()
#     print(menu)
#     wybor = menu.wybierz()
#
#     if wybor == "1":
#         print(menu.repr_szyfry())
#         wybor = menu.wybierz()
#
#         if wybor == "1":
#             zdanie = menu.podaj_zdanie_do_zakodowania_dekodowania()
#             zdanie_zakodowane = szyfrowanie_rot13(zdanie)
#             print(f"\n-------------------\n|kod : {zdanie_zakodowane}|\n-------------------\n")
#             format_do_konwersji_json = (zdanie_zakodowane, algorytm_rot_13, historia.dodaj_czas())
#             historia.dodaj(json_maker(format_do_konwersji_json))
#             menu.dodaj_zdanie_do_pliku(zdanie_zakodowane)
#
#         elif wybor == "2":
#             zdanie = menu.podaj_zdanie_do_zakodowania_dekodowania()
#             zdanie_zakodowane = szyfrowanie_rot47(zdanie)
#             print(f"\n-------------------\n|kod : {zdanie_zakodowane}|\n-------------------\n")
#             format_do_konwersji_json = (zdanie_zakodowane, algorytm_rot_47, historia.dodaj_czas())
#             historia.dodaj(json_maker(format_do_konwersji_json))
#             menu.dodaj_zdanie_do_pliku(zdanie_zakodowane)
#
#     elif wybor == "2":
#         print(menu.repr_szyfry())
#         wybor = menu.wybierz()
#
#         if wybor == "1":
#             zdanie_zakodowane = menu.podaj_zdanie_do_zakodowania_dekodowania()
#             zdanie_zdekodowane = deszyfrowanie_rot13(zdanie_zakodowane)
#             print(f"\n-------------------\n|kod : {zdanie_zdekodowane}|\n-------------------\n")
#             format_do_konwersji_json = (zdanie_zdekodowane, algorytm_rot_13, historia.dodaj_czas())
#             historia.dodaj(json_maker(format_do_konwersji_json))
#             menu.dodaj_zdanie_do_pliku(zdanie_zdekodowane)
#
#         elif wybor == "2":
#             zdanie_zakodowane = menu.podaj_zdanie_do_zakodowania_dekodowania()
#             zdanie_zdekodowane = deszyfrowanie_rot47(zdanie_zakodowane)
#             print(f"\n-------------------\n|kod : {zdanie_zdekodowane}|\n-------------------\n")
#             format_do_konwersji_json = (zdanie_zdekodowane, algorytm_rot_47, historia.dodaj_czas())
#             historia.dodaj(json_maker(format_do_konwersji_json))
#             menu.dodaj_zdanie_do_pliku(zdanie_zdekodowane)
#
#     elif wybor == "3":
#         historia.pokaz_historie()
#
#     elif wybor == "4":
#         sciezka = r"C:\Users\jendr\Desktop\historia_mini_projektu.txt"
#         historia.zapisz_historie(sciezka)
#
#     elif wybor == "5":
#         #sciezka do json C:\Users\jendr\Desktop\json_test.txt
#         sciezka = menu.podaj_sciezke_do_pliku()
#         plik = json_loader(sciezka)
#         slownik_pliku = json_handler(plik)
#         zdanie_zakodowane = slownik_pliku[0]
#         algorytm = slownik_pliku[1]
#         timestamp = slownik_pliku[2]
#
#         if algorytm == algorytm_rot_13:
#             print(f"\n-------------------\n|kod : {deszyfrowanie_rot13(zdanie_zakodowane)}|\n-------------------\n")
#             format_do_konwersji_json = (deszyfrowanie_rot13(zdanie_zakodowane), algorytm_rot_13, timestamp)
#             historia.dodaj(json_maker(format_do_konwersji_json))
#         elif algorytm == algorytm_rot_47:
#             print(f"\n-------------------\n|kod : {deszyfrowanie_rot47(zdanie_zakodowane)}|\n-------------------\n")
#             format_do_konwersji_json = (deszyfrowanie_rot47(zdanie_zakodowane), algorytm_rot_47, timestamp)
#             historia.dodaj(json_maker(format_do_konwersji_json))
#         else:
#             print("sprawdz czy wpisałes wszystko poprawnie")
#
#     elif wybor == "6":
#         break
#
#     else:
#         print("zly wwybor!!!")

#notatki review
from src.ciphers.rot13_cipher import ROT13Cipher
from src.ciphers.rot47_cypher import ROT47Cipher
from src.exceptions.cipher_exceptions import InvalidCipherTextError
from src.history.history_memory import *

class CipherFacade:
    def __init__(self):
        self.historia = History_Of_Coding_Decoding()
        self.algorytm_rot_13 = ROT13Cipher()
        self.algorytm_rot_47 = ROT47Cipher()

    def encrypt(self, tekst: str, algorytm: str)-> str:
        if algorytm == "ROT13":
            encrypted_tekst = self.algorytm_rot_13.encrypt(tekst)
        elif algorytm == "ROT47":
            encrypted_tekst = self.algorytm_rot_47.encrypt(tekst)
        else:
            raise InvalidCipherTextError(algorytm)

        return encrypted_tekst

    def decrypt(self, tekst: str, algorytm: str)-> str:
        if algorytm == "ROT13":
            decrypted_tekst = self.algorytm_rot_13.decrypt(tekst)
        elif algorytm == "ROT47":
            decrypted_tekst = self.algorytm_rot_47.decrypt(tekst)
        else:
            pass #chce wywolac customowy blad
            raise MojException("nie ma takiego szyfru")
        return decrypted_tekst

elo = CipherFacade()
elo.encrypt("elo", "ROT13")