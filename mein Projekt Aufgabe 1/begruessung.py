def namen_verbinden(namen):
    """Verbindet eine Liste von Namen zu einem Text,
    z.B. ["Amy", "Brian", "Charlotte"] -> "Amy, Brian, and Charlotte"."""
    if len(namen) == 1:
        return namen[0]
    if len(namen) == 2:
        return f"{namen[0]} and {namen[1]}"
    # alle ausser dem letzten mit Komma verbinden, den letzten mit ", and" anhängen
    alle_ausser_letzter = ", ".join(namen[:-1])
    letzter_name = namen[-1]
    return f"{alle_ausser_letzter}, and {letzter_name}"

def namen_aufteilen(namensliste):
    """Teilt Einträge mit Komma in einzelne Namen auf.
    Einträge in Anführungszeichen werden nicht aufgeteilt."""
    einzelne_namen = []
    for eintrag in namensliste:
        if eintrag.startswith('"') and eintrag.endswith('"'):
            # Requirement 8: Komma ist "escapt" -> nur Anführungszeichen entfernen
            einzelne_namen.append(eintrag.strip('"'))
        elif "," in eintrag:
            # Requirement 7: beim Komma aufteilen und Leerzeichen entfernen
            for teil in eintrag.split(","):
                einzelne_namen.append(teil.strip())
        else:
            einzelne_namen.append(eintrag)
    return einzelne_namen

def greet(name):
    # Requirement 2: kein Name angegeben
    if name is None:
        return "Hello, my friend."

    # einzelnen Namen als Liste mit einem Eintrag behandeln
    if type(name) != list:
        name = [name]

    # Requirement 7: Einträge mit Komma aufteilen
    alle_namen = namen_aufteilen(name)

    # Requirement 6: Namen in normale und geschrieene aufteilen
    normale_namen = []
    geschrieene_namen = []
    for einzelner_name in alle_namen:
        if einzelner_name.isupper():
            geschrieene_namen.append(einzelner_name)
        else:
            normale_namen.append(einzelner_name)

    # nur normale Namen (Requirement 1, 4, 5, 7)
    if not geschrieene_namen:
        return f"Hello, {namen_verbinden(normale_namen)}."

    # nur geschrieene Namen (Requirement 3)
    if not normale_namen:
        return f"HELLO {namen_verbinden(geschrieene_namen).upper()}!"

    # beides gemischt (Requirement 6)
    return f"Hello, {namen_verbinden(normale_namen)}. AND HELLO {namen_verbinden(geschrieene_namen).upper()}!"