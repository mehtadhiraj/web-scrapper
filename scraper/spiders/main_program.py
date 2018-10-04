import subprocess
import scrapy
import pymysql
import pymysql.cursors
import threading
import sys
from datetime import datetime
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
from boto.cloudtrail.exceptions import InvalidTimeRangeException
import scraper
import subprocess
import scrapy
import csv
from twisted.conch.insults.window import cursor
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner
from twisted.conch.test.test_helper import FakeDelayedCall
from _overlapped import NULL
from asn1crypto._ffi import null
from scrapy.http import Request, FormRequest
import browser_cookie3 as cookies
import pickle
import requests
import time
import threading
import sys
from scrapy.utils.log import configure_logging
import os, fnmatch
global response
from datetime import datetime
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
from twisted.internet import reactor
from multiprocessing import Process, Queue
from twisted.internet import reactor
from scraper import BbsSpider
import logging

sys.stdout = open('logs/scrapy_output.log', 'w')

exec(compile(source=open('logger_init.py').read(), filename='logger_init.py', mode='exec'))
 

#DATABASE CONNECTIVITY AS SPECIFIED IN database_config.py
exec(compile(source=open('database_config.py').read(), filename='database_config.py', mode='exec'))


try:
   
    logMsg = "Started scraping session at: "+str(datetime.now())
    print(logMsg)
    
    exec(compile(source=open('logger_init.py').read(), filename='logger_init.py', mode='exec'))
    logger.info(logMsg) 
    # Executing Database config
    exec(compile(source=open('database_config.py').read(), filename='database_config.py', mode='exec'))
    
    process = CrawlerProcess({
        'USER_AGENT': ('Chrome/69.0.3497.81'),
        'TELNETCONSOLE_ENABLED': False,
        'CONCURRENT_REQUESTS':10
    })
      
#     Get date and time of current session
    start_date_time= str(datetime.now())
    end_date_time= str(datetime.now())
     
    scrape_result= 'SCRAPING IN PROGRESS'
    # Query to add session in database
    sql_insert_session = 'INSERT INTO scrape_sessions(session_start_datetime,session_end_datetime, scrape_result, email_status ) values("'+start_date_time+'","'+end_date_time+'", "'+scrape_result+'", 0)'
    print(sql_insert_session)
    ab= cursor.execute(sql_insert_session)
    connection.commit()
    session_id = cursor.lastrowid
    print(session_id)
    logger.info('Session Started')
except TypeError:
    print('Error occured while starting a new seesion')
    logger.exception('Error occured while starting a new seesion')
    
try:
    # Loop1 to get all the storenames 
    sql = 'SELECT store_name, id FROM stores'
    cursor1.execute(sql)
    for store, store_id in cursor1:
        store = store.lower()
        print(store)
        print(store_id)
        logger.info('Scraping for '+store+' started.')
    #     Loop2 to get all the sku id for the given store
        sql = "SELECT item_sku_codes.sku_code, stores.base_url FROM item_sku_codes, stores WHERE stores.store_name = '"+store+"' AND item_sku_codes.store_id = stores.id AND item_sku_codes.is_scrape_active = 1"
        cursor2.execute(sql)
        for sku, base_url in cursor2:
            print(sku)
            print(base_url)
    #         Loop3 to get all the store locations for the given store and sku id
            sql = 'SELECT store_locations.id, city_area, pin_code FROM store_locations,stores WHERE stores.id = store_locations.store_id AND stores.store_name = "'+store+'"'
            cursor3.execute(sql)
            for location_id,area,pincode in cursor3:
                print(location_id)
                print(pincode)
                city= area
                area = area.split('_')
                area = area[0]
                print(area)
                flag = 0
    #             Loop4 to check for the existence of given pincode in a cookies directory
                for root, dirs, files in os.walk('cookies/'):
                    print(root)
                    print(dirs)
                    print(files)
                    if  str(store_id)+'_'+pincode+'.pkl' in files:
                        pass
                    else:
    #                     If given pincodes does not exist genarate a new pickle file
                        scraper.ClearCookies()
                        if store_id == 1:
                            scraper.ChangeLocationAmz(pincode, store, base_url, location_id, store_id, sku)
                        elif store_id == 2:
                            scraper.ChangeLocationGrff(pincode, store, base_url, location_id, store_id, sku, area)
                        elif store_id == 3:
                            scraper.ChangeLocationBbs(pincode, store, base_url, location_id, store_id, sku, area, session_id)
    #             Call to the spiders as per the given store
                if store_id == 2:
                    p= process.crawl(scraper.GrffSpider, base_url = base_url, pincode = pincode, sku = sku, location_id = location_id, store_id = store_id, store = store, city=city, area = area, session_id = session_id)               
                    continue       
                elif store_id == 1:
                    p = process.crawl(scraper.AmzSpider, base_url = base_url, pincode = pincode, sku = sku, location_id = location_id, store_id = store_id, store = store, city=city, area = area, session_id = session_id)
                    continue
                elif store_id == 3:
                    time.sleep(5)
                    p = scraper.BbsSpider.scrape_item_with_variants(base_url, pincode, sku, location_id,city, store_id, store, area, session_id)
                    continue
      
    process.start()
    
    end_time = str(datetime.now())
    sql_update_end_time_and_status = 'UPDATE scrape_sessions SET session_end_datetime = "'+end_time+'", scrape_result = "SUCCESSFUL" where id = "'+str(session_id)+'" '
    cursor.execute(sql_update_end_time_and_status)
    connection.commit()
    logger.info("Scraping session completed successfully.")
    
except Exception as e:
    end_time = str(datetime.now())
    sql_update_end_time_and_status = 'UPDATE scrape_sessions SET session_end_datetime = "'+end_time+'", scrape_result = "FAILED" where id = "'+str(session_id)+'" '
    cursor.execute(sql_update_end_time_and_status)
    connection.commit()
    print(e)
    logger.exception(e)
    logger.Error("Scraping session could not be completed successfully.")
    
finally:
    if ab == 1:
        scrape_result = 'SUCCESSFUL'
        print(scrape_result)
    else:
        scrape_result = 'FAILED'
    
    scraper.mailgeneration(store_id,store,str(session_id))


