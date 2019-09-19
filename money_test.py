import unittest
import dollar

class MyTestCase(unittest.TestCase):
    def test_something(self):
        five = dollar.Dollar(5)
        self.assertEqual(dollar.Dollar(10), five.times(2))
        self.assertEqual(dollar.Dollar(15), five.times(3))

    def test_equality(self):
        self.assertTrue(dollar.Dollar(5).equals(dollar.Dollar(5)))
        self.assertFalse(dollar.Dollar(5).equals(dollar.Dollar(6)))

if __name__ == '__main__':
    unittest.main()
