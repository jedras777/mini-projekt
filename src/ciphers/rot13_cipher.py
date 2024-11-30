
from src.ciphers.base_cypher import BaseCipher

class ROT13Cipher(BaseCipher):
    def encrypt(self, text: str) -> str:
        return text.translate(str.maketrans(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
            "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
        ))

    def decrypt(self, text: str) -> str:
        return self.encrypt(text)  # ROT13 is symmetric

