# from twisted.internet import reactor 
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
from scrapy.crawler import CrawlerRunner
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
from scrapy.utils.log import configure_logging
import os
global response
from datetime import datetime

#  Connect to the database.
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
        
'''
Data that needs to be stored
Defining a class consisting of required field

'''
class Item(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    rating = scrapy.Field()
    location_id = scrapy.Field()
    store_id = scrapy.Field()
    sku_id = scrapy.Field()
 
 
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
     
# Creating Cookies form Chrome
def ChangeLocation(pincode, store, base_url, location_id, store_id, sku):
     
#     sql = "SELECT id FROM `skus` WHERE website = 'amazon'";
#     #Execute query
#     cursor.execute(sql)
#     name = "AmazonSpider"
    allowed_domains = ['www.amazon.in', 'www.grofers.com', 'www.bigbasket.com'] # Domains allowed in Amazon's spider
#     base_url = 'https://www.amazon.in/dp/'
#     start_urls = []
#     for url in cursor:
    start_urls = base_url+sku
     
    # Creating an instance webdriver 
    browser = webdriver.Chrome('chromedriver.exe') 
    print(start_urls)
    browser.get(start_urls) 
       
    # Let's the user see and also load the element  
    time.sleep(2) 
        
    location = browser.find_elements_by_xpath('//*[@id="nav-global-location-slot"]/span/a') 
    print(location)  
    # using the click function which is similar to a click in mouse. 
    location[0].click() 
    time.sleep(2)
     
    #change = nextpage.find_elements_by_xpath('//*[@id="GLUXChangePostalCodeLink"]') 
    change=browser.find_elements_by_xpath('//*[@id="GLUXChangePostalCodeLink"]')
    print(change)
    change[0].click()
    #browser.css("#GLUXChangePostalCodeLink").click()
    time.sleep(2)
     
    enterpincode=browser.find_elements_by_xpath('//*[@id="GLUXZipUpdateInput"]')
    enterpincode[0].clear()
    #enterpincode[0].get_text()
    enterpincode[0].send_keys(pincode)
    time.sleep(2)
     
    apply=browser.find_elements_by_xpath('//*[@id="GLUXZipUpdate"]/span/input')
    print(apply)
    apply[0].click()
    time.sleep(2)
     
    done = browser.find_elements_by_name('glowDoneButton')#('//*[@id="a-popover-2"]/div/div[2]/span/span/span/button')
    
    print(done)
    done[0].click()
    time.sleep(2)  
    driver = webdriver.Chrome()
     
#     driver.get('chrome://settings/clearBrowserData')
    time.sleep(2)
    driver.close()
    GetChromeCookies(pincode, store, base_url, location_id, store_id, sku)
     
     
 
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

    cJar = cookies.chrome(domain_name='amazon.in')
    cJar1 = {c.name: c.value for c in cJar}
#     del cJar1['session-id-time']
#     del cJar1['visitCount']
    print(cJar)
#    Replace PINCODE below
    with open('cookies/'+store+'_pincodes/'+pincode+'.pkl', 'wb') as fp: pickle.dump(cJar1, fp)
    # # Setting browser version
    
 
#Spider to scrap amazon's data
class AmazonSpider(scrapy.Spider):
    def __init__(self, base_url, pincode, sku, location_id, store_id, store):
        self.base_url = base_url
        self.pincode = pincode
        self.area = area
        self.sku = sku
        self.location_id = location_id
        self.store_id = store_id
        self.store = store

 # Cookie based data scraping    
    def start_requests(self):
#         for file in os.listdir("cookies/amazon_pincodes/"):
#             print(file)
#             if os.path.isfile(self.pincode+'pkl'):
#                 ClearCookies()
#                 ChangeLocation(self.pincode, self.store, self.base_url, self.location_id, self.store_id, self.sku)
               
        name = "AmazonSpider"
        allowed_domains = ['www.amazon.in'] # Domains allowed in Amazon's spider
        start_urls = [self.base_url+self.sku]
        print(start_urls)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}
        with open('cookies/amazon_pincodes/'+self.pincode+'.pkl', 'rb') as fp: cookieJar = pickle.load(fp)
        print(cookieJar)
        for i,url in enumerate(start_urls):
            yield Request(url,cookies=cookieJar, callback=self.parse, headers=headers)
       
    def parse(self, response):
        item = Item()
        item['name']=response.css('#productTitle::text').extract()
        item['rating']=response.css('#acrPopover > span.a-declarative > a > i.a-icon.a-icon-star.a-star-4 > span::text').extract()
        if len(item['rating']) <1:
            item['rating'] = ['Not applicable']
        item['price']=response.css('#priceblock_ourprice::text').extract()
