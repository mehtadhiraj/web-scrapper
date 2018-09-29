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
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

#DATABASE CONNECTIVITY AS SPECIFIED IN database_config.py
exec(compile(source=open('database_config.py').read(), filename='database_config.py', mode='exec'))


#  Connect to the database.
 
    
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
     
  
     
    result = driver.find_element_by_css_selector('* /deep/ #checkbox')
    result.click()
 
         
    time.sleep(2)
    clear = driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')
    clear.click()
    time.sleep(2)
    driver.close()
   
     
# Creating Cookies form Chrome
def ChangeLocationAmz(pincode, store, base_url, location_id, store_id, sku):
     

    allowed_domains = [store]
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
     
    
    change=browser.find_elements_by_xpath('//*[@id="GLUXChangePostalCodeLink"]')
    
    change[0].click()
    
    time.sleep(2)
     
    enterpincode=browser.find_elements_by_xpath('//*[@id="GLUXZipUpdateInput"]')
    enterpincode[0].clear()
    
    enterpincode[0].send_keys(pincode)
    time.sleep(2)
     
    apply=browser.find_elements_by_xpath('//*[@id="GLUXZipUpdate"]/span/input')
    print(apply)
    apply[0].click()
    time.sleep(2)
     
    done = browser.find_elements_by_name('glowDoneButton')
    
    
    done[0].click()
    time.sleep(2)  
    driver = webdriver.Chrome()
    
    time.sleep(2)
    driver.close()
    GetChromeCookies(pincode, store, base_url, location_id, store_id, sku)
     

# Store2 Change Location

def ChangeLocationGrff(pincode, store, base_url, location_id, store_id, sku, area):

    browser = webdriver.Chrome('chromedriver.exe')
    url = base_url+sku
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
    
    
def ChangeLocationBbs(pincode, store, base_url, location_id, store_id, sku,area):
    
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

        complete[0].submit()
        time.sleep(2)
        browser.close()
        flag=1
        GetChromeCookies(pincode, store, base_url, location_id, store_id, sku)
        

            
    except ElementNotVisibleException:
        print('cant be scrapped')
        driver.close()
        name=["Not Available"]
        price=["Not Available"]
        stock=["Not Available"]
        rating=["Not Available"]
        
        sql2 = 'INSERT INTO scrape_reports(scrape_session_id,sku_code, store_id, location_id, item_name, stock_available, item_price, store_rating, scrape_datetime ) values("'+session_id+'","'+sku_id[0]+'","'+store_id[0]+'","'+location_id[0]+'","'+name[0]+'","'+price[0]+'", "'+stock[0]+'", "'+rating[0]+'")'
        print(sql2)
        cursor.execute(sql2)
        connection.commit()

 
def GetChromeCookies(pincode, store, base_url, location_id, store_id, sku) -> None:
    '''
    Utility Function to save a new location.
    
    Change to the required new location in Chrome browser by going to 
    store1 site before calling this function.

    Only to be used to capture cookies for a new PINCODE.  We save and reuse 
    these cookies to pass with the http request for the right PINCODE.

    Alternative is to use Selenium webdrivers for browser automation.
          
    '''
    import browser_cookie3 as cookies

    cJar = cookies.chrome(domain_name=store)
    cJar1 = {c.name: c.value for c in cJar}

    print(cJar)
#    Replace PINCODE below
    with open('cookies/'+str(store_id)+'_'+pincode+'.pkl', 'wb') as fp: pickle.dump(cJar1, fp)

#SENDING MAIL

def mailgeneration(store,session_id):   
    sql='select recipient_email from report_recipients' 
    cursor4.execute(sql)
      
       
    fromaddr = "karthikmudaliar13@gmail.com"
    toaddr = [] 
    for mail in cursor4:
        toaddr.append(mail[0])
    print(toaddr)
    recipients = ', '.join(toaddr)   
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
      
    # storing the senders email address   
    msg['From'] = fromaddr 
      
    # storing the receivers email address  
    msg['To'] = recipients
      
    # storing the subject  
    msg['Subject'] = "abc"
      
    # string to store the body of the mail 
    body = "def"
      
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
             
    # open the file to be sent  
    files = "csv_files/"
    filenames = [os.path.join(files, f) for f in os.listdir(files)]
    print(filenames)
            
    csvfiles=filenames[-1].startswith(str(store_id)+'_sid'+str(session_id))
    print(csvfiles)
    #filename = "bbauto.txt"
    #attachment = open("C:/Users/Admin/Desktop/bbauto.txt", "rb") 
    for file in csvfiles:  
    # instance of MIMEBase and named as p 
          part = MIMEBase('application', 'octet-stream')
          part.set_payload(open(file, 'rb').read())
          encoders.encode_base64(part)
          part.add_header('Content-Disposition', 'attachment; filename="%s"' % file)
          msg.attach(part)
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
      
    # start TLS for security 
    s.starttls() 
      
    # Authentication 
    s.login(fromaddr, "karthik@1308") 
      
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
      
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
      
    # terminating the session 
    s.quit() 
    print("Mail Sent successfully")

    
