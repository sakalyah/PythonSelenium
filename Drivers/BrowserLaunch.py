from selenium import webdriver
from Drivers import ElementsandData

class BrowserLaunch():
    def launchbrowser(self,browser,URL):

        if browser=='Chrome':
            driver = webdriver.Chrome(executable_path=ElementsandData.Chrome)
            driver.maximize_window()
            driver.get(URL)
        elif browser=='FF':
            driver = webdriver.Firefox(executable_path=ElementsandData.FF)
            driver.maximize_window()
            driver.get(URL)
        elif browser=='IE':
            driver = webdriver.Ie(executable_path=ElementsandData.IE)
            driver.maximize_window()
            driver.get(URL)
        else :
            print("No Browser Value Given")
