from selenium import webdriver
from selenium.webdriver.common.by import By

from Drivers.BrowserLaunch import BrowserLaunch
from Drivers.BrowserLaunch import ElementsandData

class listofelements():

    def test(self):
        driver = webdriver.Chrome(executable_path=ElementsandData.Chrome)
        driver.maximize_window()
        driver.get(ElementsandData.PracticeURL)
        elementsbyTag = driver.find_elements(By.XPATH,'//a')
        if elementsbyTag is not None :
            print(len(elementsbyTag))
        ele1 = driver.find_element(By.XPATH,"//td[text()='Python Programming Language']/following-sibling::td[1]")
        print("The cost of PYTHON BOOK is "+ele1.text)

c = listofelements()
c.test()