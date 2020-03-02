import unittest
import task


class TestCase(unittest.TestCase):
    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())


if __name__ == '__main__':
    unittest.main()


class TestCase(unittest.TestCase):
    def test1(self):
        expected = 3.14
        self.assertEqual(expected, task.c_area(1))

    def test2(self):
        expected = 314.0
        self.assertAlmostEqual(expected, task.c_area(10))

    def test3(self):
        expected = 0
        self.assertAlmostEqual(expected, task.c_area(0))

