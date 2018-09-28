
from twisted.internet import reactor
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
from boto.cloudtrail.exceptions import InvalidTimeRangeException
import subprocess
import scrapy
import pymysql
import csv
import pymysql.cursors
from twisted.conch.insults.window import cursor
from scrapy.crawler import CrawlerProcess
from twisted.conch.test.test_helper import FakeDelayedCall
from _overlapped import NULL
from asn1crypto._ffi import null
from scrapy.http import Request, FormRequest
import browser_cookie3 as cookies
import pickle
import requests
import time
import threading
import sys
from datetime import datetime
from scrapy.utils.log import configure_logging
import os
from selenium.common.exceptions import ElementNotVisibleException

global response


connection = pymysql.connect(
   host='localhost',
   user='root',
   password='',                             
   db='scraperdb1',
)

print ("Database Connection Established") 
cursor = connection.cursor()
cursor1  = connection.cursor()
cursor2  = connection.cursor()
cursor3  = connection.cursor()
        
        
def ClearCookies():
     
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('chrome://settings/clearBrowserData')
    time.sleep(2)
    elem = Select(driver.find_element_by_css_selector('* /deep/ #dropdownMenu'))
    elem.select_by_index(2)   
    time.sleep(2)
     
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
         
    time.sleep(2)
    clear = driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')
    clear.click()
    time.sleep(2)
    #driver.manage().deleteAllCookies();

def ChangeLocation(pincode, store, base_url, location_id, store_id, sku,area):
    
    try:
        start_urls= base_url+sku
        browser = webdriver.Chrome('chromedriver.exe')
        browser.get(start_urls)
        time.sleep(2)
    
        location = browser.find_elements_by_xpath('//*[@id="headercontroller"]/section[1]/div/div[2]/div/button')
        location[0].click()
        time.sleep(2)
    
        city = browser.find_elements_by_xpath('//*[@id="city-select"]')
        city[0].clear()
        city[0].send_keys(area)
        time.sleep(2)
    
        pin=pincode
        pincode1 = browser.find_elements_by_xpath('//*[@id="area-select"]')
        for pinc in pin:
            pincode1[0].send_keys(pinc)
            time.sleep(2)
            
        randomclick = browser.find_elements_by_css_selector('.ui-corner-all')
        print(randomclick)
        randomclick[0].click()
        time.sleep(2)
        
        complete = browser.find_elements_by_css_selector('#choose-city-form > div.ng-scope > div.btn-green > button')
# #print(complete)
        complete[0].submit()
        time.sleep(2)
        browser.close()
        flag=1
        GetChromeCookies(pincode, store, base_url, location_id, store_id, sku)
        
#  
            
    except ElementNotVisibleException:
        print('cant be scrapped')
        driver.close()
        name="Not Available"
        price="Not Available"
        stock="Not Available"
        rating="Not Available"
        
        sql2 = 'INSERT INTO scrape_reports(scrape_session_id,sku_code, store_id, location_id, item_name, stock_available, item_price, store_rating, scrape_datetime ) values("'+session_id+'","'+sku_id[0]+'","'+store_id[0]+'","'+location_id[0]+'","'+name[0]+'","'+price[0]+'", "'+stock[0]+'", "'+rating[0]+'")'
        print(sql2)
        cursor.execute(sql2)
        connection.commit()
        
def GetChromeCookies(pincode, store, base_url, location_id, store_id, sku) -> None:
    '''
    Utility Function to save a new location.
    
    Change to the required new location in Chrome browser by going to 
    Amazon.in site before calling this function.

    Only to be used to capture cookies for a new PINCODE.  We save and reuse 
    these cookies to pass with the http request for the right PINCODE.

    Alternative is to use Selenium webdrivers for browser automation.
          
    '''
    import browser_cookie3 as cookies

    cJar = cookies.chrome(domain_name='bigbasket.com ')
    cJar1 = {c.name: c.value for c in cJar}
