from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
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
import pickle
import requests
import time
import threading
global response


# Generating Cookies from chrome
def getChromeCookies() -> None:
    '''
    Utility Function to save a new location.
    
    Change to the required new location in Chrome browser by going to 
    Amazon.in sitebefore calling this function.

    Only to be used to capture cookies for a new PINCODE.  We save and reuse 
    these cookies to pass with the http request for the right PINCODE.

    Alternative is to use Selenium webdrivers for browser automation.
    '''
    import browser_cookie3 as cookies
    cJar = cookies.chrome(domain_name='bigbasket.com')
    cJar1 = {c.name: c.value for c in cJar}
    for c in cJar:
        print(c)
    print(cJar1)
#    Replace PINCODE below
    with open('cookies/bigbasket_pincodes/560029.pkl', 'wb') as fp: pickle.dump(cJar1, fp) # creating a pickel file of generated cookies

 # Creating Cookies form Chrome
getChromeCookies()

#  Connect to the database.
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',                             
    db='web-scrapper',
)
 
print ("Database Connection Established") 

cursor  = connection.cursor()

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
    
    print ("Scraping single item with no variants...")

    cursor = connection.cursor()
    sql = "SELECT id FROM `skus` WHERE producturlname = 'fresho-pav-chemical-free-300-gm'";
    # Execute query
    cursor.execute(sql)
    name = "GroferSpider"
    start_urls=[]
    allowed_domains = ['www.bigbasket.com']  # Domain allowed by this spider
    base_url = 'https://www.bigbasket.com/pd/' # Base url for grofers
    for url in cursor:
        # Appending a product id
        start_urls.append(base_url+url[0]+'//')
        print(start_urls) 
        
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
            #print(response)         


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
        
        
        print("Scraping item with variants...")
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome('C:/Users/Vivek Iyer/Desktop/web-crawler/web-scrapper/grofer/grofer/spiders/chromedriver.exe')
        driver.get(start_urls[0])
        try:
            element = WebDriverWait(driver, 60).until(
                    expected_conditions.presence_of_element_located((By.NAME, "size"))
                    )
            buttons = driver.find_elements_by_xpath('//*[@name="size"]')
            for ele in buttons:
                name = ele.get_attribute("id")
                lbl = driver.find_element_by_xpath("//*[@for=\""+ name +"\"]")
                lbl.click()
                item = driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div")
                price = driver.find_element_by_class_name("sc-bRBYWo")
                item1=[item,price]
                
                print(item.text + " " + price.text)
                storeItem(item1)
        except TimeoutException:
            print ("Connection Timeout")
        finally:
            driver.quit()
            


    def storeItem(item):
        name= item[0]
        price= item[1]
        if name:
            stock='AVAILABLE'
        else:
            stock='UNAVAILABLE'
        
    
        sql = 'INSERT INTO productdetails(name,price, stock) values("'+name[0]+'","'+price[0]+'", "'+stock+'")'
        print(sql)
        cursor.execute(sql)
        connection.commit()
#     Saving data in csv file.
        csvFile = open('products.csv', 'a+', newline='')
        writer = csv.writer(csvFile)
        writer.writerow((name[0],price[0], stock))
        csvFile.close() 
        return item
    
a= BigbasketSpider()
a.scrape_item_with_varaints()

            




#A spider to crap grofers.com
class GroferSpider(scrapy.Spider):
    # SQL
    print('Scrapy.Spider')
    print(scrapy.Spider)
    sql = "SELECT id FROM `skus` WHERE website = 'grofers'";
    # Execute query
    cursor.execute(sql)
    name = "GroferSpider"
    start_urls = []
    allowed_domains = ['www.grofers.com']  # Domain allowed by this spider
    base_url = 'https://www.grofers.com/prn//prid/' # Base url for grofers
    for url in cursor:
        # Appending a product id
        start_urls.append(base_url+url[0])
    print(start_urls)  
    
