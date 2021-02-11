import pytest

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class") #scope ="module" if we want totest any module
def oneTimeSetUp(browser):
    print("Running one time setUp")
    if browser == 'firefox':
        print("Running tests on FF")
    else:
        print("Running tests on chrome")
    yield
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

'''import pytest

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    if browser == 'firefox':
        value = 10
        print("Running tests on FF")
    else:
        value = 20
        print("Running tests on chrome")

    if request.cls is not None:
        request.cls.value = value

    yield value
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
    
class_test

"""
How to use test class to wrap methods under one class
Learn about autouse keywords in fixtures
Assert the result to create a real test scenario
"""

class SomeClassToTest():

    def __init__(self, value):
        self.value = value


    def sumNumbers(self, a, b):
        return a + b + self.value
--------------------------------------------
clas_test_demo
import pytest
from pytestpackage.class_to_test import SomeClassToTest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.abc = SomeClassToTest(self.value)

    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("Running method A")

    def test_methodB(self):
        print("Running method B")
'''