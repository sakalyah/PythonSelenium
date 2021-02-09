import unittest

from UnitTestPackage.AssertionInPython import AssertDemo
from UnitTestPackage.pythonpath import TestClass1

# Get all tests from TestClass1 and TestClass2
#tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo)
tc2 = unittest.TestLoader().loadTestsFromTestCase(AssertDemo)
tc3 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)

# Create a test suite combining TestClass1 and TestClass2
smokeTest = unittest.TestSuite([tc2, tc3])

unittest.TextTestRunner(verbosity=2).run(smokeTest)