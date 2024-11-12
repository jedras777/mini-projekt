import pytest
import json
from src.file_handlers.json_handler import json_loader,json_maker,json_handler

sample_json = {
    "text": "elo, ELO",
    "algorithm": "ROT13",
    "timestamp": "2024-11-11T00:00:00"
}

@pytest.fixture
def create_sample_json_file(tmpdir):
    """Fixture to create a sample JSON file for testing."""
    file_path = tmpdir.join("sample.json")
    with open(file_path, 'w') as json_file:
        json.dump(sample_json, json_file, indent=4)
    return str(file_path)  # Return the file path as a string

# Test for json_loader
def test_json_loader(create_sample_json_file):
    file_path = create_sample_json_file
    loaded_data = json_loader(file_path)
    assert loaded_data == sample_json, f"Expected {sample_json}, but got {loaded_data}"

# Test for json_handler
def test_json_handler():
    text, algorithm, timestamp = json_handler(sample_json)
    assert text == "elo, ELO"
    assert algorithm == "ROT13"
    assert timestamp == "2024-11-11T00:00:00"

# Test for json_maker
def test_json_maker():
    data_tuple = ("elo, ELO", "ROT13", "2024-11-11T00:00:00")
    expected_dict = sample_json
    created_dict = json_maker(data_tuple)
    assert created_dict == expected_dict, f"Expected {expected_dict}, but got {created_dict}"
