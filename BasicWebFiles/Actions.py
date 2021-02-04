from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Drivers.BrowserLaunch import BrowserLaunch
from Drivers.BrowserLaunch import ElementsandData
from BasicWebFiles.HandyWrappers import HandyWrappers, time


class Actions:
    def test(self):
        driver = webdriver.Chrome(executable_path=ElementsandData.Chrome)
        driver.maximize_window()
        hw = HandyWrappers(driver)
        driver.get(ElementsandData.PracticeURL)
        hover = hw.getelement2(By.ID,'mousehover')
        #driver.execute_script('arguments[0].scrollIntoView(true);',hover)
        Actions = ActionChains(driver)
        Actions.move_to_element(hover).perform()
        Actions.move_to_element(hw.getelement2(By.XPATH,"//a[text()='Top']")).click().perform()
        driver.get("https://jqueryui.com/droppable/")
        driver.switch_to.frame(0)
        Actions2 = ActionChains(driver)
        fromele = hw.getelement2(By.XPATH,"//div[@id='draggable']")
        to = hw.getelement2(By.XPATH,"//div[@id='droppable']")
        #Actions2.drag_and_drop(fromele,to).perform()
        Actions2.click_and_hold(fromele).move_to_element(to).release(to).perform()
        driver.get("https://jqueryui.com/slider/")
        driver.switch_to.frame(0)
        sliaction = ActionChains(driver)
        sliderelem = hw.getelement2(By.XPATH, "//div[@id='slider']/span[1]")
        sliaction.drag_and_drop_by_offset(sliderelem,100,0).perform()



S =Actions()
S.test()