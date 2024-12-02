import pytest

from src.exceptions.cipher_exceptions import FileNotExistError, FileOperationError
from src.file_handlers.json_handler import Plik
from src.settings.settings import Settings

sample_json = {
  "text": "zaszyfrowany_tekst",
  "algorithm": "ROT13",
  "timestamp": "2024-10-25 14:30:00"
}



# Test for json_loader
def test_json_loader():
    klasa = Plik()
    loaded_data = klasa.json_loader(Settings.decode_filepath)
    assert loaded_data == sample_json, f"Expected {sample_json}, but got {loaded_data}"

# Test for json_handler
def test_json_handler():
    klasa = Plik()
    text, algorithm, timestamp = klasa.json_handler(sample_json)
    assert text == "zaszyfrowany_tekst"
    assert algorithm == "ROT13"
    assert timestamp == "2024-10-25 14:30:00"

# Test for json_maker
def test_json_maker():
    klasa = Plik()
    data_tuple = ("zaszyfrowany_tekst", "ROT13", "2024-10-25 14:30:00")
    expected_dict = sample_json
    created_dict = klasa.json_maker(data_tuple)
    assert created_dict == expected_dict, f"Expected {expected_dict}, but got {created_dict}"

def test_json_loader_empty_path():
    klasa = Plik()
    with pytest.raises(FileOperationError):
        klasa.json_loader("")

def test_json_loader_with_no_data_loaded():
    klasa = Plik()
    with pytest.raises(FileNotExistError):
        klasa.json_loader("elooo")


def test_json_handler_with_no_data_handled():
    klasa = Plik()
    pusty_slownik = {}
    invalid_slownik = {
    "text": "zaszyfrowany_tekst",
    "timestamp": "2024-10-25 14:30:00"
    }
    with pytest.raises(KeyError):
        klasa.json_handler(pusty_slownik)
        klasa.json_handler(invalid_slownik)


def test_json_maker_with_no_data_provided():
    klasa = Plik()
    krotka = ()
    incomplete_krotka = ("ello",)
    with pytest.raises(IndexError):
        klasa.json_maker(krotka)
        klasa.json_maker(incomplete_krotka)
#
# def test_json_loader_permission_error(tmp_path):
#     json_file = tmp_path / "restricted.json"
#     json_file.write_text('{"key": "value"}')
#     os.chmod(json_file, 0)  # Odebranie uprawnień
#
#     with pytest.raises(PermissionError):
#         Plik().json_loader(str(json_file))
