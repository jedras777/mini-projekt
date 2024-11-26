import pytest
from src.ciphers.base_cypher import BaseCipher

class Test(BaseCipher):
    def encrypt(self, text: str) -> str:
        return text
    def decrypt(self, text: str) -> str:
        return text

def test_encrypt():
    klasa = Test()
    assert klasa.encrypt("elo") == "elo"

def test_decrypt():
    klasa = Test()
    assert klasa.decrypt("elo") == "elo"

def test_abstract_method():
    with pytest.raises(TypeError):
        _ = BaseCipher()