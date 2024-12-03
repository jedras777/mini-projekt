from unittest.mock import patch

import pytest
from _pytest.capture import CaptureFixture

from src.menu.console_menu import Menu

menu_text = [
    "--------Menu----------",
    "1.zakoduj zdanie wpisane przez siebie",
    "2.zdekoduj zdanie wpisane przez siebie",
    "3.pokaz historie",
    "4.zapisz historię do pliku",
    "5.zdekoduj plik json",
    "6.zakoncz"
]

cipher_menu = [
    "1.rot13",
    "2.rot47"
]
algorytm_rot13 = "ROT13"
algorytm_rot47 = "ROT47"

@pytest.fixture
def mock_menu():
    """
    Fixture to create a Menu instance for testing.

    Returns:
        Menu: A new Menu instance for each test.
    """
    return Menu()

def test_show_menu(mock_menu: Menu, capsys: CaptureFixture):
    """
    Fixture to create a Menu instance for testing.

    Returns:
        Menu: A new Menu instance for each test.
    """
    with patch("builtins.input", return_value="6"):
        with pytest.raises(SystemExit):
            mock_menu.show_menu()
    captured = capsys.readouterr()
    assert captured.out == "\n".join(menu_text) + "\n"

def test_wybor_1_1(mock_menu: Menu, capsys: CaptureFixture):
    """
    Test ROT13 encoding functionality.

    Validates:
    - Correct navigation through menu
    - Correct ROT13 encoding of input
    - Proper menu display after encoding

    Args:
        mock_menu (Menu): The Menu instance to test
        capsys (CaptureFixture): Pytest capture fixture for stdout
    """
    wybory = ["1","1","elo","6"]
    with patch("builtins.input", side_effect=wybory):
        with pytest.raises(SystemExit):
            mock_menu.show_menu()
    expected_output = "\n".join(menu_text)+"\n" +"\n".join(cipher_menu) +"\n" + 'ryb\n' + "\n".join(menu_text) + "\n"
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_wybor_1_2(mock_menu: Menu, capsys: CaptureFixture):
    """
    Test ROT47 encoding functionality.

    Validates:
    - Correct navigation through menu
    - Correct ROT47 encoding of input
    - Proper menu display after encoding

    Args:
        mock_menu (Menu): The Menu instance to test
        capsys (CaptureFixture): Pytest capture fixture for stdout
    """
    wybory = ["1","2","elo","6"]
    with patch("builtins.input", side_effect=wybory):
        with pytest.raises(SystemExit):
            mock_menu.show_menu()
    expected_output = "\n".join(menu_text)+"\n" +"\n".join(cipher_menu) +"\n" + '6=@\n' + "\n".join(menu_text) + "\n"
    captured = capsys.readouterr()
    assert captured.out == expected_output

def test_wybor_1_wrong_number(mock_menu: Menu, capsys: CaptureFixture):
    """
    Test error handling for invalid cipher selection during encoding.

    Validates:
    - Proper error message for invalid cipher selection
    - Correct menu navigation
    - System continues to function after invalid input

    Args:
        mock_menu (Menu): The Menu instance to test
        capsys (CaptureFixture): Pytest capture fixture for stdout
    """
    wybory = ["1", "8", "6"]
    with patch("builtins.input", side_effect=wybory):
        with pytest.raises(SystemExit):
            mock_menu.show_menu()
    expected_output = "\n".join(menu_text)+"\n" +"\n".join(cipher_menu) +"\n" + 'Nie ma takiego wyboru 8\n' + "\n".join(menu_text) + "\n"
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_wybor_2_1(mock_menu: Menu, capsys: CaptureFixture):
    """
    Test ROT13 decoding functionality.

    Validates:
    - Correct navigation through menu
    - Correct ROT13 decoding of input
    - Proper menu display after decoding

    Args:
        mock_menu (Menu): The Menu instance to test
        capsys (CaptureFixture): Pytest capture fixture for stdout
    """
    wybory = ["2","1","elo","6"]
    with patch("builtins.input", side_effect=wybory):
        with pytest.raises(SystemExit):
            mock_menu.show_menu()
    expected_output = "\n".join(menu_text)+"\n" +"\n".join(cipher_menu) +"\n" + 'ryb\n' + "\n".join(menu_text) + "\n"
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_wybor_2_2(mock_menu: Menu, capsys: CaptureFixture):
    """
    Test ROT47 decoding functionality.

    Validates:
    - Correct navigation through menu
    - Correct ROT47 decoding of input
    - Proper menu display after decoding

    Args:
        mock_menu (Menu): The Menu instance to test
        capsys (CaptureFixture): Pytest capture fixture for stdout
    """
    wybory = ["2","2","elo","6"]
    with patch("builtins.input", side_effect=wybory):
        with pytest.raises(SystemExit):
            mock_menu.show_menu()
    expected_output = "\n".join(menu_text)+"\n" +"\n".join(cipher_menu) +"\n" + '6=@\n' + "\n".join(menu_text) + "\n"
    captured = capsys.readouterr()
    assert captured.out == expected_output

def test_wybor_2_wrong_number(mock_menu: Menu, capsys: CaptureFixture):
    """
    Test error handling for invalid cipher selection during decoding.

    Validates:
    - Proper error message for invalid cipher selection
    - Correct menu navigation
    - System continues to function after invalid input

    Args:
        mock_menu (Menu): The Menu instance to test
        capsys (CaptureFixture): Pytest capture fixture for stdout
    """
    wybory = ["2", "8", "6"]
    with patch("builtins.input", side_effect=wybory):
        with pytest.raises(SystemExit):
            mock_menu.show_menu()
    expected_output = "\n".join(menu_text)+"\n" +"\n".join(cipher_menu) +"\n" + 'Nie ma takiego wyboru 8\n' + "\n".join(menu_text) + "\n"
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_wybor_3(mock_menu: Menu, capsys: CaptureFixture):
    """
    Test history display functionality.

    Validates:
    - Correct handling of empty history
    - Proper menu navigation
    - Correct error message for empty history

    Args:
        mock_menu (Menu): The Menu instance to test
        capsys (CaptureFixture): Pytest capture fixture for stdout
    """
    wybory = ["3", "6"]
    with patch("builtins.input", side_effect=wybory):
        with pytest.raises(SystemExit):
            mock_menu.show_menu()
    expected_output = "\n".join(menu_text)+"\n" + 'historia jest pusta\n' + "\n".join(menu_text) + "\n"
    captured = capsys.readouterr()
    assert captured.out == expected_output
