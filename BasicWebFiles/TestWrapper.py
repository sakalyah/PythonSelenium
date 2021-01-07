from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from Drivers.BrowserLaunch import BrowserLaunch
from Drivers.BrowserLaunch import ElementsandData
from BasicWebFiles.HandyWrappers import HandyWrappers

class Testwrappers():

    def test(self):
        driver = webdriver.Chrome(executable_path=ElementsandData.Chrome)
        driver.maximize_window()
        hw = HandyWrappers(driver)
        driver.get(ElementsandData.PracticeURL)
        ele = hw.getelement('bmwcheck')#Default Selects ID
        ele.click()
        sleep(2)
        ele1 = hw.getelement("//select[@id='carselect']",locatorType='xpath')#Given Both PArameters
        ele1.click()
        sleep(2)
        ele2 = hw.getelement2(By.CSS_SELECTOR,"#hondacheck")
        ele2.click()
        sleep(3)
        ele3 = hw.isElementVisible(By.XPATH,"//input[@id='displayed-text']")
        print(ele3.__str__())
        hw.waitforElementtoVisible(10,By.XPATH,"//a[@id='opentabb']").click()
        sleep(5)

d = Testwrappers()
d.test()
