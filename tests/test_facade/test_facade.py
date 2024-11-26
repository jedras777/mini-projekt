
import pytest
from src.exceptions.cipher_exceptions import InvalidCipherTextError
from src.facade.cipher_facade import CipherFacade
from src.settings.settings import Settings


def test_encrypt():
    klasa = CipherFacade()
    assert klasa.encrypt("elo", "ROT13") == "ryb"
    assert klasa.encrypt("elo", "ROT47") == "6=@"
    assert klasa.encrypt("", "ROT47") == ""

def test_decrypt():
    klasa = CipherFacade()
    assert klasa.decrypt("elo", "ROT13") == "ryb"
    assert klasa.decrypt("elo", "ROT47") == "6=@"
    assert klasa.decrypt("", "ROT47") == ""

def test_invalid_cipher():
    klasa = CipherFacade()
    with pytest.raises(InvalidCipherTextError):
        klasa.encrypt("elo", "ROT56")
        klasa.decrypt("elo", "ROT56")


def test_add_to_file():
    klasa = CipherFacade()
    klasa.dodaj_zdanie_do_pliku("elo")
    with open(Settings.save_path, 'r', encoding='utf-8') as file:
        zawartosc = file.read()
    assert "elo" == zawartosc