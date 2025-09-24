import importlib

def reload_module():
    import src.aufgaben.kapitel_1_variablen.aufgabe_01_einfache_variablen as aufgaben
    importlib.reload(aufgaben)
    return aufgaben


def test_aufgabe1():
    mod = reload_module()
    assert isinstance(mod.name, str), "Die Variable 'name' muss ein String sein."


def test_aufgabe2():
    mod = reload_module()
    assert isinstance(mod.alter, (int, float)), "Die Variable 'alter' muss eine Zahl sein."


def test_aufgabe3():
    mod = reload_module()
    assert mod.summe == 42, "Die Summe von 15 + 27 muss 42 ergeben."


def test_aufgabe4():
    mod = reload_module()
    assert isinstance(mod.pi, float), "Die Variable 'pi' muss ein Float sein."
    assert abs(mod.pi - 3.14159) < 0.00001, "Die Variable 'pi' muss 3.14159 enthalten."


def test_aufgabe5():
    mod = reload_module()
    assert isinstance(mod.begrueßung, str), "Die Begrüßung muss ein String sein."
    assert mod.name in mod.begrueßung, "Die Begrüßung muss den Namen enthalten."
    assert mod.begrueßung.startswith("Hallo, mein Name ist"), "Die Begrüßung muss korrekt aufgebaut sein."