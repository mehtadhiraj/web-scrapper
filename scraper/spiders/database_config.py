import pymysql
import csv
import logs
import pymysql.cursors
from pymysql import OperationalError 
import logging
try:
    
#     logger = logs.logs()
#     logs for the session per day
    #start_date_time= str(datetime.now())
    #log_session = start_date_time.split(' ')
    #log_session = log_session[0]
    #log_session = log_session.replace('-', '')
    ##print(log_session)
    
    #logger = logging.getLogger(__name__)
    #logger.setLevel(logging.INFO)
    
    #formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    
    #file_handler = logging.FileHandler('logs/scraper_'+log_session+'.log')
    #file_handler.setFormatter(formatter)
    
    #logger.addHandler(file_handler)
    
#     Database connection
    connection = pymysql.connect(
       host='localhost',
       user='root',
       password='',                             
       db='scraperdb1',
       port=3306
    )
    connection.autocommit = True
    
    logger.info("Database Connection Established")
    cursor = connection.cursor()
    cursor1  = connection.cursor()
    cursor2  = connection.cursor()
    cursor3  = connection.cursor()
    cursor4  = connection.cursor()

except OperationalError as e:
    #print('Invalid Database Creditentials')
    logger.critical('Invalid Database Creditentials')
    
