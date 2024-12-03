import pytest

from src.ciphers.base_cypher import BaseCipher


class Test(BaseCipher):
    """
    Test cipher implementation for unit testing.

    Inherits from BaseCipher and provides minimal encrypt/decrypt methods
    that return the input text unchanged.
    """
    def encrypt(self, text: str) -> str:

        """
        Encrypt method that returns input text unchanged.

        Args:
            text (str): Input text to encrypt.

        Returns:
            str: Unmodified input text.
        """
        return text
    def decrypt(self, text: str) -> str:
        """
        Decrypt method that returns input text unchanged.

        Args:
            text (str): Input text to decrypt.

        Returns:
            str: Unmodified input text.
        """
        return text

def test_encrypt():
    """
    Test encrypt method of Test cipher class.
    """
    klasa = Test()
    assert klasa.encrypt("elo") == "elo"

def test_decrypt():
    """
    Test decrypt method of Test cipher class.
    """
    klasa = Test()
    assert klasa.decrypt("elo") == "elo"

def test_abstract_method():
    """
    Test that BaseCipher cannot be instantiated directly.
    """
    with pytest.raises(TypeError):
        _ = BaseCipher()

#pytanie na zajęcia jak przetestowac pass
# class ConcreteClass(BaseCipher):
#     def encrypt(self, text: str)-> str:
#         return text + text
#     def decrypt(self, text: str) -> str:
#         return text + text
#
#
# def test_elo():
#     obj = ConcreteClass().encrypt("elo")
#     assert obj == "eloelo"

