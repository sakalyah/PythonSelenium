from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Drivers.BrowserLaunch import BrowserLaunch
from Drivers.BrowserLaunch import ElementsandData

class dropdown():

    def test(self):
        driver = webdriver.Chrome(executable_path=ElementsandData.Chrome)
        driver.maximize_window()
        driver.get(ElementsandData.PracticeURL)
        ele = driver.find_element(By.XPATH,"//select[@id='carselect']")
        sel = Select(ele)
        sel.select_by_index(1)
        sel.select_by_visible_text("Honda")

f = dropdown()
f.test()