#GENERATING CSV FILE    
def csvfilegeneration(session_id, sku_id, store_id, location_id, name, stock, price, rating, scrape_datetime, store):
    csv_path = 'csv_files/'+str(store_id[0])+'_sid'+session_id[0]+'.csv'
    csvFile = open(csv_path, 'a+', newline='')
    writer = csv.writer(csvFile)
    writer.writerow((session_id[0], sku_id[0], store_id[0], location_id[0], name[0], stock[0], price[0], rating[0], scrape_datetime))
    
    csvFile.close() 
    
    return 1

    
    
 
#Spider to scrap store1 data
class AmzSpider(scrapy.Spider):
    def __init__(self, base_url, pincode, sku, location_id, store_id, store, area):
        self.base_url = base_url
        self.pincode = pincode
        self.area = area
        self.sku = sku
        self.location_id = location_id
        self.store_id = store_id
        self.store = store

 # Cookie based data scraping    
    def start_requests(self):               
        name = "AmzSpider"
        allowed_domains = [self.store] # Domains allowed in Store1's spider
        start_urls = [self.base_url+self.sku]
        print(start_urls)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}
        with open('cookies/'+str(self.store_id)+'_'+self.pincode+'.pkl', 'rb') as fp: cookieJar = pickle.load(fp)
        print(cookieJar)
        for i,url in enumerate(start_urls):
            yield Request(url,cookies=cookieJar, callback=self.parse, headers=headers)
       
    def parse(self, response):
        item = Item()
        item['name']=response.css('#productTitle::text').extract()
        if len(item['name']) <1:
            item['name'] = ['Data Unavailable']
        
        print('=====================================================================')
        print(item['name'])
        item['rating']=response.css('#acrPopover > span.a-declarative > a > i.a-icon.a-icon-star.a-star-4 > span::text').extract()
        if len(item['rating']) <1:
            item['rating'] = ['Not applicable']
        item['price']=response.css('#priceblock_ourprice::text').extract()
         
        item['stock']=response.css('#availability > span::text').extract()
        if len(item['stock']) < 1:
            item['stock'] = ['Data Missing']
        else:
            item['stock'][0] = item['stock'][0].replace('\n',"").strip()
        # Striping data to remove blank spaces
        item['name'][0] = item['name'][0].replace('\n',"").strip() 
        item['location_id'] = [self.location_id]
        item['store_id'] = [self.store_id]
        item['sku_id'] = [self.sku]
    
          
        return storeItem(item, self.store, response)



class GrffSpider(scrapy.Spider):
    def __init__(self, base_url, pincode, sku, location_id, store_id, store, area):
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
        name = "GrffSpider"
        start_urls = [self.base_url+self.sku]
        allowed_domains = [self.store]  # Domain allowed by this spider
        print(start_urls)   
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        '''
        Open pkl file stored with stored by the name same as pincode 
        Append a pincode in the path below.
        "pin" is defined global 
        storing the following pkl file as a dictionary in a "cookieJar"
          
        '''
        with open('cookies/'+str(self.store_id)+'_'+str(self.pincode)+'.pkl', 'rb') as fp: cookieJar = pickle.load(fp) 
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
        store2 gives the stock availability in the form of buttons
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
        
        return storeItem(item, self.store, response)


class BbsSpider():
    
    
#     def __init__(self, base_url, pincode, sku, location_id, store_id, store, area):
#         
#         self.base_url = base_url
#         self.pincode = pincode
#         self.area = area
#         self.sku = sku
#         self.location_id = location_id
#         self.store_id = store_id
#         self.store = store  
#         print('+++++++++++++++++++++++--------------------------------000000000000000000000000000000000000000000000')
      #  scrape_item_with_variants(self,base_url, pincode, sku, location_id, store_id, store, area)

        

   
        
        
