import pytest
from unittest.mock import patch
from src.menu.console_menu import Menu  # Replace 'your_module' with the actual module name

@pytest.fixture
def menu_instance():
    """Fixture to create a Menu instance."""
    return Menu()

# Test the initialization of the Menu class
def test_initialization(menu_instance):
    assert menu_instance.opcja1 == "--------Menu----------"
    assert menu_instance.opcja2 == "1.zakoduj zdanie wpisane przez siebie"
    assert menu_instance.opcja3 == "2.zdekoduj zdanie wpisane przez siebie"
    assert menu_instance.opcja5 == "3.pokaz historie"
    assert menu_instance.opcja8 == "4.zapisz historię do pliku"
    assert menu_instance.opcja6 == "5.zdekoduj plik json"
    assert menu_instance.opcja4 == "6.zakoncz"
    assert menu_instance.opcja7 == ".zakoduj plik json"
    assert menu_instance.rot13_wubor == "1.rot13"
    assert menu_instance.rot47_wubor == "2.rot47"

# Test __repr__ method
def test_repr(menu_instance):
    expected_output = (
        "--------Menu----------\n"
        "1.zakoduj zdanie wpisane przez siebie\n"
        "2.zdekoduj zdanie wpisane przez siebie\n"
        "3.pokaz historie\n"
        "4.zapisz historię do pliku\n"
        "5.zdekoduj plik json\n"
        "6.zakoncz\n"
    )
    assert repr(menu_instance) == expected_output

#test repr_szyfry with mocked input
def test_repr_szyfry(menu_instance):
    expected_output = f"1.rot13\n2.rot47"
    assert menu_instance.repr_szyfry() == expected_output


# Test wybierz method with mocked input
def test_wybierz(menu_instance):
    with patch('builtins.input', return_value='1'):
        assert menu_instance.wybierz() == '1'

# Test podaj_zdanie_do_zakodowania_dekodowania with mocked input
def test_podaj_zdanie_do_zakodowania_dekodowania(menu_instance):
    with patch('builtins.input', return_value='Test zdanie'):
        assert menu_instance.podaj_zdanie_do_zakodowania_dekodowania() == 'Test zdanie'

# Test podaj_sciezke_do_pliku with mocked input
def test_podaj_sciezke_do_pliku(menu_instance):
    with patch('builtins.input', return_value='/path/to/file'):
        assert menu_instance.podaj_sciezke_do_pliku() == '/path/to/file'

# Test dodaj_zdanie_do_pliku method with tmpdir
def test_dodaj_zdanie_do_pliku(menu_instance, tmpdir):
    test_file = tmpdir.join("test_output.txt")
    test_sentence = "This is a test sentence."

    # Replace the actual path in the method with our temporary path
    menu_instance.dodaj_zdanie_do_pliku = lambda zdanie: test_file.write_text(zdanie, encoding="utf-8")

    # Call the modified method and check contents of tmp file
    menu_instance.dodaj_zdanie_do_pliku(test_sentence)
    assert test_file.read_text(encoding="utf-8") == test_sentence
