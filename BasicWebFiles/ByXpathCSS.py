from time import sleep

from selenium import webdriver
from Drivers import ElementsandData

class ByXpathCss:
    def test(self):
        driver = webdriver.Chrome(executable_path=ElementsandData.Chrome)
        driver.maximize_window()
        driver.get(ElementsandData.PracticeURL)
        Xpathelement = driver.find_element_by_xpath("//select[@id='carselect']")
        if Xpathelement is not None:
            print("XPath Code is Working")
            sleep(2)
            Xpathelement.click()
        Csselement = driver.find_element_by_css_selector("input[placeholder='Enter Your Name']")
        if Csselement is not None:
            print("CSS Code is Working")
            sleep(2)
            Csselement.send_keys("DENGEI")
        LinkTextelement = driver.find_element_by_link_text("Login")
        if LinkTextelement is not None:
            print("Link TExt Element is Found")
        Partiallinktextelement = driver.find_element_by_partial_link_text("Prac")
        if Partiallinktextelement is not None:
            print("Partial Link TExt Element is Found")
        ClassNameElement = driver.find_element_by_class_name("displayed-class")
        if ClassNameElement is not None:
            print("ClassNameElement is Found")
        TagElement = driver.find_element_by_tag_name("a")
        if TagElement is not None:
            print("TagElement is Found")

b = ByXpathCss()
b.test()