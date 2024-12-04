from datetime import datetime


class HistoryOfCodingDecoding:
    """
    Manages a history of coding and decoding operations.

    Tracks and stores cipher operations with unique identifiers and timestamps.

    Attributes:
        history (Dict[int, Any]): Dictionary storing operation records.
    """
    def __init__(self)-> None:
        """
        Initializes an empty history dictionary.
        """
        self.history = {}

    def dodaj_czas(self)-> str:
        """
        Generates a formatted timestamp.

        Returns:
            str: Current datetime in 'YYYY-MM-DD HH:MM:SS' format.
        """
        czas = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return czas

    def dodaj(self, obiekt: object)-> None:
        """
        Adds a new operation record to the history.

        Args:
            obiekt (Any): Operation record to be added.
        """
        liczba = len(self.history)
        if self.history == {}:
            liczba += 1
            self.history[liczba] = obiekt
        else:
            liczba += 1
            self.history[liczba] = obiekt

    def pokaz_historie(self)-> str:
        """
        Displays the entire operation history.

        Returns:
            Optional[str]: Formatted history string or None if empty.
        """
        if not self.history:
            return "historia jest pusta"
        else:
            tekst = ""
            for x, i in self.history.items():
                tekst += f"{x}=> {i}\n"
            return tekst

    def zapisz_historie(self, sciezka: str)-> None:
        """
        Writes the history to a file.

        Args:
            sciezka (str): File path to save history.
        """
        with open(sciezka, "w", encoding="utf-8") as plik:
            for x, i in self.history.items():
                plik.write((str(x) + "=>" + str(i) + "\n"))
        plik.close()


