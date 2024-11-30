
from src.ciphers.base_cypher import BaseCipher

class ROT47Cipher(BaseCipher):
    def encrypt(self, text: str) -> str:
        return text.translate(str.maketrans(
            r"""!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""",
            r"""PQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNO"""
        ))

    def decrypt(self, text: str) -> str:
        return self.encrypt(text)  # ROT13 is symmetric



