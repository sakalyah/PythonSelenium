import pytest

def test_demo1_methodA(oneTimeSetUp, setUp): #arguments should be in order otherwise execution will be impacted
    print("Running conftest demo1 method A")

def test_demo1_methodB(oneTimeSetUp, setUp):
    print("Running conftest demo1 method B")

def test_demo1_methodC(oneTimeSetUp, setUp):
    print("Running conftest demo1 method C")