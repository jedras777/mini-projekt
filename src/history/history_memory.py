from datetime import datetime

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
        if not self.history:
            print("historia jest pusta")
        else:
            for x, i in self.history.items():
                print(f"{x}=> {i}")

    def zapisz_historie(self, sciezka: str)-> None:
        with open(sciezka, "w", encoding="utf-8") as plik:
            for x, i in self.history.items():
                plik.write((str(x) + "=>" + str(i) + "\n"))
        plik.close()


