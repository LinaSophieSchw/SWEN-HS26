
SONDERZEICHEN = "!@#$%^&*()-_=+[]{};:,.<>?/\\|~"


def is_password_valid(passwort):
    fehler = []

    # Requirement 1: Mindestlänge
    if len(passwort) < 8:
        fehler.append("Password must be at least 8 characters")

    # Requirement 2: mindestens 2 Ziffern
    anzahl_ziffern = 0
    for zeichen in passwort:
        if zeichen.isdigit():
            anzahl_ziffern += 1
    if anzahl_ziffern < 2:
        fehler.append("The password must contain at least 2 numbers")

    # Requirement 4: mindestens ein Grossbuchstabe
    hat_grossbuchstaben = False
    for zeichen in passwort:
        if zeichen.isupper():
            hat_grossbuchstaben = True
    if not hat_grossbuchstaben:
        fehler.append("password must contain at least one capital letter")

    # Requirement 5: mindestens ein Sonderzeichen
    hat_sonderzeichen = False
    for zeichen in passwort:
        if zeichen in SONDERZEICHEN:
            hat_sonderzeichen = True
    if not hat_sonderzeichen:
        fehler.append("password must contain at least one special character")

    # Requirement 3: alle Fehler zusammen zurückgeben
    if fehler:
        return "\n".join(fehler)
    return True


if __name__ == "__main__":
    eingabe = input("Passwort eingeben: ")
    resultat = is_password_valid(eingabe)
    if resultat is True:
        print("Passwort ist gültig ✅")
    else:
        print("Passwort ist ungültig ❌")
        print(resultat)