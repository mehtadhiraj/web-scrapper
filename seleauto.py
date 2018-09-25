from selenium import webdriver
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.common.by import By
   
  
# For using sleep function because selenium  
# works only when the all the elemets of the  
# page is loaded. 
import time  
   
from selenium.webdriver.common.keys import Keys  
from boto.cloudtrail.exceptions import InvalidTimeRangeException

  
# Creating an instance webdriver 
browser = webdriver.Chrome('C:/Users/karth/Documents/LiClipse Workspace/bbscraping/chromedriver.exe')  
browser.get('https://www.amazon.in/Sunfeast-Dark-Fantasy-Choco-Fills/dp/B01CHUSZJ8/ref=sr_1_1?srs=9574332031&ie=UTF8&qid=1537696125&sr=1-1') 
  
# Let's the user see and also load the element  
time.sleep(2) 
   
location = browser.find_elements_by_xpath('//*[@id="nav-global-location-slot"]/span/a') 
print(location)  
# using the click function which is similar to a click in mouse. 
location[0].click() 
time.sleep(5)

#change = nextpage.find_elements_by_xpath('//*[@id="GLUXChangePostalCodeLink"]') 
change=browser.find_elements_by_xpath('//*[@id="GLUXChangePostalCodeLink"]')
print(change)
change[0].click()
#browser.css("#GLUXChangePostalCodeLink").click()
time.sleep(5)

enterpincode=browser.find_elements_by_xpath('//*[@id="GLUXZipUpdateInput"]')
enterpincode[0].clear()
#enterpincode[0].get_text()
enterpincode[0].send_keys('400086')
time.sleep(5)

apply=browser.find_elements_by_xpath('//*[@id="GLUXZipUpdate"]/span/input')
print(apply)
apply[0].click()
time.sleep(5)

done=browser.find_elements_by_xpath('//*[@id="a-popover-2"]/div/div[2]/span/span/span/button')
print(done)
done[0].click()
time.sleep(5)  
driver = webdriver.Chrome()

driver.get('chrome://settings/clearBrowserData')
time.sleep(3)

driver.manage().deleteAllCookies();
