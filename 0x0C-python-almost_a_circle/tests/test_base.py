import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_init_with_id(self):
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_init_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_to_json_string(self):
        b = Base(10)
        self.assertEqual(b.to_json_string([{'id': 1, 'x': 2}]), '[{"id": 1, "x": 2}]')

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()

