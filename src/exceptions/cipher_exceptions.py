
class CustomBaseError(Exception):
    message = f"Bazowy błąd:"
    def __init__(self, param: str):
        self.param = param
    def __str__(self):
        return f"{self.message} {self.param}"


class InvalidCipherTextError(CustomBaseError):
    message = "Nie ma takiego algorytmu"

class FileOperationError(CustomBaseError):
    message = "Niepoprawna ścieżka do pliku"

class InvalidMenuChoice(CustomBaseError):
    message = "Nie ma takiego wyboru"

class FileNotExistError(CustomBaseError):
    message = "Nie ma takiego pliku"
