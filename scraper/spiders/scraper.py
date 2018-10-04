# from twisted.internet import reactor 
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
from boto.cloudtrail.exceptions import InvalidTimeRangeException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.chrome.options import Options
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
import browser_cookie3 as cookies
from scrapy.utils.log import configure_logging
import os, fnmatch
from filecmp import clear_cache
global response
from datetime import datetime
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import os
exec(compile(source=open('logger_init.py').read(), filename='logger_init.py', mode='exec'))
 

#DATABASE CONNECTIVITY AS SPECIFIED IN database_config.py
exec(compile(source=open('database_config.py').read(), filename='database_config.py', mode='exec'))
 
    
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
    try: 
#         options = Options()
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
        logger.info('Cookies Cleared Successfully')
        driver.close()
    except Exception as e:
        print(e)
        logger.exception(e)   
     
# Creating Cookies form Chrome
def ChangeLocationAmz(pincode, store, base_url, location_id, store_id, sku): 
    try:
        allowed_domains = [store]
        start_urls = base_url+sku
         
        # Creating an instance webdriver 
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')   
        browser = webdriver.Chrome('chromedriver.exe',chrome_options=options)
        
        browser.get(start_urls) 
           
        # Let's the user see and also load the element  
        time.sleep(2) 
            
        location = browser.find_elements_by_xpath('//*[@id="nav-global-location-slot"]/span/a') 
          
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
        
        apply[0].click()
        time.sleep(2)
         
        done = browser.find_elements_by_name('glowDoneButton')
        
        
        done[0].click()
        time.sleep(2)  
        driver = webdriver.Chrome()
        
        time.sleep(2)
        driver.close()
        logger.info('Location changed to '+str(location_id)+' in Amz')
        GetChromeCookies(pincode, store, base_url, location_id, store_id, sku)
    except Exception as e:
        print(e) 
        logger.critical(e)

# Store2 Change Location

def ChangeLocationGrff(pincode, store, base_url, location_id, store_id, sku, area):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')   
        browser = webdriver.Chrome('chromedriver.exe',chrome_options=options)
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
        logger.info('Location changed to '+str(location_id)+' in Grff')

        GetChromeCookies(pincode, store, base_url, location_id, store_id, sku)
    except Exception as e:
        print(e)
        logger.critical(e)
    
def ChangeLocationBbs(pincode, store, base_url, location_id, store_id, sku, area, session_id):
    try:
        start_urls= base_url+sku
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')   
        browser = webdriver.Chrome('chromedriver.exe',chrome_options=options)
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
        
        randomclick[0].click()
        time.sleep(2)
        
        complete = browser.find_elements_by_css_selector('#choose-city-form > div.ng-scope > div.btn-green > button')

        complete[0].submit()
        time.sleep(2)
        flag=1
        logger.info('Location changed to '+str(location_id)+' in Bbs')
    
        browser.close()
        
        GetChromeCookies(pincode, store, base_url, location_id, store_id, sku)
                
    except ElementNotVisibleException as elem_not_vis:
        print(elem_not_vis)
        
        browser.close()
        session_id  = [str(session_id)]
        
        
        
        name=["Not Available"]
        price=["00.00"]
        stock=["Currently Unavailable"]
        rating=["Not Available"]
        scrape_datetime= str(datetime.now())
        print(sku)
        print(location_id)
        print(store_id)
        
        sql2 = 'INSERT INTO scrape_reports(scrape_session_id,sku_code, store_id, location_id, item_name, stock_available, item_price, store_rating, scrape_datetime ) values("'+session_id[0]+'","'+str(sku)+'","'+str(store_id)+'","'+str(location_id)+'","'+name[0]+'","'+stock[0]+'", "'+price[0]+'", "'+rating[0]+'", "'+scrape_datetime+'")'

        cursor.execute(sql2)
        connection.commit()
        logger.exception('Bbs data not available for '+sku+'.')
        browser.close()


 
def GetChromeCookies(pincode, store, base_url, location_id, store_id, sku) -> None:
    '''
    Utility Function to save a new location.
    
    Change to the required new location in Chrome browser by going to 
    store1 site before calling this function.

    Only to be used to capture cookies for a new PINCODE.  We save and reuse 
    these cookies to pass with the http request for the right PINCODE.

    Alternative is to use Selenium webdrivers for browser automation.
          
    '''
    try:
        cJar = cookies.chrome(domain_name=store)
        
        
            
        cJar1 = {c.name: c.value for c in cJar}#{i.name: i for i in list(j)}
        
        
    #    Replace PINCODE below
        base_folder1 = os.path.dirname(__file__)+'/cookies/'
        if not os.path.exists(base_folder1):
            os.makedirs(base_folder1)
        with open('cookies/'+str(store_id)+'_'+str(pincode)+'.pkl', 'wb') as fp: pickle.dump(cJar1, fp)
        logger.info('New Chromw cookies Collected')
        
    except TypeError as te:
        print(te)
        
    except Exception as e:
        print(e)
        logger.exception(e)
        
