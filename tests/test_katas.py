import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        result = katas.add(10, 5)
        self.assertEqual(result, 15)

    def test_multiply(self):
        result = katas.multiply(10, 5)
        self.assertEqual(result, 50)

    def test_power(self):
        result = katas.power(2, 2)
        self.assertEqual(result, 4)

    def test_factorial(self):
        x = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800,
             479001600, 6227020800, 87178291200, 1307674368000]
        for i in x():
            self.assertEqual(katas.factorial(i), x)

    def test_fibonacci(self):
        self.fail("TODO: Write fibonacci unit test")


if __name__ == '__main__':
    unittest.main()
