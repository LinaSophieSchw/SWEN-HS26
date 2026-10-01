from passwords import is_password_valid


def test_gueltiges_passwort():
    assert is_password_valid("Abcdef12#") is True


def test_zu_kurzes_passwort():
    assert is_password_valid("Ab1#2") == "Password must be at least 8 characters"

def test_zu_wenige_ziffern():
    assert is_password_valid("Abcdefg1#") == "The password must contain at least 2 numbers"

def test_mehrere_fehler_gleichzeitig():
    assert is_password_valid("Abc#") == (
        "Password must be at least 8 characters\n"
        "The password must contain at least 2 numbers"
    )

def test_kein_grossbuchstabe():
    assert is_password_valid("abcdef12#") == "password must contain at least one capital letter"

def test_kein_sonderzeichen():
    assert is_password_valid("Abcdef123") == "password must contain at least one special character"    