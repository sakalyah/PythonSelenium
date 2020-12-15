from selenium import webdriver

class RunFF():
    def testFFlaunch(self):
        driver = webdriver.Firefox(executable_path="D:\\PythonProject\\SeleniumProject\\Drivers\\geckodriver")
        #Launch the URL
        driver.get("http://www.letskodeit.com")

FF = RunFF()
FF.testFFlaunch()
