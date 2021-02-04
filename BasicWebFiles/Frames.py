from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from Drivers.BrowserLaunch import BrowserLaunch
from Drivers.BrowserLaunch import ElementsandData
from BasicWebFiles.HandyWrappers import HandyWrappers

class FrameHandling:
    def test(self):
        driver = webdriver.Chrome(executable_path=ElementsandData.Chrome)
        driver.maximize_window()
        hw = HandyWrappers(driver)
        driver.get(ElementsandData.PracticeURL)
        legend = hw.getelement2(By.XPATH,"//legend[text()='iFrame Example']")
        driver.execute_script('arguments[0].scrollIntoView(true);',legend)
        driver.switch_to.frame("iframe-name")
        courses = hw.getelement2(By.ID,'search-courses')
        courses.send_keys("PYTHON")
        hw.takeScreenshot()
        driver.switch_to.default_content()

A= FrameHandling()
A.test()

