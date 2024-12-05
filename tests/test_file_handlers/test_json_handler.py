import pytest

# from src.exceptions.cipher_exceptions import FileNotExistError, FileOperationError
from src.file_handlers.json_handler import FileNotExistError, FileOperationError, Plik
from src.settings.settings import Settings

sample_json = {
    "text": "zaszyfrowany_tekst",
    "algorithm": "ROT13",
    "timestamp": "2024-10-25 14:30:00",
}


def test_json_loader():
    """
    Test JSON file loading functionality.
    """
    klasa = Plik()
    loaded_data = klasa.json_loader(Settings.decode_filepath)
    assert loaded_data == sample_json, f"Expected {sample_json}, but got {loaded_data}"


def test_json_handler():
    """
    Test JSON data handling functionality.
    """
    klasa = Plik()
    text, algorithm, timestamp = klasa.json_handler(sample_json)
    assert text == "zaszyfrowany_tekst"
    assert algorithm == "ROT13"
    assert timestamp == "2024-10-25 14:30:00"


def test_json_maker():
    """
    Test JSON creation functionality.
    """
    klasa = Plik()
    data_tuple = ("zaszyfrowany_tekst", "ROT13", "2024-10-25 14:30:00")
    expected_dict = sample_json
    created_dict = klasa.json_maker(data_tuple)
    assert (
        created_dict == expected_dict
    ), f"Expected {expected_dict}, but got {created_dict}"


def test_json_loader_empty_path():
    """
    Test JSON loader with empty file path.
    """
    klasa = Plik()
    with pytest.raises(FileOperationError):
        klasa.json_loader("")


def test_json_loader_with_no_data_loaded():
    """
    Test JSON loader with non-existent file path.
    """
    klasa = Plik()
    with pytest.raises(FileNotExistError):
        klasa.json_loader("elooo")


def test_json_handler_with_no_data_handled():
    """
    Test JSON handler with incomplete or invalid dictionary.
    """
    klasa = Plik()
    pusty_slownik = {}
    invalid_slownik = {"text": "zaszyfrowany_tekst", "timestamp": "2024-10-25 14:30:00"}
    with pytest.raises(KeyError):
        klasa.json_handler(pusty_slownik)
        klasa.json_handler(invalid_slownik)


def test_json_maker_with_no_data_provided():
    """
    Test JSON maker with incomplete or empty tuple.
    """
    klasa = Plik()
    krotka = ()
    incomplete_krotka = ("ello",)
    with pytest.raises(IndexError):
        klasa.json_maker(krotka)
        klasa.json_maker(incomplete_krotka)
