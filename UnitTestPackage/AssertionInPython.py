"""
https://docs.python.org/3/library/unittest.html#unittest.TestCase --
Link to find all the Assertions available in Python
"""
import unittest

class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, "a is not false")
        b = False
        self.assertFalse(b, "b is not true")

    def test_assertEqual(self):
        a = "Test"
        b = "Test"
        c = [0,1,2,3]
        self.assertEqual(a, b, msg="'a' is not equal to 'b'")
        self.assertTrue(len(c)>=0,"c does not have elements")


if __name__ == '__main__':
    unittest.main(verbosity=2)