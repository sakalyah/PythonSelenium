import pytest
from Loggingmodule.ClassToTest import SomeClassToTest
from Loggingmodule.AnotherCLassToTest import AnotherClass

@pytest.mark.usefixtures("oneTimeSetUp", "setUp") #This fixture is defined for the whole CLass
class TestClassDemo():

    @pytest.fixture(autouse=True) #Since we need this object for all methods we use autouse argument
    def classSetup(self):
        self.abc = SomeClassToTest(10)
        self.pqr = AnotherClass("Harish")

    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        #assert result == 21 #No need to use self.assert since we are using pytest(imported)
        assert result == 20  # No need to use self.assert since we are using pytest(imported)
        print("Running method A")

    def test_methodB(self):
        result1 = self.pqr.test("Harish")
        assert result1 == "Harish"
        print("Running method B")