#SENDING MAIL
def mailgeneration(store_id,store,session_id):   
    try:
        sql='select recipient_email from report_recipients where is_active = 1' 
        cursor4.execute(sql)
        fromaddr = "vivekiyer98@gmail.com"
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
        msg['Subject'] = "Product Availability Report"
            
        # string to store the body of the mail 
        body = "Please find attached the report file(s)"
            
        # attach the body with the msg instance 
        msg.attach(MIMEText(body, 'plain')) 
                   
        # open the file to be sent  
        path = "csv_files/"
        pattern = "*_sid"+str(session_id)+".csv"
        filenames = []
        for root, dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    #filenames.append(os.path.join(root, name))
                    filenames.append(name)
                 
     
        print(filenames)
          
        if len(filenames) == 0:
            raise Exception
          
        for file in filenames:  
        # instance of MIMEBase and named as p 
              part = MIMEBase('application', 'octet-stream')
              part.set_payload(open(path+file, 'rb').read())
              encoders.encode_base64(part)
              part.add_header('Content-Disposition', 'attachment; filename="%s"' % file)
              msg.attach(part)
        # creates SMTP session 
        s = smtplib.SMTP(host='smtp.gmail.com',port=587,timeout=300) 
            
        # start TLS for security 
        s.starttls() 
            
        # Authentication 
        s.login(fromaddr, "messi2009") 
            
        # Converts the Multipart msg into a string 
        text = msg.as_string() 
            
        # sending the mail 
        s.sendmail(fromaddr, toaddr, text) 
           
        # terminating the session 
        s.quit() 
          
        logger.info('Mail Sent successfully.')
        end_time = str(datetime.now())
        sql_update_end_time_and_status = 'UPDATE scrape_sessions SET session_end_datetime = "'+end_time+'", email_status = 1 where id = "'+str(session_id)+'" '
        cursor.execute(sql_update_end_time_and_status)
        connection.commit()
       
    except Exception as e:
        logger.error(e)
        logger.error('Mail sending failed.')
        end_time = str(datetime.now())
        sql_update_end_time_and_status = 'UPDATE scrape_sessions SET session_end_datetime = "'+end_time+'", email_status = 0 where id = "'+str(session_id)+'" '
        cursor.execute(sql_update_end_time_and_status)
        connection.commit()
       

    
#GENERATING CSV FILE    
def csvfilegeneration(session_id, sku_id, store_id, location_id, city, name, stock, price, rating, scrape_datetime, store, pincode):
    try:
        scrape_datetime = scrape_datetime.split('.')
        scrape_datetime = scrape_datetime[0]
        city = city.replace('_', ', ')
        base_folder = os.path.dirname(__file__)+'/csv_files/'
        if not os.path.exists(base_folder):
            os.makedirs(base_folder)    
        csv_path = base_folder+str(store_id[0])+'_sid'+session_id[0]+'.csv'
        file_exists = os.path.isfile(csv_path)
        if not file_exists:
            csvFile = open(csv_path, 'w', newline='')
            writehead = csv.DictWriter(csvFile, fieldnames = ["Session Id", "SKU Id", "Store Name", "Pincode","City, Area", "Product Name", "Stock Availability","Price in Rupees", "Rating", "Scrape Datetime"])    
            writehead.writeheader()
            csvFile.close()
            
        csvFile1 = open(csv_path, 'a+', newline='')
        writer = csv.writer(csvFile1)   
        writer.writerow((session_id[0], sku_id[0], store, pincode,city, name[0], stock[0], price[0], rating[0], scrape_datetime))
        csvFile1.close() 
        
    except FileNotFoundError:
        
        logger.error('CSV for store '+str(store_id)+' is not created')
    except Exception as e:
        print(e)
        logger.error(e)
#Spider to scrap store1 data
class AmzSpider(scrapy.Spider):
    def __init__(self, base_url, pincode, sku, location_id, store_id, store,city, area, session_id):
        self.base_url = base_url
        self.pincode = pincode
        self.area = area
        self.sku = sku
        self.location_id = location_id
        self.store_id = store_id
        self.store = store
        self.session_id = session_id
        self.city= city

 # Cookie based data scraping    
    def start_requests(self):               
        try:
            name = "AmzSpider"
            allowed_domains = [self.store] # Domains allowed in Store1's spider
            start_urls = [self.base_url+self.sku]
        
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}
            with open('cookies/'+str(self.store_id)+'_'+self.pincode+'.pkl', 'rb') as fp: cookieJar = pickle.load(fp)
            
            for i,url in enumerate(start_urls):
                yield Request(url,cookies=cookieJar, callback=self.parse, headers=headers)
                
        except FileNotFoundError:
            
           logger.critical('Requested Cookies does not exist')
        except Exception as e:
            print(e)
            logger.error(e)
            
    def parse(self, response):
        try:
            item = Item()
            item['name']=response.css('#productTitle::text').extract()
            if len(item['name']) <1:
                item['name'] = ['Data Unavailable']
            
            
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
        except Exception as e:
            print(e)
            logger.critical(self.sku+' data missing')
        finally:    
            return storeItem(item, self.store, self.session_id,self.city, self.pincode, response)



