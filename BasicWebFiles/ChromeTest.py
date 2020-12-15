from selenium import webdriver
from Drivers import ElementsandData

class RunCHrome():
    def testCHromelaunch(self):
        driver = webdriver.Chrome(executable_path=ElementsandData.Chrome)
        #Launch the URL
        driver.get("http://www.letskodeit.com")

FF = RunCHrome()
FF.testCHromelaunch()
print(FF)