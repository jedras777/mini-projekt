from src.ciphers.rot13_cipher import szyfrowanie_rot13,deszyfrowanie_rot13

def test_rot_13_ciphering():
    zdanie = szyfrowanie_rot13("eloelo")
    assert zdanie == "rybryb"

def test_rot_13_ciphering_empty():
    zdanie = szyfrowanie_rot13("")
    assert zdanie == ""
def test_rot_13_ciphering_whitespaces_and_spoecial_characters():
    zdanie = szyfrowanie_rot13("    ,,,..._")
    assert zdanie == "    ,,,..._"

def test_rot_13_deciphering():
    zdanie = deszyfrowanie_rot13("eloelo")
    assert zdanie == "rybryb"

def test_rot_13_deciphering_empty():
    zdanie = deszyfrowanie_rot13("")
    assert zdanie == ""
def test_rot_13_deciphering_whitespaces_and_spoecial_characters():
    zdanie = deszyfrowanie_rot13("    ,,,..._")
    assert zdanie == "    ,,,..._"


def test_rot13_symetry():
    tekst = "eloelo"
    zakodowane = szyfrowanie_rot13(tekst)
    odkodowane = szyfrowanie_rot13(zakodowane)
    assert tekst == odkodowane