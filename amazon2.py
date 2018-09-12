# !/anaconda3/envs/py3/bin python3
# -*- coding: utf-8 -*-
"""
For Scraping Amazon site for product availability.



"""

import pandas as pd
from pandas.core.frame import DataFrame  # only for type specs
from time import sleep
from datetime import date
from random import randint
import pickle
import http.cookies
import requests
from bs4 import BeautifulSoup


def readMaterial() -> DataFrame:
    '''
    Reads SKU codes and Amazon ASIN codes from input file.
    Input csv file must exist, obviously.
    '''
    codes = pd.read_csv("C:/Deep/Amazon/input/Amazon ASIN Code.csv")
    print("Number of material codes: {}".format(codes.shape[0]))

#    Removing duplicate and empty ASIN Codes
    codes.dropna(subset=['Material', 'ASIN'], inplace=True)
    codes.drop_duplicates(subset=['ASIN'], keep='first', inplace=True)
    print("Number of clean ASIN codes: {}".format(codes.shape[0]))

#    Return an indexed dataframe
    return codes.set_index('Material', inplace=False)


def writeStatus(df: DataFrame) -> None:
    '''
    Wite Product Availability to File with current date in output directory.
    Requires output directory as a folder in current directory.
    '''
    writer = pd.ExcelWriter("C:/Deep/Amazon/output/Status " + str(date.today()) + ".xlsx",
                            engine='xlsxwriter')
    df.to_excel(writer, "Amazon", index=False)    
    
#    Some Formatting of the excel sheet
    workbook = writer.book
    worksheet = writer.sheets['Amazon']   
    worksheet.set_column('A:A', 12, workbook.add_format({'align': 'center'}))
    worksheet.set_column('B:B', 35, workbook.add_format({'align': 'left'}))
    worksheet.set_column('C:E', 15, workbook.add_format({'align': 'center'}))
    worksheet.set_column('F:F', 10, workbook.add_format({'align': 'center'}))
    
    # TBD introduce a summary sheet / pivot table
    
    writer.save()


def cleanText(span: str) -> str:
    '''
    Utility function to clean text strings from web scrapes.
    Mostly white space characters, add more as needed.
    '''
    return span.text.strip().strip('\u200c') if span else "N.A."


def getFFCookies() -> None:
    '''
    Utility Function to save a new location.
    
    Make the required new location in Firefox browser before calling this 
    function.Only to be used to capture cookies for a new PINCODE.  We 
    save and reuse these cookies to pass with the http request so that 
    the right PINCODE is active.
    Alternative is to use Selenium webdrivers for browser automation.
    '''
    import browsercookie as cookies
    cookieJar = cookies.firefox()
    azCookieJar = http.cookiejar.CookieJar()
    
    for cookie in cookieJar:
        if 'amazon.in' in cookie.domain:
            azCookieJar.set_cookie(cookie)            
    azCookieDict = requests.utils.dict_from_cookiejar(azCookieJar)
    azCookieDict.pop('session-id-time', None)
    azCookieDict.pop('visitCount', None)
    print(azCookieDict.keys())
    
#    Replace PINCODE below
    with open('C:/Deep/Amazon/input/400001.pkl', 'wb') as fp: pickle.dump(azCookieDict, fp)    


def getChromeCookies() -> None:
    '''
    Utility Function to save a new location.
    
    Change to the required new location in Chrome browser by going to 
    Amazon.in sitebefore calling this function.

    Only to be used to capture cookies for a new PINCODE.  We save and reuse 
    these cookies to pass with the http request for the right PINCODE.

    Alternative is to use Selenium webdrivers for browser automation.
    '''
    import browser_cookie3 as cookies

    cJar = cookies.chrome(domain_name='amazon.in')
    cJar1 = {c.name: c.value for c in cJar}
    del cJar1['session-id-time']
    del cJar1['visitCount']
    print(cJar.keys())
#    Replace PINCODE below
    with open('C:/Deep/Amazon/input/110001.pkl', 'wb') as fp: pickle.dump(cJar, fp)    


def getAmazonStat(codes: DataFrame, location: str) -> tuple:
    '''
    Get current product availability & details from portal.
    '''
    urlBase = "http://www.amazon.in/dp/"
    headers = {'User-Agent': (
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
            '(KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36')}
    fname = "C:/Deep/Amazon/input/" + location + ".pkl"    
    with open(fname, 'rb') as fp: cookieJar = pickle.load(fp)
    
    session = requests.session()
    
    material, titles, ratings, stocks, prices, locs = [], [], [], [], [], []
    for key, row in codes.iterrows():
        url = urlBase + row['ASIN']
#        For debugging:
#        print("Processing: " + url)
        
        r = requests.get(url, headers=headers, cookies=cookieJar)
#        Error checks and retries to be incorporated above as needed
        
        soup = BeautifulSoup(r.content, 'html5lib')

        title = cleanText(soup.find("span", id="productTitle"))
        rating = cleanText(soup.find("span", id="acrPopover")).split(' ')[0]
        availability = cleanText(soup.find("div", id="availability"))
        stock = ('In Stock' in availability)
        price = cleanText(soup.find("span", id="priceblock_ourprice"))
        loc = cleanText(soup.find("span", id="glow-ingress-line2"))

#        For debugging:
#        print('*', end='')
        print(title, rating, price, stock, loc)        

        material.append(key)
        titles.append(title)
        ratings.append(rating)
        stocks.append(stock)
        prices.append(price)
        locs.append(loc)

        sleep(randint(1, 3))
    session.close()    
    return (material, titles, ratings, prices, stocks, locs)


def main() -> None:
    df = readMaterial()
#    For testing, use only say 5 of the codes
    df = df.sample(n=5)

    locations = ['400001'
                 ]

    material, titles, ratings, stocks, prices, locs = [], [], [], [], [], []
    for location in locations:
        code, title, rating, price, stock, loc = getAmazonStat(df, location)
        material += code
        titles += title
        ratings += rating
        prices += price
        stocks += stock
        locs += loc
        print("Location {} completed".format(location))

    writeStatus(pd.DataFrame(
            {'Material': material,
             'Amazon Title': titles,
             'Amazon Rating': ratings,
             'Price at Amazon': prices,
             'Available at site': stocks,
             'Location': locs,
             }))


if __name__ == "__main__":
    main()
   
