from datetime import *
from traceback import print_stack

from selenium import webdriver
from selenium.webdriver.common.by import By

from Drivers.BrowserLaunch import BrowserLaunch
from Drivers.BrowserLaunch import ElementsandData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class HandyWrappers():

    def __init__(self,driver):
        self.driver = driver

    def getByType(self,locatorType):
        locatorType = locatorType.lower()
        if locatorType=='id':
            return By.ID
        elif locatorType=='xpath':
            return By.XPATH
        elif locatorType=='css':
            return By.CSS_SELECTOR
        else:
            print("Locator Type Not Defined")

    def getelement(self,locator,locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType,locator)
            print("Element Found")
        except:
            print("Element Not FOund")
        return element

    def getelement2(self,TypeBy,selector):

        element1 = None
        try:
            element1 = self.driver.find_element(TypeBy,selector)
            if element1 is not  None:
                print("Selector Found")
        except:
            print("Something Went Wrong")
        return element1

    def isElementVisible(self,TypeBy,selector):
        element = None
        try:
            element = self.driver.find_element(TypeBy,selector)
            if element.is_displayed():
                return  True
            else :
                return False
        except:
            print("Something Went Wrong")
            return False

    def waitforElementtoVisible(self,timeout,TypeBy,selector):
        try :
          element = None
          wait = WebDriverWait(self.driver,timeout,poll_frequency=10,ignored_exceptions=
                             [NoSuchElementException,ElementNotVisibleException,InvalidSelectorException])
          element = wait.until(EC.visibility_of_element_located((TypeBy,selector)))
          print("Waited till Element was Visible")
          return element
        except Exception as e :
            print("No Such Element Found",e)
            print_stack()
            raise e

    def takeScreenshot(self):
        filename ='jin'+str(1000)+'.png'
        destinationfile = ElementsandData.DestinationFIle + filename
        try:
           self.driver.save_screenshot(destinationfile)
           print("Screenshot taken successfully")
        except NotADirectoryError:
            print("Screenshot Failed")





