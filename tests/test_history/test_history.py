
from datetime import datetime

import pytest

from src.history.history_memory import History_Of_Coding_Decoding

@pytest.fixture
def history_instance():
    """Fixture tworząca instancję klasy do testów."""
    return History_Of_Coding_Decoding()

def test_dodaj(history_instance):
    """Test dodawania obiektu do historii."""
    history_instance.dodaj("Testowy obiekt 1")
    history_instance.dodaj("Testowy obiekt 2")

    assert len(history_instance.history) == 2
    assert history_instance.history[1] == "Testowy obiekt 1"
    assert history_instance.history[2] == "Testowy obiekt 2"

def test_pokaz_historie(history_instance, capsys):
    """Test wyświetlania historii w konsoli."""
    history_instance.dodaj("Obiekt 1")
    history_instance.dodaj("Obiekt 2")
    history_instance.pokaz_historie()

    captured = capsys.readouterr()
    assert "1=> Obiekt 1" in captured.out
    assert "2=> Obiekt 2" in captured.out

def test_zapisz_historie(history_instance, tmp_path):
    """Test zapisywania historii do pliku."""
    history_instance.dodaj("Pierwszy obiekt")
    history_instance.dodaj("Drugi obiekt")


    # Ścieżka tymczasowego pliku
    file_path = tmp_path / "historia.txt"
    history_instance.zapisz_historie(str(file_path))

    # Odczyt pliku i sprawdzenie zawartości
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    assert "1=>Pierwszy obiekt\n" in content
    assert "2=>Drugi obiekt\n" in content

def test_dodaj_czas(history_instance):
    """Test dodawania aktualnego czasu."""
    mock_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = history_instance.dodaj_czas()

    assert result == mock_time
