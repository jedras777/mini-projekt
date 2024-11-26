from src.ciphers.base_cypher import slownik_asciiiii, robimy_slowniki, lista_znakow

def szyfrowanie_rot47(zdanie: str)-> str:
    slownik_zdania = robimy_slowniki(zdanie)
    kodder = []
    for indeks, litera in slownik_zdania.items():
        for indeks1, litera_slowniku in slownik_asciiiii.items():
            if litera == litera_slowniku:
                if indeks1 <= 47:
                    kodder.append(slownik_asciiiii[indeks1 + 47])
                else:
                    kodder.append(slownik_asciiiii[(indeks1 + 47) - 94])
        if litera in lista_znakow:
            kodder.append(litera)
    return "".join(kodder)

def deszyfrowanie_rot47(zdanie: str)-> str:
    slownik_zdania = robimy_slowniki(zdanie)
    kodder = []
    for indeks, litera in slownik_zdania.items():
        for indeks1, litera_slowniku in slownik_asciiiii.items():
            if litera == litera_slowniku:
                if indeks1 < 48:
                    kodder.append(slownik_asciiiii[(indeks1 - 47 + 94)])
                else:
                    kodder.append(slownik_asciiiii[(indeks1 - 47)])
        if litera in lista_znakow:
            kodder.append(litera)
    return "".join(kodder)




#notatki review
from src.ciphers.base_cypher import BaseCipher

class ROT47Cipher(BaseCipher):
    def encrypt(self, text: str) -> str:
        return text.translate(str.maketrans(
            r"""!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""",
            r"""PQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNO"""
        ))

    def decrypt(self, text: str) -> str:
        return self.encrypt(text)  # ROT13 is symmetric



