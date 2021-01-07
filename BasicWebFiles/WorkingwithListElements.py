from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from Drivers.BrowserLaunch import BrowserLaunch
from Drivers.BrowserLaunch import ElementsandData

class listofelements():

    def test(self):
        driver = webdriver.Chrome(executable_path=ElementsandData.Chrome)
        driver.maximize_window()
        driver.get(ElementsandData.PracticeURL)
        elementsbyTag = driver.find_elements(By.XPATH,'//legend[text()="Radio Button Example"]//following::label/input')
        if elementsbyTag is not None :
            print(len(elementsbyTag))
        for i in range(len(elementsbyTag)):
            elementsbyTag[i].click()


c = listofelements()
c.test()