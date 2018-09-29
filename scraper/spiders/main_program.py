import subprocess
import scrapy
import pymysql
import pymysql.cursors
import threading
import sys
from datetime import datetime


process = CrawlerProcess({
    'USER_AGENT': (
            'Chrome/69.0.3497.81')
})




cursor = connection.cursor()

start_date_time= str(datetime.now())
end_date_time= str(datetime.now())

scrape_result= 'SCRAPING IN PROGRESS'
sql_insert_session = 'INSERT INTO scrape_sessions(session_start_datetime,session_end_datetime, scrape_result ) values("'+start_date_time+'","'+end_date_time+'", "'+scrape_result+'")'
print(sql_insert_session)
ab= cursor.execute(sql_insert_session)
connection.commit()

sql = 'SELECT store_name, id FROM stores'
cursor1.execute(sql)

for store, store_id in cursor1:
    store = store.lower()
    print(store)
    print(store_id)
    sql = "SELECT item_sku_codes.sku_code, stores.base_url FROM item_sku_codes, stores WHERE stores.store_name = '"+store+"' AND item_sku_codes.store_id = stores.id AND item_sku_codes.is_scrape_active = 1"
    print(cursor2.execute(sql))
    for sku, base_url in cursor2:
        print('+++++++++++++++++++++++++++')
        print(sku)
        print('+++++++++++++++++++++++++++')
        print(base_url)
        sql = 'SELECT store_locations.store_id, city_area, pin_code FROM store_locations,stores WHERE stores.id = store_locations.store_id AND stores.store_name = "'+store+'"'
        cursor3.execute(sql)
        for location_id,area,pincode in cursor3:
            print(location_id)
            print(pincode)
            area = area.split('_')
            area = area[0]
            print(area)
            flag = 0
            for root, dirs, files in os.walk('cookies/'):
                print(root)
                print(dirs)
                print(files)
                if  str(store_id)+'_'+pincode+'.pkl' in files:
                    print('=======ddddddddddddd========= '+pincode+' ')
                    pass
                else:
                    ClearCookies()
                    if store_id == 1:
                        ChangeLocationAmz(pincode, store, base_url, location_id, store_id, sku)
                    elif store_id == 2:
                        ChangeLocationGrff(pincode, store, base_url, location_id, store_id, sku, area)

                    elif store_id == 3:
                        flag=ChangeLocationBbs(pincode, store, base_url, location_id, store_id, sku, area)
            if store_id == 2:
                process.crawl(GrffSpider, base_url = base_url, pincode = pincode, sku = sku, location_id = location_id, store_id = store_id, store = store)
                
                
            elif store_id == 1:
                process.crawl(AmzSpider, base_url = base_url, pincode = pincode, sku = sku, location_id = location_id, store_id = store_id, store = store)
                
                
            elif store_id == 3:
                if flag == 0:
                    pass
                else:
                    b=BbsSpider(base_url, pincode, sku, location_id, store_id, store)
                    b.scrape_item_with_varaints(base_url, pincode, sku, location_id, store_id, store)
            continue
                
        
process.start()

