import unittest
import MathOperation as m
class MathOperationTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(m.add(4, 5), 9)
        self.assertNotEqual(m.add(4, 5), 0)

    def test_sub(self):
        self.assertEqual(m.subtract(4, 5), -1)

    def test_multi(self):
        self.assertEqual(m.multiply(4, 5), 20)
        self.assertNotEqual(m.multiply(4, 0), 1)
        self.assertEqual(m.multiply(-4, 4), -16)
        self.assertEqual(m.multiply(-4, -4), 16)

    def test_div(self):
        self.assertEqual(m.divide(4, 2), 2)
        self.assertEqual(m.divide(0, 4), 0)
        self.assertRaises(ValueError, m.divide, 4, 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)

