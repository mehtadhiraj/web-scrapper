from twisted.internet import reactor
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
from boto.cloudtrail.exceptions import InvalidTimeRangeException
import os
import psutil
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
    
    driver.close()
    
    
    #driver.manage().deleteAllCookies();    
     
# Creating Cookies form Chrome

def ChangeLocationbigbasket(pincode, url, sku, store):
    browser = webdriver.Chrome('chromedriver.exe')
    start_urls= url+sku
    browser.get('https://www.bigbasket.com/pd/40033824/fresho-apple-washington-regular-4-pcs/?nc=feat-prod&t_pg=l1-cat-fruits-vegetables&t_p=cl-temp-1&t_s=feat-prod&t_pos_sec=3&t_pos_item=1&t_ch=desktop')
    time.sleep(2)

    location = browser.find_elements_by_xpath('//*[@id="headercontroller"]/section[1]/div/div[2]/div/button')
    location[0].click()
    time.sleep(2)
    
    city = browser.find_elements_by_xpath('//*[@id="city-select"]')
    city[0].clear()
    city[0].send_keys('Mumbai')
    time.sleep(2)
    
    pin=pincode
    pincode1 = browser.find_elements_by_xpath('//*[@id="area-select"]')
    for pinc in pin:
        pincode1[0].send_keys(pinc)
        time.sleep(2)
    #pincode[0].send_keys(Keys.ENTER)
    #time.sleep(2)
    
    randomclick = browser.find_elements_by_css_selector('.ui-corner-all')
    print(randomclick)
    randomclick[0].click()
    time.sleep(2)
    
    complete = browser.find_elements_by_css_selector('#choose-city-form > div.ng-scope > div.btn-green > button')
    #print(complete)
    complete[0].submit()
    time.sleep(2)
    
    getChromeCookies(pincode,store,url)
    
    
    


# Generating Cookies from chrome
def getChromeCookies(pincode, store, url) -> None:
    
    print(pincode)
    print(store)
    print(url)
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
    cJar = cookies.chrome(domain_name='bigbasket.com')
    cJar1 = {c.name: c.value for c in cJar}
    for c in cJar:
        print(c)
    print(cJar1)
#    Replace PINCODE below

    #with open('cookies/_pincodes/.pkl', 'wb') as fp: pickle.dump(cJar1, fp) 
       
    folder_loc= 'cookies/'+store+'_pincodes/'+pincode+'.pkl'
    print(folder_loc)
    with open(folder_loc, 'wb') as fp: pickle.dump(cJar1, fp) # creating a pickel file of generated cookies

 # Creating Cookies form Chrome


    
#  Connect to the database.

process= psutil.Process(os.getpid())
print(process)
print(process.memory_full_info())     


'''
 Data that needs to be stored
 Defining a class consisting of required field
 
'''
class Item(scrapy.Item):
    name = scrapy.Field()
    offer = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    rating = scrapy.Field()
    area = scrapy.Field()
    pincode = scrapy.Field()
    website = scrapy.Field()

class BigbasketSpider():
      
      
          
    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        '''
        Open pkl file stored with stored by the name same as pincode 
        Append a pincode in the path below.
        "pin" is defined global 
        storing the following pkl file as a dictionary in a "cookieJar"
          
        '''
        with open('./cookies/bigbasket_pincodes/'+pin+'.pkl', 'rb') as fp: cookieJar = pickle.load(fp) 
        print(cookieJar)
        # Passing URL cookieJar and the headers to scrap location based values.
        for i,url in enumerate(self.start_urls):
            yield Request(url,cookies=cookieJar, callback=self.scrape_item_with_variants, headers=headers)
    def scrape_single_item(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome('C:/Users/Vivek Iyer/Desktop/web-crawler/web-scrapper/grofer/grofer/spiders/chromedriver.exe')
        driver.get(start_urls[0])
        try:
            element = WebDriverWait(driver, 60).until(
                    expected_conditions.presence_of_element_located((By.CLASS_NAME, "sc-bRBYWo"))
                    )
            item_desc = driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div")
            print (item_desc.text + " " + element.text)
        except TimeoutException:
            print ("Connection Timeout")
        finally:
            driver.quit()
    
    

          
    def scrape_item_with_varaints(self):
        print ("Scraping single item with no variants...")
  
        
          
        print("Scraping item with variants...")
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
        driver.get('https://www.bigbasket.com/pd/10000170/fresho-cabbage-red-1-kg/')
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
                item1,price1=item,price
                 
                print(item + " " + price)
                return item1,price1
        except TimeoutException:
            print ("Connection Timeout")
        finally:
            driver.quit()
             
 
        
connection = pymysql.connect(
   host='localhost',
   user='root',
   password='',                             
   db='scraperdb',
)

print ("Database Connection Established") 
cursor = connection.cursor()
cursor1  = connection.cursor()
cursor2  = connection.cursor()
cursor3  = connection.cursor()
    
sql = 'SELECT store_name, store_id FROM store'
cursor1.execute(sql)

def storeItem(item,price):
    skus_id= '10000170'
    store_id= 's1'
    location_id= 'l2'
    product_stock= 'In Stock'
    product_rating= '3.0 out of 5'
    name= item
    price= price
    if name:
        stock='AVAILABLE'
    else:
        stock='UNAVAILABLE'
     
    
    sql = 'INSERT INTO productdetails(skus_id, store_id, location_id, product_name, product_price, product_stock, product_rating) values("'+skus_id+'","'+store_id+'","'+location_id+'","'+name+'","'+price+'", "'+product_stock+'", "'+product_rating+'")'
    print(sql)
    cursor.execute(sql)
    connection.commit()
#     Saving data in csv file.
    csvFile = open('products.csv', 'a+', newline='')
    writer = csv.writer(csvFile)
    writer.writerow((name[0],price[0], stock))
    csvFile.close() 
    return item        


for store, store_id in cursor1:
    print(store)
    print(store_id)
    sql = "SELECT skus.sku_id, store.base_url FROM skus, store WHERE store.store_name = '"+store+"' AND skus.store_id = store.store_id"
    print(cursor2.execute(sql))
    for sku, base_url in cursor2:
        print(sku)
        print(base_url)
        sql = 'SELECT * FROM location'
        cursor3.execute(sql)
        for location_id, area, pincode in cursor3:
            print(location_id)
            print(pincode)
            print(area)
        for root, dirs, files in os.walk('cookies/bigbasket_pincodes/'):
                print(root)
                print(dirs)
                print(files)
                if pincode+'.pkl' in files:
                    pass
                else:
                    ClearCookies()
                    if store == 'bigbasket':
                        
                        ChangeLocationbigbasket(pincode, base_url, sku, store)
                    else:
                        print("SORRY")
                a= BigbasketSpider()
                item1,price1=a.scrape_item_with_varaints()
                print(item1)
                
                storeItem(item1,price1)

process= psutil.Process(os.getpid())
print(process)
print(process.memory_full_info())     
    
     
# a= BigbasketSpider()
# a.scrape_item_with_varaints()