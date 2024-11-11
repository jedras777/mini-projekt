from src.ciphers.rot47_cypher import szyfrowanie_rot47,deszyfrowanie_rot47

def test_rot_47_ciphering():
    zdanie = szyfrowanie_rot47("eloelo")
    assert zdanie == "6=@6=@"

def test_rot_47_ciphering_empty():
    zdanie = szyfrowanie_rot47("")
    assert zdanie == ""

def test_rot_47_ciphering_whitespaces_and_spoecial_characters():
    zdanie = szyfrowanie_rot47("   !@#$!#$@!!12341325")
    assert zdanie == "   PoRSPRSoPP`abc`bad"

def test_rot_47_deciphering():
    zdanie = deszyfrowanie_rot47("eloelo")
    assert zdanie == "6=@6=@"

def test_rot_47_deciphering_empty():
    zdanie = deszyfrowanie_rot47("")
    assert zdanie == ""
def test_rot_47_deciphering_whitespaces_and_spoecial_characters():
    zdanie = deszyfrowanie_rot47("   !@#$!#$@!!12341325")
    assert zdanie == "   PoRSPRSoPP`abc`bad"

def test_rot47_symetry():
    tekst = "eloelo"
    zakodowane = szyfrowanie_rot47(tekst)
    odkodowane = szyfrowanie_rot47(zakodowane)
    assert tekst == odkodowane