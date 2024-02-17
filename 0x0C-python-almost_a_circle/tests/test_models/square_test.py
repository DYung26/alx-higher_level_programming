import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_init(self):
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 1)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_to_dictionary(self):
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.to_dictionary(), {'id': 1, 'size': 5, 'x': 2, 'y': 3})

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()

