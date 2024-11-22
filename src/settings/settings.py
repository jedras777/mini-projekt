from dataclasses import dataclass
from pathlib import Path
ROOTPATH = Path(__file__).parent.parent

@dataclass
class Settings:
    decode_filepath: str = ROOTPATH / "decode.json"
    save_path: str = ROOTPATH / "save.txt"

print(Settings.decode_filepath)