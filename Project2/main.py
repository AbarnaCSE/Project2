
import time
from xml.etree.ElementPath import findtext
from Data import data
from Locators import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

class LoginPage:

   def __init__(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

   def boot(self):
       self.driver.get(data.WebData().url)
       self.driver.maximize_window()
       self.driver.implicitly_wait(10)

   def quit(self):
       self.driver.quit()

   def login(self):

    try:
       self.boot()
       locator.WebLocators().clickButton(self.driver, locator.WebLocators().Forgotyourpasswordlocator)
       time.sleep(5)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
       locator.WebLocators().clickButton(self.driver, locator.WebLocators().ResetPasswordlocator)
       time.sleep(5)
       self.boot()
       locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, data.WebData().password)
       locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonlocator)
       locator.WebLocators().clickButton(self.driver, locator.WebLocators().Adminlocator)
       assert self.driver.title == data.WebData().Title
       print("SUCCESS: Web Title Verified")

       locator_data = {
          "UserManagementlocator": "UserManagement",
          "Joblocator":"Job",
          "Organizationlocator":"Organization",
          "Qualificationslocator":"Qualifications",
          "Nationalitieslocator": "Nationalities",
          "CorporateBrandinglocator": "CorporateBranding",
          "Configurationlocator":"Configuration",
          "adminlocator": "Admin",
          "PIMlocator" : "PIM",
          "Leavelocator" : "Leave",
          "Timelocator" : "Time",
          "Recruitmentlocator" : "Recruitment",
          "MyInfolocator" : "MyInfo",
          "Performancelocator" :"Performance",
          "Dashboardlocator" : "Dashboard",
          "Directorylocator" : "Directory",
          "Maintenancelocator" : "Maintenance",
          "Claimlocator" :"Claim",
          "Buzzlocator" : "Buzz"

          }
       for locator_key, data_key in locator_data.items():
         locator_method = getattr(locator.WebLocators(), locator_key)
         Validate1 = locator.WebLocators().findtext(self.driver, locator_method)
         validate2 = getattr(data.WebData(), data_key)
         if (Validate1 == validate2):
            print(f"'{data_key}' is present in Admin Page")
         else:
            print(f"'{data_key}' is not present in Admin Page")
            time.sleep(5)
    except NoSuchElementException as e:
        print("Error!")        
    finally:
        self.quit()         
    
obj = LoginPage()
obj.login()













































