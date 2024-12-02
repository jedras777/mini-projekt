from abc import ABC, abstractmethod


class BaseCipher(ABC):

    """
    Abstract base class defining the interface for cipher algorithms.

    Provides a template for encryption and decryption methods that must be
    implemented by concrete cipher classes.

    Attributes:
    None
    """
    @abstractmethod
    def encrypt(self, text: str) -> str:
        """
        Abstract method for encrypting input text.

        Args:
            text (str): The text to be encrypted.

        Returns:
            str: The encrypted text.

        Raises:
            NotImplementedError: If the method is not implemented by subclass.
        """
        pass

    @abstractmethod
    def decrypt(self, text: str) -> str:
        """
        Abstract method for decrypting input text.

        Args:
            text (str): The text to be decrypted.

        Returns:
            str: The decrypted text.

        Raises:
            NotImplementedError: If the method is not implemented by subclass.
        """
        pass
