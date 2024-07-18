
import unittest
from circle import getArea, getPerimeter


class CircleTest(unittest.TestCase):
    def test_area(self):
# Bu faqat matematik testlar uchun va bu nuqtadan keyin 7 ta aniqlikda ishlaydi
        self.assertAlmostEqual(getArea(10), 314.159) # Agar (getArea(10), 314.159, 4) bolsa 4 aniqlikgacha
        self.assertAlmostEqual(getArea(3), 28.27431)

    def test_perimeter(self):
        self.assertAlmostEqual(getPerimeter(10), 62.8318)
        self.assertAlmostEqual(getPerimeter(4), 25.13272)


# if __name__ == '__main__':
# unittest.main()
unittest.main()
