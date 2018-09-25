from selenium import webdriver
import pymysql
import pymysql.cursors
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',                             
        db='web-scrapper',
    )
print ("Scraping single item with no variants...")

cursor = connection.cursor()
sql = "SELECT id FROM `skus` WHERE website = 'bigbasket'";
# Execute query
cursor.execute(sql)
name = "GroferSpider"
start_urls = []
allowed_domains = ['www.bigbasket.com']  # Domain allowed by this spider
base_url = 'https://www.bigbasket.com/pd/' # Base url for grofers
for url in cursor:
    # Appending a product id
    start_urls.append(base_url+url[0]+'//')
print(start_urls) 


def scrape_single_item():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome('C:/Users/Vivek Iyer/Desktop/web-crawler/web-scrapper/grofer/grofer/spiders/chromedriver.exe')
    driver.get(start_urls[0])
    try:
        element = WebDriverWait(driver, 60).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "sc-bRBYWo"))
        )
        item_desc = driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div")
        print (item_desc.text + " " + element.text)
    except TimeoutException:
        print ("Connection Timeout")
    finally:
        driver.quit()
        
def scrape_item_with_varaints():
    print("Scraping item with variants...")
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(start_urls[0])
    try:
        element = WebDriverWait(driver, 60).until(
            expected_conditions.presence_of_element_located((By.NAME, "size"))
        )
        buttons = driver.find_elements_by_xpath('//*[@name="size"]')
        for ele in buttons:
            name = ele.get_attribute("id")
            lbl = driver.find_element_by_xpath("//*[@for=\""+ name +"\"]")
            lbl.click()
            item = driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div")
            price = driver.find_element_by_class_name("sc-bRBYWo")
            print(item.text + " " + price.text)
    except TimeoutException:
        print ("Connection Timeout")
    finally:
        driver.quit()



scrape_single_item()
scrape_item_with_varaints()
