"""InvalidCipherTextError
- FileOperationError
- InvalidMenuChoiceError
 """

class InvalidCipherTextError(Exception):
    def __init__(self, algorytm):
        self.algorytm = algorytm
    def __str__(self):
        return f"NIE ZNAM TAKIEGO ALGORYTMU ERROR:{self.algorytm}"

class FileOperationError(Exception):
    def __init__(self, sciezka):
        self.sciezka = sciezka
    def __str__(self):
        return f"NIE MA TAKIEJ SCIEZKI ERROR:{self.sciezka}"

class InvalidMenuChoice(Exception):
    def __init__(self, choice):
        self.choice = choice
    def __str__(self):
        return f"NIE MA TAKIEJ SCIEZKI ERROR:{self.choice}"