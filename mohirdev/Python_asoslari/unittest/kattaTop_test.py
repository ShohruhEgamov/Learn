import unittest
from kattaTop import kattasiniQaytar

class KattaTop(unittest.TestCase):
    def test_top(self):
        self.assertAlmostEqual(kattasiniQaytar(2, 3, 1), 3)
        self.assertAlmostEqual(kattasiniQaytar(5, 3, 4), 5)
        self.assertAlmostEqual(kattasiniQaytar(2, 2, 2), 2)
        self.assertAlmostEqual(kattasiniQaytar(-1, -3, -2), -1)

if __name__ == "__main__":
    unittest.main()