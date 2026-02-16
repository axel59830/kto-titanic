from typing import List
import unittest

MIN_LENGTH_EXCLUSIVE: int = 7


def count_names_longer_than_seven(prenoms: List[str]) -> int:
    """
    Compte le nombre de prénoms strictement supérieurs à 7 lettres
    et affiche pour chacun s’il dépasse ou non 7 lettres.
    """
    more_than_seven: int = 0

    for prenom in prenoms:
        if len(prenom) > MIN_LENGTH_EXCLUSIVE:
            print(f"{prenom} contient plus de 7 lettres")
            more_than_seven += 1
        else:
            print(f"{prenom} contient 7 lettres ou moins")

    return more_than_seven


class TestNamesMethod(unittest.TestCase):
     def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = count_names_longer_than_seven(prenoms=prenoms)
        self.assertEqual(more_than_seven, 4)

if __name__ == '__main__':
    unittest.main()

