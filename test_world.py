import unittest
import world

class TestWorld(unittest.TestCase):
    def test_first_char(self) -> None:
        self.assertEqual("W", world.get_world()[0])

    def test_second_char(self) -> None:
        self.assertEqual("o", world.get_world()[1])

    def test_third_char(self) -> None:
        self.assertEqual("r", world.get_world()[2])

    def test_fourth_char(self) -> None:
        self.assertEqual("l", world.get_world()[3])

    def test_fifth_char(self) -> None:
        self.assertEqual("d", world.get_world()[4])

if __name__ == '__main__':
    unittest.main()