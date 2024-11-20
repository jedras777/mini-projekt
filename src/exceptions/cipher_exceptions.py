"""InvalidCipherTextError
- FileOperationError
- InvalidMenuChoiceError
 """

class InvalidCipherTextError(Exception):
    def __init__(self, algorytm):
        self.algorytm = algorytm
    def __str__(self):
        return f"NIE ZNAM TAKIEGO ALGORYTMU:{self.algorytm}"