#         item['offer']=response.css('#regularprice_savings > td.a-span12.a-color-price.a-size-base::text').extract()
        item['stock']=response.css('#availability > span::text').extract()
         
        # Striping data to remove blank spaces
        item['name'][0] = item['name'][0].replace('\n',"").strip() 
        item['stock'][0] = item['stock'][0].replace('\n',"").strip()
        item['location_id'] = [self.location_id]
        item['store_id'] = [self.store_id]
        item['sku_id'] = [self.sku]
    
          
        return storeItem(item, response)
 
def storeItem(item, response):
    
    sql_fetch_session_id_all= 'SELECT max(id) FROM scrape_sessions'
    cursor.execute(sql_fetch_session_id_all)
    connection.commit()
    current_session_id = []
    for id in cursor:
        session_id = str(id[0])
    name = item['name']
    price = item['price']
    if len(price) < 1:
        price = ['Data Missing']
    stock = item['stock']
    rating = item['rating']
    asin_id  = item['sku_id']
    store_id = item['store_id']
    location_id = item['location_id']
    scrape_datetime= str(datetime.now())
    store_id = str(store_id[0])
    location_id = str(location_id[0]) 
    store_id = [store_id]
    location_id = [location_id]
    session_id = [session_id]
    print(name)
    print(price)
    print(stock)
    print(rating)
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print(asin_id)
    print(type(store_id))
    print(location_id)
    print(session_id)

    
    
     
    sql2 = 'INSERT INTO scrape_reports(scrape_session_id,sku_code, store_id, location_id, item_name, stock_available, item_price, store_rating, scrape_datetime ) values("'+session_id[0]+'","'+asin_id[0]+'","'+store_id[0]+'","'+location_id[0]+'","'+name[0]+'","'+stock[0]+'", "'+price[0]+'", "'+rating[0]+'","'+scrape_datetime+'")'
    print(sql2)
    cursor.execute(sql2)
    connection.commit()
#     Saving data in csv file.
    csvFile = open('products.csv', 'w+', newline='')
    writer = csv.writer(csvFile)
    writer.writerow((name[0], price[0], stock[0], rating[0]))
    csvFile.close() 
    return item
# 
#      
# # Setting browser version
process = CrawlerProcess({
    'USER_AGENT': (
            'Chrome/69.0.3497.81')
})
# #      
# #     # Invoking Spiders to crawl data  
# # process.crawl(GroferSpider)
# # process.crawl(AmazonSpider)
# # process.start()
# print('Process Stopped')
   
# process.start()



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




    
    

for store, store_id in cursor1:
    print(store)
    print(store_id)
    sql = "SELECT item_sku_codes.sku_code, stores.base_url FROM item_sku_codes, stores WHERE stores.store_name = '"+store+"' AND item_sku_codes.store_id = stores.id"
    print(cursor2.execute(sql))
    for sku, base_url in cursor2:
        print('+++++++++++++++++++++++++++')
        print(sku)
        print('+++++++++++++++++++++++++++')
        print(base_url)
        sql = 'SELECT store_locations.id, city_area, pin_code FROM store_locations,stores WHERE stores.id = store_locations.store_id'
        cursor3.execute(sql)
        for location_id,area,pincode in cursor3:
            print(location_id)
            print(pincode)
            print(area)
            for root, dirs, files in os.walk('cookies/amazon_pincodes/'):
                print(root)
                print(dirs)
                print(files)
                if pincode+'.pkl' in files:
                    print('=======ddddddddddddd========= '+pincode+' ')
                    pass
                else:
                    ClearCookies()
                    ChangeLocation(pincode, store, base_url, location_id, store_id, sku)
            process.crawl(AmazonSpider, base_url = base_url, pincode = pincode, sku = sku, location_id = location_id, store_id = store_id, store = store)
#             process.crawl(AmazonSpider, base_url = base_url, pincode = pincode, sku = sku, location_id = location_id, store_id = store_id)


                
process.start()
sql_fetch_session_id_all= 'SELECT max(id) FROM scrape_sessions'
cursor.execute(sql_fetch_session_id_all)
current_session_id = []
for id in cursor:
    session_id = str(id[0])

end_time = str(datetime.now())
if ab == 1:
    scrape_result = 'SUCCESSFUL'
else:
    scrape_result = 'FAILED'

sql_update_end_time_and_status = 'UPDATE scrape_sessions SET session_end_datetime = "'+end_time+'", scrape_result = "'+scrape_result+'" where id = "'+session_id+'" '
cursor.execute(sql_update_end_time_and_status)
connection.commit()


print(cursor)
