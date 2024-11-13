
from src.ciphers.base_cypher import robimy_slowniki, slownik_malych, slownik_duzych, lista_znakow

def szyfrowanie_rot13(zdanie: str)-> str:
    slownik_zdania = robimy_slowniki(zdanie)
    zdanie_zakodowane = []
    for key, elem in slownik_zdania.items():
        for (numer_duzy, litera_duza), (numer_maly, litera_mala) in zip(slownik_duzych.items(), slownik_malych.items()):
            if elem == litera_duza:
                if numer_duzy <= 13:
                    zdanie_zakodowane.append(slownik_duzych[numer_duzy + 13].upper())
                else:
                    zdanie_zakodowane.append(slownik_duzych[(numer_duzy + 13) - 26].upper())
            elif elem == litera_mala:
                if numer_maly <= 13:
                    zdanie_zakodowane.append(slownik_duzych[numer_maly + 13].lower())
                else:
                    zdanie_zakodowane.append(slownik_duzych[(numer_maly + 13) - 26].lower())
        if elem in lista_znakow:
            zdanie_zakodowane.append(elem)
    return "".join(zdanie_zakodowane)

def deszyfrowanie_rot13(zdanie: str)-> str:
    slownik_zdania = robimy_slowniki(zdanie)
    zdanie_zakodowane = []
    for key, elem in slownik_zdania.items():
        for (numer_duzy, litera_duza), (numer_maly, litera_mala) in zip(slownik_duzych.items(), slownik_malych.items()):
            if elem == litera_duza:
                if numer_duzy > 13:
                    zdanie_zakodowane.append(slownik_duzych[numer_duzy - 13].upper())
                else:
                    zdanie_zakodowane.append(slownik_duzych[(numer_duzy - 13) + 26].upper())
            elif elem == litera_mala:
                if numer_maly > 13:
                    zdanie_zakodowane.append(slownik_duzych[numer_maly - 13].lower())
                else:
                    zdanie_zakodowane.append(slownik_duzych[(numer_maly - 13) + 26].lower())
        if elem in lista_znakow:
            zdanie_zakodowane.append(elem)
    return "".join(zdanie_zakodowane)







#notatki review
from .base_cypher import BaseCipher

class ROT13Cipher(BaseCipher):
    def encrypt(self, text: str) -> str:
        return text.translate(str.maketrans(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
            "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
        ))

    def decrypt(self, text: str) -> str:
        return self.encrypt(text)  # ROT13 is symmetric