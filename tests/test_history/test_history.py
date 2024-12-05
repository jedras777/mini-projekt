from datetime import datetime
from pathlib import Path

import pytest
from _pytest.capture import CaptureFixture

from src.history.history_memory import HistoryOfCodingDecoding


@pytest.fixture
def history_instance():
    """
    Fixture creating an instance of HistoryOfCodingDecoding for tests.

    Returns:
        HistoryOfCodingDecoding: A fresh instance for testing.
    """
    return HistoryOfCodingDecoding()


def test_dodaj(history_instance: HistoryOfCodingDecoding):
    """
    Test adding objects to history.
    """
    history_instance.dodaj("Testowy obiekt 1")
    history_instance.dodaj("Testowy obiekt 2")

    assert len(history_instance.history) == 2
    assert history_instance.history[1] == "Testowy obiekt 1"
    assert history_instance.history[2] == "Testowy obiekt 2"


def test_pokaz_historie(
    history_instance: HistoryOfCodingDecoding, capsys: CaptureFixture
):
    """
    Test displaying history in console.
    """
    history_instance.dodaj("Obiekt 1")
    history_instance.dodaj("Obiekt 2")
    history_instance.pokaz_historie()

    captured = capsys.readouterr()
    assert "1=> Obiekt 1" in captured.out
    assert "2=> Obiekt 2" in captured.out


def test_zapisz_historie(history_instance: HistoryOfCodingDecoding, tmp_path: Path):
    """
    Test saving history to a file.
    """
    history_instance.dodaj("Pierwszy obiekt")
    history_instance.dodaj("Drugi obiekt")

    file_path = tmp_path / "historia.txt"
    history_instance.zapisz_historie(str(file_path))

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    assert "1=>Pierwszy obiekt\n" in content
    assert "2=>Drugi obiekt\n" in content


def test_dodaj_czas(history_instance: HistoryOfCodingDecoding):
    """
    Test adding current timestamp.
    """
    mock_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = history_instance.dodaj_czas()

    assert result == mock_time
