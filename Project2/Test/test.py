import time

from Locators import locator
from Data import data

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import pytest

class Test:
   
   @pytest.fixture
   def __init__(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

   def boot(self):
       self.driver.get(data.WebData().url)
       self.driver.maximize_window()
       self.driver.implicitly_wait(10)

   def quit(self):
       self.driver.quit()

   @pytest.mark.html

   def login(self):

    try:
        self.boot()
        credentials_generator = data.WebData().get_credentials()
        for username, password in credentials_generator:
            locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, username)
            locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, password)
            locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonlocator)
            time.sleep(5)
            if self.driver.title == data.WebData().Title:
                print("SUCCESS: Web Title Verified")
                time.sleep(5)
                print(self.driver.current_url)
            else:
                 print("FAIL: Web Title not Verified")

    except NoSuchElementException as e:
        print("Error!")
            
    finally:
        self.quit()               

