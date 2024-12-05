
from src.ciphers.base_cypher import BaseCipher


class ROT13Cipher(BaseCipher):
    """
     Implements the ROT13 substitution cipher algorithm.

     ROT13 is a simple letter substitution cipher that replaces a letter
     with the 13th letter after it in the alphabet. Due to its symmetrical
     nature, encryption and decryption are the same operation.
     """
    def encrypt(self, text: str) -> str:
        """
        Encrypts the input text using ROT13 substitution.

        Args:
            text (str): The text to be encrypted.

        Returns:
            str: The encrypted text.
        """
        return text.translate(str.maketrans(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
            "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
        ))

    def decrypt(self, text: str) -> str:
        """
        Decrypts the input text using ROT13 substitution.

        Due to ROT13's symmetrical nature, decryption is identical to encryption.

        Args:
            text (str): The text to be decrypted.

        Returns:
            str: The decrypted text.
        """
        return self.encrypt(text)  # ROT13 is symmetric

