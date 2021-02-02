from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from Drivers.BrowserLaunch import BrowserLaunch
from Drivers.BrowserLaunch import ElementsandData
from BasicWebFiles.HandyWrappers import HandyWrappers

class WindowHandling:
    def test(self):
        driver = webdriver.Chrome(executable_path=ElementsandData.Chrome)
        driver.maximize_window()
        hw = HandyWrappers(driver)
        driver.get(ElementsandData.PracticeURL)
        mainwindow = driver.current_window_handle
        hw.getelement2(By.ID,"openwindow").click()
        windows = driver.window_handles
        for win in windows :
            print(win)
            if win not in mainwindow:
                driver.switch_to.window(win)
                driver.maximize_window()
                ele = hw.getelement2(By.XPATH,"//input[@placeholder='Find a course']")
                ele.send_keys("PYTHON")
                driver.execute_script("arguments[0].setAttribute('style', 'background: yellow; border: 2px solid red;');",ele)
                hw.takeScreenshot()


SS = WindowHandling()
SS.test()
