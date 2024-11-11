import pytest
from src.ciphers.base_cypher import robimy_slowniki,tworze_slownik_ascii,tworze_liste_znakow_ascii

def test_towrzenie_slownika():
    assert robimy_slowniki("abc") == {1:"a",2:"b",3:"c"}

def test_tworzenie_slownika_ze_spacją():
    wynik = robimy_slowniki("a b")
    assert wynik == {1:"a", 2:" ", 3:"b"}

def test_tworzenie_pustego_slownika():
    wynik = robimy_slowniki("")
    assert wynik == {}




def test_makiing_ascii_list():
    lista = tworze_liste_znakow_ascii()
    assert len(lista) == 94

def test_first_and_last_object():
    wynik = tworze_liste_znakow_ascii()
    assert wynik[0] == '!'
    assert wynik[-1] == '~'

def test_content_of_the_list():
    lista = []
    for i in range(33, 127):
        lista.append(chr(i))
    assert tworze_liste_znakow_ascii() == lista


def test_empty_list():
    slownik = tworze_slownik_ascii([])
    assert slownik == {}

def test_list_with_3_elem():
    slownik = tworze_slownik_ascii(["a","b","c"])
    assert slownik == {1:"a", 2:"b", 3:"c"}

def test_lista_ze_znakami_specjalnymi():
    wynik = tworze_slownik_ascii(['!', '@', '#'])
    assert wynik == {1: '!', 2: '@', 3: '#'}