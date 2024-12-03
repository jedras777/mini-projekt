
class CustomBaseError(Exception):
    """
    Base class for custom exceptions with parameterized error messages.

    Allows creating specific error messages with additional context.

    Attributes:
         message (str): Default error message template.
         param (str): Additional error context parameter.
    """
    message = f"Bazowy błąd:"
    def __init__(self, param: str) -> None:
        """
        Initialize custom error with specific parameter.

        Args:
            param (str): Additional error description or context.
        """
        self.param = param

    def __str__(self)-> str:
        """
        Generate formatted error message.

        Returns:
             str: Detailed error description combining message and parameter.
        """
        return f"{self.message} {self.param}"


class InvalidCipherTextError(CustomBaseError):
    """
    Exception raised when an invalid cipher algorithm is specified.

    Inherits from CustomBaseError with a specific error message for
    cipher-related issues.
    """
    message = "Nie ma takiego algorytmu"

class FileOperationError(CustomBaseError):
    """
    Exception raised for invalid file operation attempts.

    Indicates issues with file paths or file system interactions.
    """
    message = "Niepoprawna ścieżka do pliku"

class InvalidMenuChoice(CustomBaseError):
    """
    Exception raised for incorrect menu selections.

    Signals that a user has made an unsupported menu choice.
    """
    message = "Nie ma takiego wyboru"

class FileNotExistError(CustomBaseError):
    """
    Exception raised when attempting to access a non-existent file.

    Provides clear indication of file unavailability.
    """
    message = "Nie ma takiego pliku"
