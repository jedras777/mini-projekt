import json

#plik = r"C:\Users\jendr\Desktop\json_test.txt"
historia = r"C:\Users\jendr\Desktop\historia_mini_projektu.txt"


def json_loader(sciezka):
    with open(sciezka) as json_file:
        data = json.load(json_file)
    return data

def json_handler(dict):
   text = dict["text"]
   algorithm = dict["algorithm"]
   timestamp = dict["timestamp"]
   return text, algorithm, timestamp

def json_maker(tuple):
    slownik = {}
    slownik["text"] = tuple[0]
    slownik["algorithm"] = tuple[1]
    slownik["timestamp"] = tuple[2]
    return slownik

# elo = json_handler(plik)
# elo1 = json_maker(elo)
# elo = json_loader(plik)
# print(elo)