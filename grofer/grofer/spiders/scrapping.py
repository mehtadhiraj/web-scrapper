import scrapy
import pymysql
import pymysql.cursors
from twisted.conch.insults.window import cursor
from grofer.items import GroferItem

# Connect to the database.
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',                             
    db='web-scapper',
    charset='utf8mb4',
)

print ("Database Connection Established")
cursor  = connection.cursor()
    #SQL
sql = "SELECT link FROM `key-table` WHERE website = 'grofer'";
    #Execute query
cursor.execute(sql)
urls = []

class GroferSpider(scrapy.Spider):
    name = "GroferSpider"
    allowed_domains = ['www.grofers.com']
    start_urls = []
    for url in cursor:
        start_urls.append(url[0])
    
    def parse(self, response):
        item = GroferItem()
        item['name']=response.css('.LinesEllipsis::text').extract()
        item['offer']=response.css('.offer-text::text').extract()
        item['price']=response.css('.pdp-product__price--new::text').extract()
        name = item['name'][0]
        offer = item['offer'][0]
        price = item['price'][1]+"Rs."
        print("=============="+item['name'][0])
        print(item['offer'][0])
        print(item['price'][1]+"Rs.")
        cursor=connection.cursor()
        sql = "INSERT INTO `product`(`name`, `discount`, `price`) VALUES('"+name+"','"+offer+"','"+price+"Rs.')"
        cursor.execute(sql)
        #print("======================================================="+str(res[0]))
        return item








# #Sending an http requests. 
# #veryfying sertificate = false as there are some missing certificates from grofer during hand shake
# res = requests.get('https://grofers.com/',verify = False)
# #Getting a source code in an organized format using a beautiful soup
# soup = BeautifulSoup(res.text, 'lxml')
# #====Finding the required components from the web page
# offer = soup.find('div', {'class': 'plp-product__offer'}).text
# productName = soup.find('div', {'class': 'plp-product__name--box'}).text
# quantity = soup.find('div', {'class': 'plp-product__quantity'}).text
# price = soup.find('span', {'class': 'plp-product__price--new'}).text
# #creating a dictioanery of the details
# product = {
#     'name' : productName,
#     'offer' : offer,
#     'quantity' : quantity,
#     'price' : price
#     }
# #Printitng all  the product details
# print('====================================\nDetails of product are as follows\n====================================')
# print('Name        : '+product['name'])
# print('Offer       : '+product['offer'])
# print('Quantity    : '+product['quantity'])
# print('Price       : '+product['price']+'Rs.')