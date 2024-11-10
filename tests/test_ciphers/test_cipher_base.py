import pytest
from src.ciphers.base_cypher import robimy_slowniki

def test_towrzenie_slownika():
    assert robimy_slowniki("abc") == {1:"a",2:"b",3:"c"}
