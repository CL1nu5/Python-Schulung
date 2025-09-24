import importlib.util

def reload_module():
    import src.aufgaben.kapitel_1_variablen.aufgabe_02_rechenoperationen as aufgaben
    importlib.reload(aufgaben)
    return aufgaben


def test_teil_aufgabe1():
    mod = reload_module()
    assert mod.addition == 20, "Das Ergebnis muss 20 sein."

def test_teil_aufgabe2():
    mod = reload_module()
    assert mod.subtraktion == 11, "Das Ergebnis muss 11 sein."

def test_teil_aufgabe3():
    mod = reload_module()
    assert mod.multiplikation == 42, "Das Ergebnis muss 42 sein."

def test_teil_aufgabe4():
    mod = reload_module()
    assert mod.division == 4, "Das Ergebnis muss 4 sein."

def test_teil_aufgabe5():
    mod = reload_module()
    assert mod.rest == 2, "Das Ergebnis muss 2 sein."

def test_teil_aufgabe6():
    mod = reload_module()
    assert mod.potenz == 256, "Das Ergebnis muss 256 sein."

def test_teil_aufgabe7():
    mod = reload_module()
    assert mod.ganzzahl_division == 5, "Das Ergebnis muss 5 sein."

def test_teil_aufgabe8():
    mod = reload_module()
    assert mod.klammerrechnung == 20, "Das Ergebnis muss 20 sein."

def test_teil_aufgabe9():
    mod = reload_module()
    assert mod.modulo_klammer == 3, "Das Ergebnis muss 3 sein."