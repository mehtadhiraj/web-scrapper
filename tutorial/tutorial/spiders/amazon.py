# -*- coding: utf-8 -*-
import scrapy
import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='sample webscrapper',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor=connection.cursor()

query="Select `url` from `skuurl`"
cursor.execute(query)
result=cursor.fetchone()
for res in result:
    res=result['url']
    print(res)
    print(res[8:])

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = [res[8:]+'.html']
    start_urls = [res+'.html/']


    def parse(self, response):
        #Extracting the content using css selectors
        titles = response.css('#productTitle::text').extract()
        price = response.css('#priceblock_dealprice::text').extract()
        stock = response.css('.a-size-medium.a-color-success::text').extract()
        rating = response.css('.a-icon-alt::text').extract()
       
        #Give the extracted content row wise
        for item in zip(titles,price,stock,rating):
            #create a dictionary to store the scraped info
            scraped_info = {
                    'title' : item[0],
                    'price' : item[1],
                    'stock' : item[2],
                    'rating' : item[3],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
