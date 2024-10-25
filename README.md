# Ciphering Project

Mini-projekt szyfrujący wykorzystujący wzorzec Facade i dobre praktyki programowania w Pythonie.

## Opis projektu

Aplikacja konsolowa umożliwiająca szyfrowanie i deszyfrowanie tekstu przy użyciu algorytmów ROT13 i ROT47. 
System wykorzystuje wzorzec projektowy Facade do zapewnienia prostego interfejsu użytkownika, jednocześnie enkapsulując złożoną logikę biznesową.

## Funkcjonalności

1. Szyfrowanie tekstu (ROT13/ROT47)
2. Zapisywanie zaszyfrowanych tekstów do pliku
3. Odczytywanie i deszyfrowanie tekstów z pliku
4. Wyświetlanie historii operacji
5. Menu konsolowe do obsługi wszystkich funkcji

## Struktura projektu

```
src/
  ciphers/
    __init__.py
    base_cipher.py      # Klasa bazowa dla szyfrów
    rot13_cipher.py
    rot47_cipher.py
  file_handlers/
    __init__.py
    json_handler.py     # Obsługa zapisu/odczytu JSON
  menu/
    __init__.py
    console_menu.py     # Menu konsolowe
  history/
    __init__.py
    memory_history.py   # Historia w pamięci
  facade/
    __init__.py
    cipher_facade.py    # Główna fasada systemu
  exceptions/
    __init__.py
    cipher_exceptions.py # Własne wyjątki
  main.py
tests/
  __init__.py
  test_ciphers/
  test_file_handlers/
  test_menu/
  test_history/
  test_facade/
.pre-commit-config.yaml
pyproject.toml
README.md
```

## Wymagania techniczne

### Podstawowe wymagania
- Python 3.8+
- Pytest
- Ruff
- Pre-commit hooks

### Instalacja

1. Sklonuj repozytorium:
```bash
git clone <repository-url>
```

2. Stwórz i aktywuj wirtualne środowisko:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Zainstaluj zależności:
```bash
pip install -r requirements.txt
```

4. Zainstaluj pre-commit hooks:
```bash
pre-commit install
```

### Uruchomienie
```bash
python src/main.py
```

### Testy
```bash
pytest
pytest --cov=src tests/  # z pokryciem kodu
```

## Wymagania projektowe

### Wzorce projektowe
- Wymagane: Facade
- Opcjonalne: Dodatkowe wzorce (np. Abstract Factory)

### Obsługa błędów
Minimum 3 własne wyjątki:
- InvalidCipherTextError
- FileOperationError
- InvalidMenuChoiceError

### Format pliku JSON
```json
{
  "text": "zaszyfrowany_tekst",
  "algorithm": "ROT13/ROT47",
  "timestamp": "2024-10-25 14:30:00"
}
```

### Wymagania kodu
1. Pełne typowanie (type hints)
2. Docstringi zgodne z PEP 257
3. Walidacja danych wejściowych
4. Pokrycie testami minimum 80%

## Dodatkowe wyzwania (opcjonalne)
1. GUI w tkinter
2. Zapis historii do pliku
3. Automatyczna detekcja typu szyfru
4. 100% pokrycia testami
5. Implementacja TDD

## Kryteria oceny
1. Poprawność implementacji wzorca Facade
2. Czystość i organizacja kodu
3. Prawidłowa obsługa błędów
4. Pokrycie testami
5. Historia commitów (conventional commits)
6. Poprawność PR/MR

## Narzędzia
### Ruff
Konfiguracja w `pyproject.toml` dla:
- Formatowania kodu
- Sprawdzania importów
- Weryfikacji type hints

### Pre-commit
Podstawowa konfiguracja sprawdzająca:
- Formatowanie kodu
- Importy
- Type hints

### Pytest-cov
Do weryfikacji pokrycia kodu testami

## Pomoc
W razie pytań lub problemów, utwórz issue w repozytorium lub skontaktuj się z mentorem.

## Licencja
[MIT](https://choosealicense.com/licenses/mit/)
