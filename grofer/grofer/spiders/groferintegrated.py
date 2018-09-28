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



def ChangeLocationgrofers(pincode, store, base_url, location_id, store_id, sku, area):

    browser = webdriver.Chrome('chromedriver.exe')
    url = base_url+sku
    print(url)
    browser.get(url)
    time.sleep(2)

    location = browser.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div[2]/header/div[1]/a')
    location[0].click()
    time.sleep(2)

    city = browser.find_elements_by_tag_name('input')
    city[0].send_keys(area)
    time.sleep(2)

    city[0].send_keys(Keys.ENTER)
    time.sleep(2)
    
    browser.close()
    
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

    cJar = cookies.chrome(domain_name='grofers.com')
    cJar1 = {c.name: c.value for c in cJar}
#     del cJar1['session-id-time']
#     del cJar1['visitCount']
    print(cJar)
#    Replace PINCODE below
    with open('cookies/'+store+'_pincodes/'+pincode+'.pkl', 'wb') as fp: pickle.dump(cJar1, fp)
    # # Setting browser version
    
class GroferSpider(scrapy.Spider):
    def __init__(self, base_url, pincode, sku, location_id, store_id, store):
        self.base_url = base_url
        self.pincode = pincode
        self.area = area
        self.sku = sku
        self.location_id = location_id
        self.store_id = store_id
        self.store = store
         
# Requesting a Cookies for location based data scraping
    def start_requests(self):
          
        print('===========================================')
    #     print(self.pincode)
        print('Scrapy.Spider')
        print(scrapy.Spider)
        name = "GroferSpider"
        start_urls = [self.base_url+self.sku]
        allowed_domains = ['www.grofers.com']  # Domain allowed by this spider
        print(start_urls)   
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        '''
        Open pkl file stored with stored by the name same as pincode 
        Append a pincode in the path below.
        "pin" is defined global 
        storing the following pkl file as a dictionary in a "cookieJar"
          
        '''
        with open('./cookies/grofers_pincodes/'+self.pincode+'.pkl', 'rb') as fp: cookieJar = pickle.load(fp) 
        print(cookieJar)
        # Passing URL cookieJar and the headers to scrap location based values.
        for i,url in enumerate(start_urls):
            yield Request(url,cookies=cookieJar, callback=self.parse, headers=headers)
              
    # Parsing to scrap data  
    def parse(self, response):
        item = Item() # Creating an object of class Item
        item['name']=response.css('.LinesEllipsis::text').extract()
        item['price']=response.css('.pdp-product__price--new::text').extract()
        item['price']=[item['price'][1]]
#         item['stock']=response.css('#app > div > div.os-windows > div:nth-child(6) > div > div > div.pdp-wrapper > div.wrapper.pdp__top-container.pdp-wrapper--variant > div > div > div.pdp-product__container > div.pdp-product.pdp-product__move-top > div.pdp-product__variants-list > div > div > div.product-variant__list > button::text').extract()
        item['rating']= ['Not Applicable']
         
        '''
        Grofers give the stock availability in the form of buttons
        Stock unavailable is also in the form of button 
        Hence data fetched is of both available and unavailable.
        '''
        item['stock']= response.css('.product-variant__btn::text').extract()
        # It consists of data from a button that is unavailable. 
        outOfStock = response.css('.product-variant__btn--disabled::text').extract()
        #Hence using set operation data of unavailable product is removed from the complete list. 
        item['stock'] = list(set(item['stock'])-set(outOfStock))
        #Now applying a join operation to store the data on a 0th index.
        item['stock'] = [', '.join(item['stock'])]
        # After all the operation if stock is still empty we store the status as Unavailable
        if item['stock'][0] == '':
            item['stock'] = ['Curently Unavailable']
        item['location_id'] = [self.location_id]
        item['store_id'] = [self.store_id]
        item['sku_id'] = [self.sku]
        
        return storeItem(item, response)


 # Creating Cookies form Chrome
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
            area = area.split('_')
            area = area[0]
            print(area)
            
            for root, dirs, files in os.walk('cookies/grofers_pincodes/'):
                print(root)
                print(dirs)
                print(files)
                if pincode+'.pkl' in files:
                    print('=======ddddddddddddd========= '+pincode+' ')
                    pass
                else:
                    ClearCookies()
                    if store == 'grofers':
                        ChangeLocationgrofers(pincode, store, base_url, location_id, store_id, sku, area)
            process.crawl(GroferSpider, base_url = base_url, pincode = pincode, sku = sku, location_id = location_id, store_id = store_id, store = store)
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
