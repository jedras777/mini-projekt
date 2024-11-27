import json
import os
from src.tools.logger import logger
from src.exceptions.cipher_exceptions import FileOperationError, FileNotExistError


class Plik:
    def __init__(self):
        pass

    def json_loader(self, sciezka: str)-> dict:
        if not sciezka:
            logger.debug("sprawdzam sciezke")
            raise FileOperationError(sciezka)
        elif not os.path.isfile(sciezka):
            raise FileNotExistError(sciezka)
        else:
            with open(sciezka) as json_file:
                data = json.load(json_file)
            return data


    def json_handler(self, slownik: dict)-> tuple:
       text = slownik["text"]
       algorithm = slownik["algorithm"]
       timestamp = slownik["timestamp"]
       return text, algorithm, timestamp

    def json_maker(self, krotka: tuple)-> dict:
        slownik = {}
        slownik["text"] = krotka[0]
        slownik["algorithm"] = krotka[1]
        slownik["timestamp"] = krotka[2]
        return slownik

# elo = json_handler(plik)
# elo1 = json_maker(elo)
# elo = json_loader(plik)
