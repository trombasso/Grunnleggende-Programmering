from O5_clock import Clock  # The code to test
import unittest  # The test framework


class Test_Clock(unittest.TestCase):
    def setUp(self):
        self.__clock = Clock()

    def test_inc_sec_from_default_values(self):
        self.__clock.inc_second()
        self.assertEqual(self.__clock.clock_as_string(), "00.00.0000 kl:00.00.01")

    def test_inc_min_from_default_values(self):
        self.__clock.inc_minutes()
        self.assertEqual(self.__clock.clock_as_string(), "00.00.0000 kl:00.01.00")

    def test_inc_sec_from_midnight_jan(self):
        self.__clock = Clock(31, 1, 2021, 23, 59, 59)
        self.__clock.inc_second()
        self.assertEqual(self.__clock.clock_as_string(), "01.02.2021 kl:00.00.00")

    # flere test cases... :-) spesielt tip-over tilfeller


if __name__ == "__main__":
    unittest.main()
