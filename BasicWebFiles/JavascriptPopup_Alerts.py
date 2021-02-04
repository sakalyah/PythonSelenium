from selenium.webdriver.common.by import By

from Drivers.BrowserLaunch import BrowserLaunch
from Drivers.BrowserLaunch import ElementsandData
from BasicWebFiles.HandyWrappers import HandyWrappers
from time import sleep

from selenium import webdriver

class Alerts:
    def test(self):
        driver = webdriver.Chrome(executable_path=ElementsandData.Chrome)
        driver.maximize_window()
        hw = HandyWrappers(driver)
        driver.get(ElementsandData.PracticeURL)
        hw.getelement2(By.ID,'alertbtn').click()
        Alert1 = driver.switch_to.alert
        Alert1.accept()
        hw.getelement2(By.ID, 'confirmbtn').click()
        #hw.takeScreenshot()
        Alert2 = driver.switch_to.alert
        Alert2.dismiss()

J = Alerts()
J.test()