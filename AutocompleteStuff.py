from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from Drivers.BrowserLaunch import BrowserLaunch
from Drivers.BrowserLaunch import ElementsandData
from BasicWebFiles.HandyWrappers import HandyWrappers

class Autocomplete:
    def test(self):
        driver = webdriver.Chrome(executable_path=ElementsandData.Chrome)
        driver.maximize_window()
        hw = HandyWrappers(driver)
        driver.get(ElementsandData.SouthwestURL)
        Round = hw.getelement2(By.XPATH,"//span[text()='Round trip']")
        driver.execute_script('arguments[0].scrollIntoView(true);',Round)
        depart = hw.waitforElementtoVisible(10,By.XPATH,"//span[text()='Depart']//following::input[1]")
        depart.send_keys("New Orleans, LA - MSY")
        list = hw.waitforElementtoVisible(10,By.ID,"LandingAirBookingSearchForm_originationAirportCode--menu")
        listelements = list.find_elements(By.XPATH,"//ul[@id='LandingAirBookingSearchForm_originationAirportCode--menu']//li//button")
        for city in listelements :
            if city.get_attribute("aria-label")=="New Orleans, LA - MSY" :
                city.click()
                #driver.save_screenshot(ElementsandData.DestinationFIle)
                hw.takeScreenshot()


A = Autocomplete()
A.test()