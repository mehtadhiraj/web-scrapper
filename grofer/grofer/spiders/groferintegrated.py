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
# from you_get.extractors.huaban import Pin

global response

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


def ChangeLocationgrofers(pincode, store, base_url, location_id, store_id, sku):

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
    
    getChromeCookies(pincode, area, store)
    
def getChromeCookies(pincode, area, store) -> None:
    
    print(pincode)
    print(storename)
    print(area)
    '''
    Utility Function to save a new location.
    
    Change to the required new location in Chrome browser by going to 
    Amazon.in sitebefore calling this function.

    Only to be used to capture cookies for a new PINCODE.  We save and reuse 
    these cookies to pass with the http request for the right PINCODE.

    Alternative is to use Selenium webdrivers for browser automation.
    '''
    print("===================================================================")
    import browser_cookie3 as cookies
    if store == 'amazon':
        domain = store+'.in'
    else:
        domain = store+'.com'
    cJar = cookies.chrome(domain_name=domain)
    cJar1 = {c.name: c.value for c in cJar}
    for c in cJar:
        print(c)
    print(cJar1)
#    Replace PINCODE below

    #with open('cookies/_pincodes/.pkl', 'wb') as fp: pickle.dump(cJar1, fp)    
    url_append= 'cookies/'+store+'_pincodes/'+pincode+'.pkl'
    with open(url_append, 'wb') as fp: pickle.dump(cJar1, fp) # creating a pickel file of generated cookies
    
# class GroferSpider(scrapy.Spider):
#     def __init__(self, base_url, pincode, sku, location_id, store_id, store):
#         self.base_url = base_url
#         self.pincode = pincode
#         self.area = area
#         self.sku = sku
#         self.location_id = location_id
#         self.store_id = store_id
#         self.store = store
#         
# # Requesting a Cookies for location based data scraping
#     def start_requests(self):
#          
#         print('===========================================')
#     #     print(self.pincode)
#         print('Scrapy.Spider')
#         print(scrapy.Spider)
#         name = "GroferSpider"
#         start_urls = base_url+sku
#         allowed_domains = ['www.grofers.com']  # Domain allowed by this spider
#         print(start_urls)   
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
#         '''
#         Open pkl file stored with stored by the name same as pincode 
#         Append a pincode in the path below.
#         "pin" is defined global 
#         storing the following pkl file as a dictionary in a "cookieJar"
#          
#         '''
#         with open('./cookies/grofers_pincodes/'+self.pincode+'.pkl', 'rb') as fp: cookieJar = pickle.load(fp) 
#         print(cookieJar)
#         # Passing URL cookieJar and the headers to scrap location based values.
#         for i,url in enumerate(start_urls):
#             yield Request(url,cookies=cookieJar, callback=self.parse, headers=headers)
#              
#     # Parsing to scrap data  
#     def parse(self, response):
#         item = Item() # Creating an object of class Item
#         item['name']=response.css('.LinesEllipsis::text').extract()
#         item['price']=response.css('.pdp-product__price--new::text').extract()
#         item['price']=[item['price'][1]]
# #         item['stock']=response.css('#app > div > div.os-windows > div:nth-child(6) > div > div > div.pdp-wrapper > div.wrapper.pdp__top-container.pdp-wrapper--variant > div > div > div.pdp-product__container > div.pdp-product.pdp-product__move-top > div.pdp-product__variants-list > div > div > div.product-variant__list > button::text').extract()
#         item['rating']= ['Not Applicable']
#         
#         '''
#         Grofers give the stock availability in the form of buttons
#         Stock unavailable is also in the form of button 
#         Hence data fetched is of both available and unavailable.
#         '''
#         item['stock']= response.css('.product-variant__btn::text').extract()
#         # It consists of data from a button that is unavailable. 
#         outOfStock = response.css('.product-variant__btn--disabled::text').extract()
#         #Hence using set operation data of unavailable product is removed from the complete list. 
#         item['stock'] = list(set(item['stock'])-set(outOfStock))
#         #Now applying a join operation to store the data on a 0th index.
#         item['stock'] = [', '.join(item['stock'])]
#         # After all the operation if stock is still empty we store the status as Unavailable
#         if item['stock'][0] == '':
#             item['stock'] = ['Curently Unavailable']
#         item['location_id'] = [location_id]
#         item['store_id'] = [store_id]
#         item['sku_id'] = [sku]
#         return storeItem(item, response)


 # Creating Cookies form Chrome
connection = pymysql.connect(
   host='localhost',
   user='root',
   password='',                             
   db='scraperdb1',
)

print ("Database Connection Established") 

process = CrawlerProcess({
    'USER_AGENT': (
            'Chrome/69.0.3497.81')
})

cursor1 = connection.cursor()
cursor2 = connection.cursor()
cursor3 = connection.cursor()
print(cursor1)
sql='select store_name, id from stores'
cursor1.execute(sql)

for store, store_id in cursor1:
    print(store)
    print(store_id)
    sql = "SELECT item_sku_codes.sku_code, stores.base_url FROM item_sku_codes, stores WHERE stores.store_name = '"+store+"' AND item_sku_codes.store_id = stores.store_id"
    print(cursor2.execute(sql))
    for sku, base_url in cursor2:
        print(sku)
        print(base_url)
        sql='select id, city_area, pin_code from store_locations, stores where stores.id=store_locations.store_id'
        cursor3.execute(sql)
        for location_id, city_area, pincode in cursor3:
            print(location_id)
            print(pincode)
            print(area)
        for root, dirs, files in os.walk('cookies/amazon_pincodes/'):
            city, area = city_area.split('_')
            print(root)
            print(dirs)
            print(files)
            if pincode+'.pkl' in files:
                pass
            else:
                ClearCookies()
                ChangeLocation(pincode, store, base_url, location_id, store_id, sku, area)
#             process.crawl(AmazonSpider, base_url = base_url, pincode = pincode, sku = sku, location_id = location_id, store_id = store_id, store = store)

print(process)
print(process.memory_full_info())     
        

        