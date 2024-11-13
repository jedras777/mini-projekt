from datetime import datetime
from src.file_handlers.json_handler import *
class Informacja:
    def __init__(self, pliczek: dict):
        self.pliczek = json_handler(pliczek)
        self.text = self.pliczek[0]
        self.algorithm = self.pliczek[1]
        self.timestamp = self.pliczek[2]
        # self.czas = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self)-> str:
        return f"czas: {self.timestamp}, tresc: {self.text}, format: {self.algorithm}"

class History_Of_Coding_Decoding:
    def __init__(self):
        self.history = {}

    def dodaj_czas(self)-> str:
        czas = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return czas
    def dodaj(self, obiekt: object)-> None:
        liczba = len(self.history)
        if self.history == {}:
            liczba += 1
            self.history[liczba] = obiekt
        else:
            liczba += 1
            self.history[liczba] = obiekt

    def pokaz_historie(self):
        for x, i in self.history.items():
            print(f"{x}=> {i}")

    def zapisz_historie(self, sciezka: str)-> None:
        with open(sciezka, "w", encoding="utf-8") as plik:
            for x, i in self.history.items():
                plik.write((str(x) + "=>" + str(i) + "\n"))
        plik.close()



# elo = Informacja(plik)
# historia.dodaj(elo)
# historia.pokaz_historie()