class GrffSpider(scrapy.Spider):
    def __init__(self, base_url, pincode, sku, location_id, store_id, store, city, area, session_id):
        self.base_url = base_url
        self.pincode = pincode
        self.area = area
        self.sku = sku
        self.location_id = location_id
        self.store_id = store_id
        self.store = store
        self.session_id = session_id
        self.city = city
         
# Requesting a Cookies for location based data scraping
    def start_requests(self):
        try: 
            name = "GrffSpider"
            start_urls = [self.base_url+self.sku]
            allowed_domains = [self.store]  # Domain allowed by this spider
              
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
            '''
            Open pkl file stored with stored by the name same as pincode 
            Append a pincode in the path below.
            "pin" is defined global 
            storing the following pkl file as a dictionary in a "cookieJar"
              
            '''
            with open('cookies/'+str(self.store_id)+'_'+str(self.pincode)+'.pkl', 'rb') as fp: cookieJar = pickle.load(fp) 
            
            # Passing URL cookieJar and the headers to scrap location based values.
            for i,url in enumerate(start_urls):
                yield Request(url,cookies=cookieJar, callback=self.parse, headers=headers)
        
        except FileNotFoundError:
            
           logger.critical('Requested Cookies does not exist')
        except Exception as e:
            print(e)
            logger.error(e)
                  
    # Parsing to scrap data  
    def parse(self, response):
        try:    
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
            
        except Exception as e:
            print(e)
            logger.critical(self.sku+' data missing')
   
        finally:    
            return storeItem(item, self.store, self.session_id,self.city, self.pincode, response)

# Bbs Spider starts here
class BbsSpider():

    def scrape_item_with_variants(base_url, pincode, sku, location_id,city, store_id, store, area, session_id):
        try:
            start_urls= base_url+sku
            with open('cookies/'+str(store_id)+'_'+str(pincode)+'.pkl', 'rb') as fp: cookieJar = pickle.load(fp) 
           
      
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
    
            driver.get(start_urls)
            for cookiename,cookievalue in cookieJar.items():
                driver.add_cookie({'name':cookiename,'value':cookievalue,'path':'/','Secure':'True'})
                
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
                storeItemBbs(item1,sku,location_id,city,store_id,store, session_id, pincode)
            driver.close()
                
        except FileNotFoundError as e:
            print(e)
            logger.critical(e)
            driver.close()
        
        except TimeoutException:
            print ("Connection Timeout")
            logger.warning('Connection time out while collecting data for '+str(store_id)+'-'+str(sku))
            

    
            driver.close()
   
 
def storeItem(item, store, session_id,city, pincode, response):
    
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
    store_id = [str(store_id)]
    location_id = [str(location_id)]
    session_id = [str(session_id)]
    print(name)
    print(price)
    print(stock)
    print(rating)
    print(sku_id)
    print(store_id)
    print(location_id)
    print(session_id)
    print(store)

    try:    
        sql2 = 'INSERT INTO scrape_reports(scrape_session_id,sku_code, store_id, location_id, item_name, stock_available, item_price, store_rating, scrape_datetime ) values("'+session_id[0]+'","'+sku_id[0]+'","'+store_id[0]+'","'+location_id[0]+'","'+name[0]+'","'+stock[0]+'", "'+price[0]+'", "'+rating[0]+'","'+scrape_datetime+'")'
       
        cursor.execute(sql2)
        
        connection.commit()
        logger.info('Data of '+store+' - '+sku_id[0]+'  stored  Successfully')
        csvfilegeneration(session_id, sku_id, store_id, location_id, city, name, stock, price, rating, scrape_datetime, store, pincode)
    
    except Exception as e:
        print(e)
        logger.critical(e)
    
    finally:
        return item
         
def storeItemBbs(item,sku_id,location_id,city,store_id,store, session_id, pincode):
    
    name= [item[0]]
    price=[item[1]]
    price = [price[0].replace('Rs ','')]
    
    stock= ["Available"]
    rating= ["Not Applicable"]
    session_id = [str(session_id)]
    sku_id = [sku_id]
    location_id = [str(location_id)]
    store_id = [str(store_id)]
    scrape_datetime = str(datetime.now())
                        
    print(name)
    print(price)
    print(stock)
    print(rating)
    print(sku_id)
    print(store_id)
    print(location_id)
    print(store)
        
    try:
        sql2 = 'INSERT INTO scrape_reports(scrape_session_id,sku_code, store_id, location_id, item_name, stock_available, item_price, store_rating, scrape_datetime ) values("'+session_id[0]+'","'+sku_id[0]+'","'+store_id[0]+'","'+location_id[0]+'","'+name[0]+'","'+stock[0]+'", "'+price[0]+'", "'+rating[0]+'","'+scrape_datetime+'")'
      
        cursor.execute(sql2)
        connection.commit()
        logger.info('Data of '+store+' - '+sku_id[0]+'  stored  Successfully')
        
        csvfilegeneration(session_id, sku_id, store_id, location_id, city, name, stock, price, rating, scrape_datetime, store, pincode)
    except Exception as e:
        print(e)
        logger.critical(e)


