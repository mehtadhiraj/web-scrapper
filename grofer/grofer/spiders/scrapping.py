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
    host='10.0.8.94',
    user='root',
    password='123',                             
    db='web-scrapper',
)

print ("Database Connection Established") 
cursor  = connection.cursor()

# define the fields for your item here like
class Item(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    offer = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    
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
        return storeItem(item, response)
 
# Storing the data in csv format   
def storeItem(item, response):
    item['name']=response.css('.LinesEllipsis::text').extract()
    item['offer']=response.css('.offer-text::text').extract()
    item['price']=response.css('.pdp-product__price--new::text').extract()
    item['stock']=response.css('.product-variant__list::text').extract()
    item['name'][0] = item['name'][0].strip() # Striping data to remove blank spaces
    name = item['name']
    offer = item['offer']
    price = item['price']
    stock = item['stock']
    
    print(name)
    print(offer)
    print(price)
    print(stock)
    sql = "INSERT INTO productdetails(name, offer, price, stock, rating) values('"+name[0]+"','"+offer[0]+"','"+price+"', '"+stock+"', '')"
    cursor.execute(sql)
    connection.commit()
    # Saving data inn csv file.
    csvFile = open('products.csv', 'a+', newline='')
    writer = csv.writer(csvFile)
    writer.writerow((name[0], offer[0], price[1], stock))
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


