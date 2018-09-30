import pymysql
import csv
import logs
import pymysql.cursors
from pymysql import OperationalError 

try:
    
    logger = logs.logs()
#     Database connection
    connection = pymysql.connect(
       host='localhost',
       user='root',
       password='123',                             
       db='scraperdb1',
    )
    print ("Database Connection Established") 
    logger.info("Database Connection Established")
    cursor = connection.cursor()
    cursor1  = connection.cursor()
    cursor2  = connection.cursor()
    cursor3  = connection.cursor()
    cursor4  = connection.cursor()

except OperationalError as e:
    print('Invalid Database Creditentials')
    logger.critical('Invalid Database Creditentials')
    
