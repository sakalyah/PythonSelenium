from time import sleep

from selenium import webdriver
from Drivers import ElementsandData

class ByIDName():
    def test(self):
        driver = webdriver.Chrome(executable_path=ElementsandData.Chrome)
        driver.maximize_window()
        driver.get(ElementsandData.PracticeURL)
        elementbyID = driver.find_element_by_id("name")

        if elementbyID is not None:
            print("Element Found by ID")
            sleep(2)
            elementbyID.send_keys("TESTING")
        elementByName = driver.find_element_by_name("show-hide")

        if elementByName is not None:
            print("Element Found By Name")
            sleep(2)
            elementByName.send_keys("HARISH")

a = ByIDName()
a.test()
