from selenium import webdriver
from Drivers import ElementsandData

class RunFF():
    def testFFlaunch(self):
        driver = webdriver.Firefox(executable_path=ElementsandData.FF)
        #Launch the URL
        driver.get("http://www.letskodeit.com")

FF = RunFF()
FF.testFFlaunch()
