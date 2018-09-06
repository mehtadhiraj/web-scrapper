import scrapy
import pymysql
import pymysql.cursors
from twisted.conch.insults.window import cursor
from scrapy.crawler import CrawlerProcess
#from grofer.items import GroferItem

# Connect to the database.
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',                             
    db='web-scrapper',
    charset='utf8mb4',
)

print ("Database Connection Established")
cursor  = connection.cursor()
#SQL
sql = "SELECT producturlname, id FROM `skus` WHERE website = 'grofers'";
#Execute query
cursor.execute(sql)

class Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    offer = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()

class GroferSpider(scrapy.Spider):
    name = "GroferSpider"
    allowed_domains = ['www.grofers.com']
    base_url = 'https://www.grofers.com/prn/'
    start_urls = []
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
        name = item['name'][0]
        offer = item['offer'][0]
        price = item['price'][1]+"Rs."
        print("=============="+item['name'][0])
        print(item['offer'][0])
        print(item['price'][1]+"Rs.")
        print(item['stock'])
        return item
        
    
class AmazonSpider(scrapy.Spider):
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
        item['offer']=response.css('.a-span12.a-color-price.a-size-base::text').extract()
        item['price']=response.css('#priceblock_ourprice::text').extract()
        item['stock']=response.css('.a-size-medium.a-color-success::text').extract()
        name = item['name'][0]
        offer = item['offer'][0]
        price = item['price'][1]+"Rs."
        print("=============="+item['name'][0])
        print(item['offer'][0])
        print(item['price'][1]+"Rs.")
        print(item['stock'])
        
        return item

# Setting browser version
process = CrawlerProcess({
    'USER_AGENT': (
            'Chrome/69.0.3497.81')
})

process.crawl(GroferSpider)
process.start() 
