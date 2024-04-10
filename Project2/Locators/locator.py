
from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

class WebLocators:
   
   def __init__(self):
       self.usernameLocator = "username"
       self.passwordLocator = "password"
       self.buttonlocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
       self.Forgotyourpasswordlocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p'
       self.ResetPasswordlocator ='//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]'
       self.Adminlocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span'
       self.UserManagementlocator = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]'
       self.Joblocator ='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span'
       self.Organizationlocator = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span'
       self.Qualificationslocator ='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span'
       self.Nationalitieslocator ='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a'
       self.CorporateBrandinglocator ='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]'
       self.Configurationlocator ='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span'
       self.adminlocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span'
       self.PIMlocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'
       self.Leavelocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span'
       self.Timelocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span'
       self.Recruitmentlocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span'
       self.MyInfolocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span'
       self.Performancelocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span'
       self.Dashboardlocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span'
       self.Directorylocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span'
       self.Maintenancelocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span'
       self.Claimlocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a/span'
       self.Buzzlocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a/span'

   def enterText(self, driver, value, textValue):
       element=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, value)))
       element.send_keys(textValue)
   def clickButton(self,driver, value):
       element=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, value)))
       element.click()
   def findtext(self,driver, value):
       element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, value)))
       element_text = element.text
       return element_text



   
    
    
   

    
       
   
    





    
   

    

       

