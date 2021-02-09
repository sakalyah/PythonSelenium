import unittest

class TestCaseDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setup Class Method")
    def setUp(self):
        print("I will run before any test")

    def test_A(self):
        print("Testing Module A")

    def test_B(self):
        print("Testing Module B")

    def test_C(self):
        print("Testing Module C")

    def tearDown(self):
        print("This is TearDown")

    @classmethod
    def tearDownClass(cls):
        print("Tear Down CLass Method")

if __name__=='__main__':
    #unittest.main(verbosity=2)
    unittest.main(verbosity=2)