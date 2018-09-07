import scrapy
import pymysql
import pymysql.cursors
from twisted.conch.insults.window import cursor
from scrapy.crawler import CrawlerProcess
from twisted.conch.test.test_helper import FakeDelayedCall
#from grofer.items import GroferItem

# Connect to the database.
connection = pymysql.connect(
    host='10.0.0.5',
    user='root',
    password='',                             
    db='web-scrapper',
    charset='utf8mb4',
)


print ("Database Connection Established") 
cursor  = connection.cursor()
print ("Database Connection Established")
cursor  = connection.cursor()
class Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
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
    name = "Spider"
    start_urls = []
    allowed_domains = ['www.grofers.com', 'www.amazon.in']
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
        name = item['name'][0]
        offer = item['offer'][0]
        price = item['price']
        print("=============="+name)
        print(item['offer'][0])
        print(item['price'])
        print(item['stock'])
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
        item['name']=response.css('#productTitle::text').extract()
        item['offer']=response.css('.a-span12.a-color-price.a-size-base::text').extract()
        item['price']=response.css('#priceblock_ourprice::text').extract()
        item['stock']=response.css('.a-size-medium.a-color-success::text').extract()
        name = item['name'][0]
        offer = item['offer']
        price = item['price']
        print("=============="+item['name'][0].strip())
        print(item['offer'])
        print(item['price'])
        print(item['stock'])
        item['name'] = item['name'][0].strip()
        return item
        
#     Setting browser version
process = CrawlerProcess({
    'USER_AGENT': (
            'Chrome/69.0.3497.81')
})
  
process.crawl(GroferSpider)
process.crawl(AmazonSpider)
process.crawl(GroferSpider)
process.crawl(AmazonSpider)
process.crawl(GroferSpider)
process.crawl(AmazonSpider)
process.crawl(GroferSpider)
process.crawl(AmazonSpider)
process.crawl(GroferSpider)
process.crawl(AmazonSpider)
process.crawl(GroferSpider)
process.crawl(AmazonSpider)
process.crawl(GroferSpider)
process.crawl(AmazonSpider)
process.crawl(GroferSpider)
process.crawl(AmazonSpider)
process.crawl(GroferSpider)
process.crawl(AmazonSpider)
process.crawl(GroferSpider)
process.crawl(AmazonSpider)

process.start()
print('Process Stopped')
process.stop()


