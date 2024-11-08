import json

#plik = r"C:\Users\jendr\Desktop\json_test.txt"
historia = r"C:\Users\jendr\Desktop\historia_mini_projektu.txt"


def json_loader(sciezka: str)-> dict:
    with open(sciezka) as json_file:
        data = json.load(json_file)
    return data
def json_handler(slownik: dict)-> tuple:
   text = slownik["text"]
   algorithm = slownik["algorithm"]
   timestamp = slownik["timestamp"]
   return text, algorithm, timestamp

def json_maker(krotka: tuple)-> dict:
    slownik = {}
    slownik["text"] = krotka[0]
    slownik["algorithm"] = krotka[1]
    slownik["timestamp"] = krotka[2]
    return slownik

# elo = json_handler(plik)
# elo1 = json_maker(elo)
# elo = json_loader(plik)

