import unittest
import dollar

class MyTestCase(unittest.TestCase):
    def test_something(self):
        five = dollar.Dollar()
        five.times(2)
        self.assertEqual(10, five.amount)


if __name__ == '__main__':
    unittest.main()
