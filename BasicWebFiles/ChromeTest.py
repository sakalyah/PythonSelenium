from selenium import webdriver

class RunCHrome():
    def testCHromelaunch(self):
        driver = webdriver.Chrome(executable_path="D:\\PythonProject\\SeleniumProject\\Drivers\\chromedriver")
        #Launch the URL
        driver.get("http://www.letskodeit.com")

FF = RunCHrome()
FF.testCHromelaunch()
print(FF)