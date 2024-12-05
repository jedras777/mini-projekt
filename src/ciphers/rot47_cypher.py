from .base_cypher import BaseCipher


class ROT47Cipher(BaseCipher):
    """
    Implements the ROT47 substitution cipher algorithm.

    ROT47 is a more comprehensive substitution cipher that rotates
    printable ASCII characters by 47 positions.
    """

    def encrypt(self, text: str) -> str:
        """
        Encrypts the input text using ROT47 substitution.

        Args:
            text (str): The text to be encrypted.

        Returns:
            str: The encrypted text.
        """
        return text.translate(
            str.maketrans(
                r"""!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""",
                r"""PQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNO""",
            )
        )

    def decrypt(self, text: str) -> str:
        """
        Decrypts the input text using ROT47 substitution.

        Due to ROT47's symmetrical nature, decryption is identical to encryption.

        Args:
            text (str): The text to be decrypted.

        Returns:
            str: The decrypted text.
        """
        return self.encrypt(text)  # ROT13 is symmetric
