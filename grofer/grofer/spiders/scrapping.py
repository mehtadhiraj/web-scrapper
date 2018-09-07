import scrapy
import pymysql
import csv
import pymysql.cursors
from twisted.conch.insults.window import cursor
from scrapy.crawler import CrawlerProcess
from twisted.conch.test.test_helper import FakeDelayedCall
#from grofer.items import GroferItem

# Connect to the database.
connection = pymysql.connect(
    host='10.0.8.94',
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
    
# A spider to crap grofers.com
class GroferSpider(scrapy.Spider):
    #SQL
    sql = "SELECT producturlname, id FROM `skus` WHERE website = 'grofers'";
    #Execute query
    cursor.execute(sql)
    name = "GroferSpider"
    start_urls = []
    allowed_domains = ['www.grofers.com']
    base_url = 'https://www.grofers.com/prn/'
    for url in cursor:
        start_urls.append(base_url+url[0]+'/prid/'+url[1])
    print("=================================================\n")
    print(start_urls)     
    def parse(self, response):
        item = Item()
        item['name']=response.css('.LinesEllipsis::text').extract()
        item['offer']=response.css('.offer-text::text').extract()
        item['price']=response.css('.pdp-product__price--new::text').extract()
        item['stock']=response.css('.product-variant__list::text').extract()
        item['name'][0] = item['name'][0].strip()
        name = item['name']
        offer = item['offer']
        price = item['price']
        stock = item['stock']
        print(name)
        print(offer)
        print(price)
        print(stock)
        csvFile = open('products.csv', 'a+', newline='')
        writer = csv.writer(csvFile)
        writer.writerow((name[0], offer[0], price[1]))
        csvFile.close()
        return item
                
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
        item['name'] = response.css('#productTitle::text').extract()
        item['offer'] = response.css('.a-span12.a-color-price.a-size-base::text').extract()
        item['price'] = response.css('#priceblock_ourprice::text').extract()
        item['stock'] =response.css('.a-size-medium.a-color-success::text').extract()
#         item['name'] = item['name'][0]
#         item['offer'] = item['offer']
#         item['price'] = item['price']
        
        item['name'][0] = item['name'][0].strip()
        name = item['name']
        offer = item['offer']
        price = item['price']
        stock = item['stock']
        print(name)
        print(offer)
        print(price)
        print(stock)
        
        csvFile = open('products.csv', 'a+', newline='')
        writer = csv.writer(csvFile)
        writer.writerow((name[0], offer[0], price[0]))
        csvFile.close()
        return item
#     Setting browser version
process = CrawlerProcess({
    'USER_AGENT': (
            'Chrome/69.0.3497.81')
})
  
process.crawl(GroferSpider)
process.crawl(AmazonSpider)

process.start()
print('Process Stopped')
process.stop()


