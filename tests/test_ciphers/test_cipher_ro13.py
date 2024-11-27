from src.ciphers.rot13_cipher import ROT13Cipher



def test_encrypt_method():
    klasa = ROT13Cipher()
    assert klasa.encrypt("hello") == "uryyb"
    assert klasa.encrypt("HELLO") == "URYYB"
    assert klasa.encrypt("Python123") == "Clguba123"

def test_decrypt_method():
    klasa = ROT13Cipher()
    assert klasa.decrypt("hello") == "uryyb"
    assert klasa.decrypt("HELLO") == "URYYB"
    assert klasa.decrypt("Python123") == "Clguba123"

def test_symmetry():
    klasa = ROT13Cipher()
    decrypted = klasa.decrypt("elo")
    encrypted = klasa.encrypt(decrypted)
    assert encrypted == "elo"

def test_empty_string():
    klasa = ROT13Cipher()
    assert klasa.encrypt("") == ""
    assert klasa.decrypt("") == ""

def test_non_alpha_characters():
    cipher = ROT13Cipher()
    text = r"1234!@#$%^&*()_+[]{};':\",./<>?"
    assert cipher.encrypt(text) == text
    assert cipher.decrypt(text) == text

def test_large_input():
    klasa = ROT13Cipher()
    text = "a" * 1000  # 1000 znaków 'a'
    encrypted = klasa.encrypt(text)
    decrypted = klasa.decrypt(encrypted)
    assert decrypted == text

def test_non_latin_characters():
    klasa = ROT13Cipher()
    text = "Zażółć gęślą jaźń"
    encrypted = klasa.encrypt(text)
    decrypted = klasa.decrypt(encrypted)
    assert decrypted == text

def test_encrypting_encrypted_text():
    klasa = ROT13Cipher()
    text = "Example Text"
    encrypted_once = klasa.encrypt(text)
    encrypted_twice = klasa.encrypt(encrypted_once)
    assert encrypted_twice == text
