import unittest
import basic_py_file

class TestWorld(unittest.TestCase):
    def test_first_char(self) -> None:
        self.assertEqual("W", basic_py_file.get_world()[0])

    def test_second_char(self) -> None:
        self.assertEqual("o", basic_py_file.get_world()[1])

    def test_third_char(self) -> None:
        self.assertEqual("r", basic_py_file.get_world()[2])

    def test_fourth_char(self) -> None:
        self.assertEqual("l", basic_py_file.get_world()[3])

    def test_fifth_char(self) -> None:
        self.assertEqual("d", basic_py_file.get_world()[4])

if __name__ == '__main__':
    unittest.main()