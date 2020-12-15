from selenium import webdriver
from Drivers import ElementsandData

class IETEST():
    def testIE(self):
        driver = webdriver.Ie(executable_path=ElementsandData.IE)

        driver.get("http://salesforce.com")

ie = IETEST()
ie.testIE()
