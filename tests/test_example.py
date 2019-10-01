import unittest


def target_add(a, b):
    return a + b


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(8, target_add(2, 6))

    def test_add_zero(self):
        self.assertEqual(2, target_add(2, 0))


if __name__ == "__main__":
    unittest.main()
