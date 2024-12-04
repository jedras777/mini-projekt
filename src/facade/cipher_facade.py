
from src.ciphers.rot13_cipher import ROT13Cipher
from src.ciphers.rot47_cypher import ROT47Cipher
from src.exceptions.cipher_exceptions import InvalidCipherTextError
from src.file_handlers.json_handler import Plik
from src.history.history_memory import HistoryOfCodingDecoding
from src.settings.settings import Settings


class CipherFacade:
    """
    A facade class that provides a unified interface for encryption and decryption
    using ROT13 and ROT47 cipher algorithms.

    Attributes:
        historia (History_Of_Coding_Decoding): Manages the history of
        encoding/decoding operations.
        algorytm_rot_13 (ROT13Cipher): Instance of ROT13 cipher algorithm.
        algorytm_rot_47 (ROT47Cipher): Instance of ROT47 cipher algorithm.
        plik (Plik): File handler for JSON operations.
    """
    def __init__(self)-> None:
        self.historia = HistoryOfCodingDecoding()
        self.algorytm_rot_13 = ROT13Cipher()
        self.algorytm_rot_47 = ROT47Cipher()
        self.plik = Plik()

    def encrypt(self, tekst: str, algorytm: str)-> str:
        """
        Encrypts the given text using the specified cipher algorithm.

        Args:
            tekst (str): The text to be encrypted.
            algorytm (str): The cipher algorithm to use ('ROT13' or 'ROT47').

        Returns:
            str: The encrypted text.

        Raises:
            InvalidCipherTextError: If an unsupported cipher algorithm is specified.
        """
        if algorytm == "ROT13":
            encrypted_tekst = self.algorytm_rot_13.encrypt(tekst)
        elif algorytm == "ROT47":
            encrypted_tekst = self.algorytm_rot_47.encrypt(tekst)
        else:
            raise InvalidCipherTextError(algorytm)

        format_do_zapisu: tuple[str, str, str] = (encrypted_tekst,
                                                  algorytm,
                                                  self.historia.dodaj_czas())
        self.historia.dodaj(self.plik.json_maker(format_do_zapisu))
        self.dodaj_zdanie_do_pliku(encrypted_tekst)

        return encrypted_tekst

    def decrypt(self, tekst: str, algorytm: str)-> str:
        """
       Decrypts the given text using the specified cipher algorithm.

       Args:
           tekst (str): The text to be decrypted.
           algorytm (str): The cipher algorithm to use ('ROT13' or 'ROT47').

       Returns:
           str: The decrypted text.

       Raises:
           InvalidCipherTextError: If an unsupported cipher algorithm is specified.
       """
        if algorytm == "ROT13":
            decrypted_tekst = self.algorytm_rot_13.decrypt(tekst)
        elif algorytm == "ROT47":
            decrypted_tekst = self.algorytm_rot_47.decrypt(tekst)
        else:
            raise InvalidCipherTextError(algorytm)

        format_do_zapisu: tuple[str, str, str] = (decrypted_tekst,
                                                  algorytm,
                                                  self.historia.dodaj_czas())
        self.historia.dodaj(self.plik.json_maker(format_do_zapisu))
        self.dodaj_zdanie_do_pliku(decrypted_tekst)

        return decrypted_tekst

    def dodaj_zdanie_do_pliku(self, zdanie: str)-> None:
        """
         Writes the given text to a file specified in Settings.

         Args:
             zdanie (str): The text to be written to the file.
         """
        with open(Settings.save_path, "w", encoding="utf-8") as plik:
            plik.write(zdanie)

    def odkoduj_z_pliku(self, file_path=Settings.decode_filepath)-> str:
        """
        Decodes text from a JSON file using the stored algorithm.

        Returns:
            str: The encrypted text.

        Raises:
            InvalidCipherTextError: If an unsupported cipher algorithm is specified.
        """
        plik = self.plik.json_loader(file_path)
        slownik_pliku = self.plik.json_handler(plik)
        zdanie_zakodowane = slownik_pliku[0]
        algorytm = slownik_pliku[1]
        timestamp = slownik_pliku[2]

        match algorytm:
            case "ROT13":
                encrypted = self.algorytm_rot_13.decrypt(zdanie_zakodowane)
                format_do_zapisu = (encrypted, algorytm, timestamp)
                self.historia.dodaj(self.plik.json_maker(format_do_zapisu))
                return encrypted

            case "ROT47":
                encrypted = self.algorytm_rot_47.decrypt(zdanie_zakodowane)
                format_do_zapisu = (encrypted, algorytm, timestamp)
                self.historia.dodaj(self.plik.json_maker(format_do_zapisu))
                return encrypted

            case _:
                raise InvalidCipherTextError(algorytm)

