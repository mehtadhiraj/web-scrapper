
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
    cJar = cookies.chrome(domain_name='grofers.com')
    cJar1 = {c.name: c.value for c in cJar}
#     del cJar1['session-id-time']
#     del cJar1['visitCount']
    for c in cJar:
        print(c)
    print(cJar1)
#    Replace PINCODE below
    with open('cookies/grofers_pincodes/400701.pkl', 'wb') as fp: pickle.dump(cJar1, fp)    
getChromeCookies()

# # Connect to the database.
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',                             
    db='web-scrapper',
)
 
print ("Database Connection Established") 
cursor  = connection.cursor()
 
# define the fields for your item here like
class Item(scrapy.Item):
    name = scrapy.Field()
    offer = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    rating = scrapy.Field()
    website = scrapy.Field()

#A spider to crap grofers.com
class GroferSpider(scrapy.Spider):
    # SQL
    sql = "SELECT id FROM `skus` WHERE website = 'grofers'";
    # Execute query
    cursor.execute(sql)
    name = "GroferSpider"
    start_urls = []
    allowed_domains = ['www.grofers.com']  # Allowed domain for grofers
    base_url = 'https://www.grofers.com/prn//prid/' # Base url gor grofers
    for url in cursor:
        # Appending product name found in URL and a product id
        start_urls.append(base_url+url[0])
    print("=================================================\n")
    print(start_urls)  
    
# Cookie based data scraping
    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        with open('./cookies/grofers_pincodes/400701.pkl', 'rb') as fp: cookieJar = pickle.load(fp)
        print(cookieJar)
        for i,url in enumerate(self.start_urls):
            yield Request(url,cookies=cookieJar, callback=self.parse, headers=headers)
      
    # Parsing to scrap data  
    def parse(self, response):
        item = Item()
        item['name']=response.css('.LinesEllipsis::text').extract()
        item['offer']=response.css('.offer-text::text').extract()
        item['offer']='No Offer'
        item['price']=response.css('.pdp-product__price--new::text').extract()
        item['price']=[item['price'][1]]
#         item['stock']=response.css('#app > div > div.os-windows > div:nth-child(6) > div > div > div.pdp-wrapper > div.wrapper.pdp__top-container.pdp-wrapper--variant > div > div > div.pdp-product__container > div.pdp-product.pdp-product__move-top > div.pdp-product__variants-list > div > div > div.product-variant__list > button::text').extract()
        item['rating']= ['Data Missing']
        item['stock']= response.css('.pdp-product__out-of-stock::text').extract()
        #item['stock']=['Data missing']
        item['website']='Grofers'
        print(item['stock'])
        return storeItem(item, response)  
                 
class AmazonSpider(scrapy.Spider):
    #SQL
    sql = "SELECT producturlname, id FROM `skus` WHERE website = 'amazon'";
    #Execute query
    cursor.execute(sql)
     
    name = "AmazonSpider"
    allowed_domains = ['www.amazon.in']
    base_url = 'https://www.amazon.in/dp/'
    start_urls = []
    for url in cursor:
        start_urls.append(base_url+url[1])
    print("=================================================\n")
    print(start_urls)
# Cookie based data scraping    
    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}
        with open('cookies/amazon_pincodes/400701.pkl', 'rb') as fp: cookieJar = pickle.load(fp)
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
        item['website']='Amazon'
        item['name'][0] = item['name'][0].replace('\n',"").strip() # Striping data to remove blank spaces
    
        return storeItem(item, response)
  
# Storing Item in database
def storeItem(item, response):
    name = item['name']
    offer = item['offer']
    price = item['price']
    stock = item['stock']
    rating = item['rating']
    website = item['website']

    print(name)
    print(offer)
    print(price)
    print(stock)
    print(rating)
    print(website)
    sql = 'INSERT INTO productdetails(name, offer, price, stock, rating, website) values("'+name[0]+'","'+offer[0]+'","'+price[0]+'", "'+stock[0]+'", "'+rating[0]+'", "'+website[0]+'")'
    cursor.execute(sql)
    connection.commit()
#     Saving data in csv file.
    csvFile = open('products.csv', 'a+', newline='')
    writer = csv.writer(csvFile)
    writer.writerow((name[0], offer[0], price[0], stock[0], rating[0], website[0]))
    csvFile.close() 
    return item
 
# Setting browser version
process = CrawlerProcess({
    'USER_AGENT': (
            'Chrome/69.0.3497.81')
})
 
# Invoking Spiders to crawl data  
process.crawl(GroferSpider)
process.crawl(AmazonSpider)
process.start()
print('Process Stopped')
process.stop()









