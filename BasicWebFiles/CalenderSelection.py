from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from Drivers.BrowserLaunch import BrowserLaunch
from Drivers.BrowserLaunch import ElementsandData
from BasicWebFiles.HandyWrappers import HandyWrappers

class CalenderSelection:
    def test(self):
        driver = webdriver.Chrome(executable_path=ElementsandData.Chrome)
        driver.maximize_window()
        hw = HandyWrappers(driver)
        driver.get(ElementsandData.ExpediaURL)
        Flights = hw.waitforElementtoVisible(10,By.XPATH,"//span[text()='Flights']")
        Flights.click()
        Departing = hw.waitforElementtoVisible(10,By.XPATH,"//button[@aria-label='Going to']//following::div[@class='uitk-date-picker-menu uitk-menu uitk-menu-mounted'][1]//button[text()]")
        Departing.click()
        Feb = hw.waitforElementtoVisible(20,By.XPATH,"//h2[text()='February 2021']")
        Date1 = "//table[@class='uitk-date-picker-weeks'][position()=1]//td"
        Date2 = "//button[@aria-label='5 Feb 2021.']"
        Date3 =Date1 + Date2
        print(Date3)
        DepartingDate2 = hw.waitforElementtoVisible(15,By.XPATH,Date3)
        DepartingDate2.click()
        sleep(2)
        hw.getelement2(By.XPATH,"//span[text()='Done']").click()
        sleep(2)
       # print(hw.getelement(By.XPATH,"//span[text()='Departing']//following::a[1]/button[1]").get_Attribute("aria-label"))

d = CalenderSelection()
d.test()
