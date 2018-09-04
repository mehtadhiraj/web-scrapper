# -*- coding: utf-8 -*-
import scrapy
import pymysql
 
connection = pymysql.connect(host='localhost',
                      user='root',
                      password='',
                      db='webscrapper',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)
 
cursor = connection.cursor()
 
# Selecting.
query = "SELECT `*` FROM `sku_master`"
result=cursor.execute(query)
for res in result:
    print (res)
    

 

    
 
# Inserting
#query = "INSERT INTO `table` (id) VALUES (1)"
#cursor.execute(query)
 
#connection.commit() # You need this if you want your changes 'commited' to the database.


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['www.amazon.in/Mi-Redmi-5-Black-32GB/dp/B077PWBC7J/ref=sr_1_1?s=electronics&ie=UTF8&qid=1535955509&sr=1-1&keywords=redmi+note+5.html']
    start_urls = ['https://www.amazon.in/Mi-Redmi-5-Black-32GB/dp/B077PWBC7J/ref=sr_1_1?s=electronics&ie=UTF8&qid=1535955509&sr=1-1&keywords=redmi+note+5.html/']

    def parse(self, response):
       #Extract product information
       titles = response.css('#productTitle::text').extract()
       stock = response.css('.a-size-medium.a-color-success::text').extract()
       prices = response.css('#priceblock_ourprice::text').extract()
       discounts = response.css('.a-span12.a-color-price.a-size-base::text').extract()


       for item in zip(titles,prices,stock,discounts):
           scraped_info = {
               'title' : item[0],
               'price' : item[1],
               'stock' : item[2], #Set's the url for scrapy to download images
               'discount' : item[3]
           }

           yield scraped_info
