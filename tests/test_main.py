import unittest
from src.main import woerterbuch_umkehren, haeufigste_woerter, dictionaries_zusammenfuehren


class TestDictionaryUebungen(unittest.TestCase):

    def test_woerterbuch_umkehren(self):
        eingabe = {'a': 1, 'b': 2, 'c': 3}
        erwartete_ausgabe = {1: 'a', 2: 'b', 3: 'c'}
        self.assertEqual(woerterbuch_umkehren(eingabe), erwartete_ausgabe)

        # Test mit leerem Dictionary
        self.assertEqual(woerterbuch_umkehren({}), {})

    def test_haeufigste_woerter(self):
        text = "Der Hund läuft. Der Hund bellt. Die Katze miaut."
        self.assertEqual(haeufigste_woerter(text), {'Der': 2, 'Hund': 2, 'läuft.': 1, 'bellt.': 1, 'Die': 1, 'Katze': 1, 'miaut.': 1})

        # Test mit leerem Text
        self.assertEqual(haeufigste_woerter("", 1), {})

    def test_dictionaries_zusammenfuehren(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        dict3 = {'d': 5}
        erwartete_ausgabe = {'a': 1, 'b': 3, 'c': 4, 'd': 5}
        self.assertEqual(dictionaries_zusammenfuehren(dict1, dict2, dict3), erwartete_ausgabe)

        # Test mit einem leeren Dictionary
        self.assertEqual(dictionaries_zusammenfuehren(dict1, {}, dict3), {'a': 1, 'b': 2, 'd': 5})

        # Test ohne Argumente
        self.assertEqual(dictionaries_zusammenfuehren(), {})


if __name__ == '__main__':
    unittest.main()
