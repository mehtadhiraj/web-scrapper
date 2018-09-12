
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

# Connect to the database.
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='123',                             
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
    
# A spider to crap grofers.com
class GroferSpider(scrapy.Spider):
    # SQL
    sql = "SELECT producturlname, id FROM `skus` WHERE website = 'grofers'";
    # Execute query
    cursor.execute(sql)
    name = "GroferSpider"
    start_urls = []
    allowed_domains = ['www.grofers.com']  # Allowed domain for grofers
    base_url = 'https://www.grofers.com/prn/' # Base url gor grofers
    for url in cursor:
        # Appending product name found in URL and a product id
        start_urls.append(base_url+url[0]+'/prid/'+url[1])
    print("=================================================\n")
    print(start_urls)   
    # Parsing to scrap data  
    def parse(self, response):
        item = Item()
        item['name']=response.css('.LinesEllipsis::text').extract()
        item['offer']=response.css('.offer-text::text').extract()
        item['price']=response.css('.pdp-product__price--new::text').extract()
        item['price']=[item['price'][1]]
#         item['stock']=response.css('#app > div > div.os-windows > div:nth-child(6) > div > div > div.pdp-wrapper > div.wrapper.pdp__top-container.pdp-wrapper--variant > div > div > div.pdp-product__container > div.pdp-product.pdp-product__move-top > div.pdp-product__variants-list > div > div > div.product-variant__list > button::text').extract()
        item['rating']= ['Not available']
        item['stock']=['Data Unavailable']
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
     
    def parse(self, response):
        item = Item()
        item['name']=response.css('#productTitle::text').extract()
        item['rating']=response.css('#acrPopover > span.a-declarative > a > i.a-icon.a-icon-star.a-star-4 > span::text').extract()
        item['price']=response.css('#priceblock_ourprice::text').extract()
        item['offer']=response.css('#regularprice_savings > td.a-span12.a-color-price.a-size-base::text').extract()
        item['stock']=response.css('#availability > span::text').extract()
        item['name'][0] = item['name'][0].replace('\n',"").strip() # Striping data to remove blank spaces
        return storeItem(item, response)
 
# Storing Item in database
def storeItem(item, response):
    name = item['name']
    offer = item['offer']
    price = item['price']
    stock = item['stock']
    rating = item['rating']
    print(name)
    print(offer)
    print(price)
    print(stock)
    print(rating)
    sql = 'INSERT INTO productdetails(name, offer, price, stock, rating) values("'+name[0]+'","'+offer[0]+'","'+price[0]+'", "'+stock[0]+'", "'+rating[0]+'")'
    cursor.execute(sql)
    connection.commit()
    # Saving data in csv file.
    csvFile = open('products.csv', 'a+', newline='')
    writer = csv.writer(csvFile)
    writer.writerow((name[0], offer[0], price[0], stock))
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









