

import pytest

from src.exceptions.cipher_exceptions import InvalidCipherTextError
from src.facade.cipher_facade import CipherFacade
from src.settings.settings import Settings


def test_encrypt():
    """
    Test encrypt method with different ciphers.
    """
    klasa = CipherFacade()
    assert klasa.encrypt("elo", "ROT13") == "ryb"
    assert klasa.encrypt("elo", "ROT47") == "6=@"
    assert klasa.encrypt("", "ROT47") == ""

def test_decrypt():
    """
    Test decrypt method with different ciphers.
    """
    klasa = CipherFacade()
    assert klasa.decrypt("elo", "ROT13") == "ryb"
    assert klasa.decrypt("elo", "ROT47") == "6=@"
    assert klasa.decrypt("", "ROT47") == ""

def test_encrypt_invalid_cipher_text_error():
    """
    Verify InvalidCipherTextError is raised for invalid cipher.
    """
    klasa = CipherFacade()
    with pytest.raises(InvalidCipherTextError):
        klasa.encrypt("elo", "ROT56")

def test_decrypt_invalid_cipher_text_error():
    """
    Verify InvalidCipherTextError is raised for invalid cipher.
    """
    klasa = CipherFacade()
    with pytest.raises(InvalidCipherTextError):
        klasa.decrypt("elo", "ROT56")

def test_add_to_file():
    """
    Test adding text to file.
    """
    klasa = CipherFacade()
    klasa.dodaj_zdanie_do_pliku("elo")
    with open(Settings.save_path, 'r', encoding='utf-8') as file:
        zawartosc = file.read()
    assert "elo" == zawartosc



def test_odkoduj_z_pliku():
    """
    Test decoding text from file.
    """
    klasa = CipherFacade()
    assert klasa.odkoduj_z_pliku() == "mnfmlsebjnal_grxfg"
