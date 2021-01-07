from selenium import webdriver
from selenium.webdriver.common.by import By

from Drivers.BrowserLaunch import BrowserLaunch
from Drivers.BrowserLaunch import ElementsandData

class By_class():

    def test(self):
        driver = webdriver.Chrome(executable_path=ElementsandData.Chrome)
        driver.maximize_window()
        driver.get(ElementsandData.PracticeURL)
        elementByXpath = driver.find_element(By.XPATH,"//input[@id='hondaradio']")
        if elementByXpath is not None:
            print(elementByXpath.get_attribute('value'))
        elementByID = driver.find_element(By.ID,"openwindow")
        if elementByID is not None:
            elementByID.click()

d = By_class()
d.test()