#     del cJar1['session-id-time']
#     del cJar1['visitCount']
    print(cJar)
#    Replace PINCODE below
    with open('cookies/'+store+'_pincodes/'+pincode+'.pkl', 'wb') as fp: pickle.dump(cJar1, fp)

#pincode[0].send_keys(Keys.ENTER)
#time.sleep(2)

#     randomclick = browser.find_elements_by_css_selector('.ui-corner-all')
#     print(randomclick)
#     randomclick[0].click()
#     time.sleep(2)
#  
#     complete = browser.find_elements_by_css_selector('#choose-city-form > div.ng-scope > div.btn-green > button')
# #print(complete)
#     complete[0].submit()
#     time.sleep(2)
    
class BigbasketSpider():
    def __init__(self, base_url, pincode, sku, location_id, store_id, store):
        self.base_url = base_url
        self.pincode = pincode
        self.area = area
        self.sku = sku
        self.location_id = location_id
        self.store_id = store_id
        self.store = store  
        
        
    def start_requests(self):
#         for file in os.listdir("cookies/amazon_pincodes/"):
#             print(file)
#             if os.path.isfile(self.pincode+'pkl'):
#                 ClearCookies()
#                 ChangeLocation(self.pincode, self.store, self.base_url, self.location_id, self.store_id, self.sku)
        
                
#        name = "BigBasket"
#        allowed_domains = ['www.bigbasket.com'] # Domains allowed in Amazon's spider
        start_urls = [self.base_url+self.sku]
        print(start_urls)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}
        with open('cookies/amazon_pincodes/'+self.pincode+'.pkl', 'rb') as fp: cookieJar = pickle.load(fp)
        print(cookieJar)
        for i,url in enumerate(start_urls):
            yield Request(url,cookies=cookieJar, callback=self.scrape_item_with_varaints, headers=headers)
       
#            
#     def scrape_single_item():
#         options = webdriver.ChromeOptions()
#         options.add_argument('headless')
#         driver = webdriver.Chrome('chromedriver.exe')
#         driver.get('https://www.bigbasket.com/pd/40107787/kwality-ladi-pav-300-gm/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop')
#         try:
#             element = WebDriverWait(driver, 60).until(
#                         expected_conditions.presence_of_element_located((By.CLASS_NAME, "sc-bRBYWo"))
#                         )
#             item_desc = driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div")
#             print (item_desc.text + " " + element.text)
#         except TimeoutException:
#             print ("Connection Timeout")
#         finally:
#             driver.quit()

#
    def scrape_item_with_varaints(self,base_url, pincode, sku, location_id, store_id, store):
        print ("Scraping single item with no variants...")
        
        start_urls = base_url+sku
        print('++++++++++++++++++++++++++++++')
        print(start_urls)
        #cursor = connection.cursor()
        #sql = "SELECT id FROM `skus` WHERE website = 'bigbasket'";
        # Execute query
        #cursor.execute(sql)
          
        print("Scraping item with variants...")
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
        driver.get(start_urls)
        try:
            element = WebDriverWait(driver, 60).until(
                    expected_conditions.presence_of_element_located((By.NAME, "size"))
                    )
            buttons = driver.find_elements_by_xpath('//*[@name="size"]')
            for ele in buttons:
                name = ele.get_attribute("id")
                lbl = driver.find_element_by_xpath("//*[@for=\""+ name +"\"]")
                lbl.click()
                item = driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div").text
                price = driver.find_element_by_class_name("sc-bRBYWo").text
                item1=[item,price]
                 
                print(item + " " + price)
                storeItem(item1,self.sku,self.location_id,self.store_id)
        except TimeoutException:
            print ("Connection Timeout")
        finally:
            driver.quit()
            