#     def start_requests(self):
      
#         start_urls = [self.base_url+self.sku]
#         print(start_urls)
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}
#         with open('cookies/'+str(self.store_id)+'_'+self.pincode+'.pkl', 'rb') as fp: cookieJar = pickle.load(fp)
#         print(cookieJar)
#         for i,url in enumerate(start_urls):
#             yield Request(url,cookies=cookieJar, callback=self.scrape_item_with_varaints, headers=headers)
       

#
    def scrape_item_with_variants(base_url, pincode, sku, location_id, store_id, store, area):
        
        print('+++++++++++++++++++++++--------------------------------000000000000000000000000000000000000000000000')
        
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}
#         with open('cookies/'+str(self.store_id)+'_'+self.pincode+'.pkl', 'rb') as fp: cookieJar = pickle.load(fp)
#         print(cookieJar)
#         for i,url in enumerate(start_urls):
#             yield Request(url,cookies=cookieJar, callback=self.parse, headers=headers)
#        
#         
#         print ("Scraping single item with no variants...")
#         
#         start_urls = base_url+sku
#         print('+++++++++++++`1+++++++++++++++++')
#         print(start_urls)
#         
        start_urls= base_url+sku
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
                storeItemBbs(item1,sku,location_id,store_id,store)
        except TimeoutException:
            print ("Connection Timeout")
        finally:
            driver.close()
   
 
def storeItem(item, store, response):
    
    sql_fetch_session_id_all= 'SELECT max(id) FROM scrape_sessions'
    cursor.execute(sql_fetch_session_id_all)
    connection.commit()
    current_session_id = []
    for id in cursor:
        session_id = str(id[0])
    name = item['name']
    price = item['price']
    if len(price) < 1:
        price = ['000.00']
    stock = item['stock']
    rating = item['rating']
    sku_id  = item['sku_id']
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
    print(sku_id)
    print(store_id)
    print(location_id)
    print(session_id)
    print(store)

    sql2 = 'INSERT INTO scrape_reports(scrape_session_id,sku_code, store_id, location_id, item_name, stock_available, item_price, store_rating, scrape_datetime ) values("'+session_id[0]+'","'+sku_id[0]+'","'+store_id[0]+'","'+location_id[0]+'","'+name[0]+'","'+stock[0]+'", "'+price[0]+'", "'+rating[0]+'","'+scrape_datetime+'")'
    print(sql2)
    cursor.execute(sql2)
    
    connection.commit()

    csvfilegeneration(session_id, sku_id, store_id, location_id, name, stock, price, rating, scrape_datetime, store)
    
    
    
     
def storeItemBbs(item,sku_id,location_id,store_id,store):
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
    print(store)
        
    sql2 = 'INSERT INTO scrape_reports(scrape_session_id,sku_code, store_id, location_id, item_name, stock_available, item_price, store_rating, scrape_datetime ) values("'+session_id[0]+'","'+sku_id[0]+'","'+store_id[0]+'","'+location_id[0]+'","'+name[0]+'","'+stock[0]+'", "'+price[0]+'", "'+rating[0]+'","'+scrape_datetime[0]+'")'
    print(sql2)
    cursor.execute(sql2)
    connection.commit()
    csvfilegeneration(session_id, sku_id, store_id, location_id, name, stock, price, rating, scrape_datetime, store)
    

    


#      
# exec(compile(source=open('main_program.py').read(), filename='main_program.py', mode='exec'))

# sql_fetch_session_id_all= 'SELECT max(id) FROM scrape_sessions'
# cursor.execute(sql_fetch_session_id_all)
# current_session_id = []
# for id in cursor:
#     session_id = str(id[0])
# 
# end_time = str(datetime.now())
# if ab == 1:
#     scrape_result = 'SUCCESSFUL'
# else:
#     scrape_result = 'FAILED'
# 
# sql_update_end_time_and_status = 'UPDATE scrape_sessions SET session_end_datetime = "'+end_time+'", scrape_result = "'+scrape_result+'" where id = "'+session_id+'" '
# cursor.execute(sql_update_end_time_and_status)
# connection.commit()




print(cursor)
