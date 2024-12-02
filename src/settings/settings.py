from dataclasses import dataclass
from pathlib import Path

ROOTPATH = Path(__file__).parent.parent
TESTPATH = Path(__file__).parent.parent.parent

@dataclass
class Settings:
    decode_filepath: str = ROOTPATH / "decode.json"
    save_path: str = ROOTPATH / "save.txt"
    save_history_path: str = ROOTPATH / "history.txt"
    test_path: str = TESTPATH / r"tests/test_facade/save_test.txt"

print(Settings.decode_filepath)
print(Settings.save_history_path)
print(Settings.save_path)
