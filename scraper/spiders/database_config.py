import pymysql
import csv
import pymysql.cursors
from pymysql import OperationalError 

try:
#     Database connection
    connection = pymysql.connect(
       host='localhost',
       user='root',
       password='',                             
       db='scraperdb1',
    )
    print ("Database Connection Established") 
    
    cursor = connection.cursor()
    cursor1  = connection.cursor()
    cursor2  = connection.cursor()
    cursor3  = connection.cursor()
    cursor4  = connection.cursor()

except OperationalError as e:
    print('Invalid Database Creditentials')

    
