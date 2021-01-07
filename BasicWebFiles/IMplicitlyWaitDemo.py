from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from Drivers.BrowserLaunch import BrowserLaunch
from Drivers.BrowserLaunch import ElementsandData
from BasicWebFiles.HandyWrappers import HandyWrappers

class IMplicitDemo:
    def test(self):
        driver = webdriver.Chrome(executable_path=ElementsandData.Chrome)
        driver.maximize_window()
        hw = HandyWrappers(driver)
        driver.get(ElementsandData.LetskodeitURL)
        driver.implicitly_wait(5)
        hw.getelement2(By.XPATH,"//a[@href='/sign_in']").click()
        hw.getelement2(By.ID,"user_email").send_keys("abcdefgh@gmail.com")
        sleep(2)
        driver.save_screenshot("D:\\PythonProject\\SeleniumProject\\SCREENSHOTS\\jin.png")
a = IMplicitDemo()
a.test()