# Requesting a Cookies for location baed data scraping
    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        '''
        Open pkl file stored with stored by the name same as pincode 
        Append a pincode in the path below.
        "pin" is defined global 
        storing the following pkl file as a dictionary in a "cookieJar"
        
        '''
        with open('./cookies/grofers_pincodes/'+pin+'.pkl', 'rb') as fp: cookieJar = pickle.load(fp) 
        print(cookieJar)
        # Passing URL cookieJar and the headers to scrap location based values.
        for i,url in enumerate(self.start_urls):
            yield Request(url,cookies=cookieJar, callback=self.parse, headers=headers)
      
    # Parsing to scrap data  
    def parse(self, response):
        item = Item() # Creating an object of class Item
        item['name']=response.css('.LinesEllipsis::text').extract()
        item['offer']=response.css('.offer-text::text').extract()
        item['price']=response.css('.pdp-product__price--new::text').extract()
        item['price']=[item['price'][1]]
        item['rating']= ['Data Missing'] # For grofers no rating feature available. Hence stated as "Data Missing"
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
        item['website']=['Grofers']
        item['area'] = [location]
        item['pincode'] = [pin]
        return storeItem(item, response)  
                 
#Spider to Scrap data from Amazon
class AmazonSpider(scrapy.Spider):
    #SQL
    sql = "SELECT id FROM `skus` WHERE website = 'amazon'";
    #Execute query
    cursor.execute(sql)
     
    name = "AmazonSpider"
    allowed_domains = ['www.amazon.in'] # Domains allowed in Amazon's spider
    base_url = 'https://www.amazon.in/dp/'
    start_urls = []
    for url in cursor:
        start_urls.append(base_url+url[0])
    print(start_urls)
# Cookie based data scraping    
    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}
        with open('cookies/amazon_pincodes/'+pin+'.pkl', 'rb') as fp: cookieJar = pickle.load(fp)
        print(cookieJar)
        for i,url in enumerate(self.start_urls):
            yield Request(url,cookies=cookieJar, callback=self.parse, headers=headers)
      
    def parse(self, response):
        item = Item()
        item['name']=response.css('#productTitle::text').extract()
        item['rating']=response.css('#acrPopover > span.a-declarative > a > i.a-icon.a-icon-star.a-star-4 > span::text').extract()
        item['price']=response.css('#priceblock_ourprice::text').extract()
        item['offer']=response.css('#regularprice_savings > td.a-span12.a-color-price.a-size-base::text').extract()
        item['stock']=response.css('#availability > span::text').extract()
        item['website']=['Amazon']
        item['area'] = [location]
        item['pincode'] = [pin]
        # Striping data to remove blank spaces
        item['name'][0] = item['name'][0].replace('\n',"").strip() 
        item['stock'][0] = item['stock'][0].replace('\n',"").strip()
        
        return storeItem(item, response)
  
# Storing Item in database
def storeItem(item, response):
    name = item['name']
    offer = item['offer']
    price = item['price']
    stock = item['stock']
    rating = item['rating']
    website = item['website']
    loc = item['area']
    pincd = item['pincode']

    print(name)
    print(offer)
    print(price)
    print(stock)
    print(rating)
    print(website)
    print(pincd)
    print(loc)
    
    sql = 'INSERT INTO productdetails(name, offer, price, stock, rating, area, pincode, website) values("'+name[0]+'","'+offer[0]+'","'+price[0]+'", "'+stock[0]+'", "'+rating[0]+'", "'+loc[0]+'","'+pincd[0]+'","'+website[0]+'")'
    print(sql)
    cursor.execute(sql)
    connection.commit()
#     Saving data in csv file.
    csvFile = open('products.csv', 'a+', newline='')
    writer = csv.writer(csvFile)
    writer.writerow((name[0], offer[0], price[0], stock))
    csvFile.close() 
    return item
     
#     # Setting browser version
#     process = CrawlerProcess({
#         'USER_AGENT': (
#                 'Chrome/69.0.3497.81')
#     })
#      
#     # Invoking Spiders to crawl data  
#     process.crawl(GroferSpider)
#     process.crawl(AmazonSpider)
#     process.start()
#     print('Process Stopped')
    

# SQL query
sql = 'SELECT area, pincode FROM location'
# Execute query
cursor.execute(sql)
# Setting browser version
process = CrawlerProcess({
    'USER_AGENT': (
            'Chrome/69.0.3497.81')
})

# Looping through all the pincodes present in database 
for location, pincode in cursor:
    global pin, area # Defined global in order to access it in both the spiders
    pin = pincode
    print(pin)
    area = location
    print(area) 
    # Invoking spiders of grofer and amazon to crawl data.
    process.crawl(GroferSpider)
    process.crawl(AmazonSpider)
process.start() # Start the process to crawl
print('Process Stopped')







