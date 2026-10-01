from begruessung import greet


def test_einfacher_name():
    assert greet("Bob") == "Hello, Bob."

def test_geschrieener_name():
    assert greet("JERRY") == "HELLO JERRY!"    

def test_zwei_namen():
    assert greet(["Jill", "Jane"]) == "Hello, Jill and Jane."

def test_mehrere_namen_mit_oxford_komma():
    assert greet(["Amy", "Brian", "Charlotte"]) == "Hello, Amy, Brian, and Charlotte."

def test_normale_und_geschrieene_namen_gemischt():
    assert greet(["Amy", "BRIAN", "Charlotte"]) == "Hello, Amy and Charlotte. AND HELLO BRIAN!"    

def test_eintrag_mit_komma_wird_aufgeteilt():
    assert greet(["Bob", "Charlie, Dianne"]) == "Hello, Bob, Charlie, and Dianne."    

def test_komma_in_anfuehrungszeichen_bleibt_erhalten():
    assert greet(["Bob", "\"Charlie, Dianne\""]) == "Hello, Bob and Charlie, Dianne."    