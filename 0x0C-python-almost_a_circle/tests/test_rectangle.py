import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        r = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 1)

    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_to_dictionary(self):
        r = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r.to_dictionary(), {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3})

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()

