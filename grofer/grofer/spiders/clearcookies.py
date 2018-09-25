from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium import webdriver
import time



driver = webdriver.Chrome('chromedriver.exe')
driver.get('chrome://settings/clearBrowserData')
time.sleep(3)

elem = Select(driver.find_element_by_css_selector('* /deep/ #dropdownMenu'))

elem.select_by_index('4')

#option[0].click()
time.sleep(5)

#checkboxes = driver.find_elements_by_css_selector('* /deep/ #checkbox')
#for checkbox in checkboxes:
#    if not checkbox.is_selected():
#        checkbox.click()

result = driver.find_element_by_css_selector('* /deep/ #checkbox')
result.click()
#if result:
#    print('Checkbox already selected')
#else:
#    driver.find_element_by_css_selector('* /deep/ #checkbox').click();
#    print('Checkbox selected')
    
time.sleep(5)


clear = driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')
clear.click()
time.sleep(5)

#driver.manage().deleteAllCookies();


