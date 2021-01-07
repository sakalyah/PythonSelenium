from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

from Drivers.BrowserLaunch import BrowserLaunch
from Drivers.BrowserLaunch import ElementsandData
from BasicWebFiles.HandyWrappers import HandyWrappers

class ExplicitDemo :

    def test(self):
        driver = webdriver.Chrome(executable_path=ElementsandData.Chrome)
        driver.maximize_window()
        driver.get("http://www.expedia.com")
        wait = WebDriverWait(driver,10,poll_frequency=10,
                             ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
        element = wait.until(EC.visibility_of_element_located((By.XPATH,"//a//span[text()='Flights']")))
        element.click()

C = ExplicitDemo()
C.test()


