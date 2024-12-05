from dataclasses import dataclass
from pathlib import Path

ROOTPATH = Path(__file__).parent.parent
TESTPATH = Path(__file__).parent.parent.parent


@dataclass
class Settings:
    """
    Configuration settings for file paths in the application.

    Attributes:
        ROOTPATH (ClassVar[Path]): Root directory path of the project.
        TESTPATH (ClassVar[Path]): Test directory path.
        decode_filepath (ClassVar[Path]): Path to the decode JSON file.
        save_path (ClassVar[Path]): Path to the save text file.
        save_history_path (ClassVar[Path]): Path to the history text file.
        test_path (ClassVar[Path]): Path to the test save file.
    """

    decode_filepath: str = ROOTPATH / "decode.json"
    save_path: str = ROOTPATH / "save.txt"
    save_history_path: str = ROOTPATH / "history.txt"
    test_path: str = TESTPATH / r"tests/test_facade/save_test.txt"


print(Settings.decode_filepath)
print(Settings.save_history_path)
print(Settings.save_path)
