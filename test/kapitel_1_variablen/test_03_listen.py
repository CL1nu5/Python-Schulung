import importlib.util, sys

def reload_module():
    import src.aufgaben.kapitel_1_variablen.aufgabe_03_listen as aufgaben
    importlib.reload(aufgaben)
    return aufgaben


def test_teil_aufgabe1():
    mod = reload_module()
    assert isinstance(mod.zahlen, list), "'zahlen' muss eine Liste sein."
    assert mod.zahlen == [1, 2, 3, 4, 5], "Die Liste 'zahlen' soll [1, 2, 3, 4, 5] enthalten."


def test_teil_aufgabe2():
    mod = reload_module()
    assert mod.erstes_element == 1, "Das erste Element von [1, 2, 3, 4, 5] muss 1 sein."


def test_teil_aufgabe3():
    mod = reload_module()
    assert mod.letztes_element == 5, "Das letzte Element von [1, 2, 3, 4, 5] muss 5 sein."


def test_teil_aufgabe4():
    mod = reload_module()
    assert mod.zahlen[-1] == 6, "Nach Hinzufügen muss das letzte Element 6 sein."
    assert len(mod.zahlen) == 6, "Die Liste muss nach dem Anhängen 6 Elemente haben."


def test_teil_aufgabe5():
    mod = reload_module()
    assert mod.zahlen[1] == 99, "Das zweite Element der Liste muss 99 sein."


def test_teil_aufgabe6():
    mod = reload_module()
    assert mod.laenge == len(mod.zahlen), "Die Variable 'laenge' muss die Länge der Liste 'zahlen' enthalten."
    assert mod.laenge == 6, "Die Länge der Liste muss 6 sein."