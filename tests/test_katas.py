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
        with self.assertRaises(ValueError):
            katas.power(2, -1)
        with self.assertRaises(ValueError):
            katas.power(2, 0.2)

    def test_factorial(self):
        x = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800,
             39916800, 479001600, 6227020800, 87178291200]
        for i, n in enumerate(x):
            self.assertEqual(katas.factorial(i+1), n)
            with self.assertRaises(ValueError):
                katas.factorial(-1)

    def test_fibonacci(self):
        x = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
             1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393,
             196418, 317811, 514229]
        for i, n in enumerate(x):
            self.assertEqual(katas.fibonacci(i), n)
        with self.assertRaises(ValueError):
            katas.fibonacci(-1)


if __name__ == '__main__':
    unittest.main()
