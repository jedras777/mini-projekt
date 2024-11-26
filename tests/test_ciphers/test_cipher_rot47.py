from src.ciphers.rot47_cypher import ROT47Cipher



def test_encrypt_method():
    klasa = ROT47Cipher()
    assert klasa.encrypt("elo") == "6=@"
    assert klasa.encrypt("ELL") == "t{{"
    assert klasa.encrypt("Python123") == "!JE9@?`ab"

def test_decrypt_method():
    klasa = ROT47Cipher()
    assert klasa.decrypt("hello") == "96==@"
    assert klasa.decrypt("HELLO") == "wt{{~"
    assert klasa.decrypt("Python123") == "!JE9@?`ab"

def test_symmetry():
    klasa = ROT47Cipher()
    decrypted = klasa.decrypt("elo")
    encrypted = klasa.encrypt(decrypted)
    assert encrypted == "elo"

def test_empty_string():
    klasa = ROT47Cipher()
    assert klasa.encrypt("") == ""
    assert klasa.decrypt("") == ""