import pytest
from unittest.mock import patch
from src.menu.console_menu import Menu

@pytest.fixture
def menu_instance():
    """Fixture to create a Menu instance."""
    return Menu()

