import unittest

from exam import fmod_wrapper


class MyTestCase(unittest.TestCase):
    def test_okay_positive(self):
        self.assertEqual(fmod_wrapper(10, 5), 0)

    def test_okay_with_negative(self):
        self.assertEqual(fmod_wrapper(-10, 3), -1)

    def test_function_raises_error_for_devision_by_zero(self):
        with self.assertRaises(ValueError) as context:
            fmod_wrapper(7, 0)

    def test_function_raises_error_for_string_param1(self):
        with self.assertRaises(TypeError) as context:
            fmod_wrapper("qwerty", 2)

    def test_function_raises_error_for_string_param2(self):
        with self.assertRaises(TypeError) as context:
            fmod_wrapper(3, "sasa")
