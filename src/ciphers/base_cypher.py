
#rot13 tworzenie slownikow
import string
def robimy_slowniki(string):
    slownik = {}
    for indeks, litera in enumerate(string, start=1):
        slownik[indeks] = litera
    return slownik


male = string.ascii_lowercase
duze = string.ascii_uppercase

slownik_malych = robimy_slowniki(male)
slownik_duzych = robimy_slowniki(duze)
lista_znakow = [".", " ", "_", ","] #uaktulanic liste znakow

#rot47 tworzenie slownikow


def tworze_liste_znakow_ascii():
    ascii_list = []
    for i in range(33, 127):
        ascii_list.append(chr(i))
    return ascii_list


def tworze_slownik_ascii(lista):
    slownik_ascii = {}
    for indeks, litera in enumerate(lista, start=1):
        slownik_ascii[indeks] = litera
    return slownik_ascii

lista = tworze_liste_znakow_ascii()
slownik_asciiiii = tworze_slownik_ascii(lista)