def storeItem(item,sku_id,location_id,store_id):
    name= [item[0]]
    price=[item[1]]
    price = [price[0].replace('Rs ','')]
    
    stock= ["Available"]
    rating= ["Not Applicable"]
    
    sku_id = [sku_id]
    location_id = [str(location_id)]
    store_id = [str(store_id)]
    scrape_datetime = [str(datetime.now())]
    
        
    sql_fetch_session_id_all= 'SELECT max(id) FROM scrape_sessions'
    cursor.execute(sql_fetch_session_id_all)
    connection.commit()
    current_session_id = []
    for id in cursor:
        session_id = str(id[0])
                        
    print(name)
    print(price)
    print(stock)
    print(rating)
    print(sku_id)
    print(store_id)
    print(location_id)
        
    sql2 = 'INSERT INTO scrape_reports(scrape_session_id,sku_code, store_id, location_id, item_name, item_price, stock_available, store_rating, scrape_datetime ) values("'+session_id[0]+'","'+sku_id[0]+'","'+store_id[0]+'","'+location_id[0]+'","'+name[0]+'","'+price[0]+'", "'+stock[0]+'", "'+rating[0]+'","'+scrape_datetime[0]+'")'
    print(sql2)
    cursor.execute(sql2)
    connection.commit()
                 
cursor = connection.cursor()

start_date_time= str(datetime.now())
end_date_time= str(datetime.now())

scrape_result= 'SCRAPING IN PROGRESS'
sql_insert_session = 'INSERT INTO scrape_sessions(session_start_datetime,session_end_datetime, scrape_result ) values("'+start_date_time+'","'+end_date_time+'", "'+scrape_result+'")'
print(sql_insert_session)
ab= cursor.execute(sql_insert_session)
connection.commit()

sql = 'SELECT store_name, id FROM stores'
cursor1.execute(sql)



flag=0
    



for store, store_id in cursor1:
    print(store)
    print(store_id)
    sql = "SELECT item_sku_codes.sku_code, stores.base_url FROM item_sku_codes, stores WHERE stores.store_name = '"+store+"' AND item_sku_codes.store_id = stores.id"
    print(cursor2.execute(sql))
    for sku, base_url in cursor2:
        print(sku)
        print(base_url)
        sql = 'SELECT store_locations.id, city_area, pin_code FROM store_locations,stores WHERE stores.id = store_locations.id'
        cursor3.execute(sql)
        for location_id,area,pincode in cursor3:
            print(location_id)
            print(pincode)
            area = area.split('_')
            area = area[0]
            print(area)
            for root, dirs, files in os.walk('cookies/bigbasket_pincodes/'):
                print(root)
                print(dirs)
                print(files)
                if pincode+'.pkl' in files:
                    pass
                else:
                    ClearCookies()
                    ChangeLocation(pincode, store, base_url, location_id, store_id, sku,area)
            if flag==1:
                print('++++++++++++++++++++++++++++++++++++++++++++')
                print(flag)
                pass
            
            else:
                b=BigbasketSpider(base_url, pincode, sku, location_id, store_id, store)
                b.scrape_item_with_varaints(base_url, pincode, sku, location_id, store_id, store)

         #base_url = base_url, pincode = pincode, sku = sku, location_id = location_id, store_id = store_id, store = store)
#             process.crawl(AmazonSpider, base_url = base_url, pincode = pincode, sku = sku, location_id = location_id, store_id = store_id)


            

sql_fetch_session_id_all= 'SELECT max(id) FROM scrape_sessions'
cursor.execute(sql_fetch_session_id_all)
connection.commit()
current_session_id = []
for id in cursor:
    session_id = id[0]

end_time = [str(datetime.now())]
if ab == 1:
    scrape_result = 'SUCCESSFUL'
else:
    scrape_result = 'FAILED'

sql_update_end_time_and_status = "UPDATE scrape_sessions SET session_end_datetime = '+(end_time[0])+', scrape_result = '+(scrape_result)' where id ='+(session_id)+' "


print(cursor)        
