import json
import os

from exceptions.cipher_exceptions import FileNotExistError, FileOperationError
from tools.logger import logger


class Plik:
    """
    Handles JSON file operations for cipher text storage and retrieval.

    Provides methods for loading, parsing, and creating JSON files
    with cipher-related information.
    """

    def __init__(self) -> None:
        pass

    def json_loader(self, sciezka: str) -> dict:
        """
        Loads JSON data from a specified file path.

        Args:
            sciezka (str): Path to the JSON file.

        Returns:
            Dict[str, Union[str, int]]: Loaded JSON data.

        Raises:
            FileOperationError: If file path is empty.
            FileNotExistError: If specified file does not exist.
        """
        if not sciezka:
            logger.debug("sprawdzam sciezke")
            raise FileOperationError(sciezka)
        elif not os.path.isfile(sciezka):
            raise FileNotExistError(sciezka)
        else:
            with open(sciezka) as json_file:
                data = json.load(json_file)
            return data

    def json_handler(self, slownik: dict) -> tuple:
        """
        Extracts key information from JSON dictionary.

        Args:
            slownik (Dict[str, str]): Dictionary containing cipher data.

        Returns:
            Tuple[str, str, str]: Extracted text, algorithm, and timestamp.
        """
        text = slownik["text"]
        algorithm = slownik["algorithm"]
        timestamp = slownik["timestamp"]
        return text, algorithm, timestamp

    def json_maker(self, krotka: tuple) -> dict:
        """
        Creates a JSON-compatible dictionary from input tuple.

        Args:
            krotka (Tuple[str, str, str]): Tuple containing text, algorithm, timestamp.

        Returns:
            Dict[str, str]: Formatted dictionary for JSON serialization.
        """
        slownik = {}
        slownik["text"] = krotka[0]
        slownik["algorithm"] = krotka[1]
        slownik["timestamp"] = krotka[2]
        return slownik
