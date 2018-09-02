from bs4 import BeautifulSoup
import requests

#Sending an http requests. 
#veryfying sertificate = false as there are some missing certificates from grofer during hand shake
res = requests.get('https://grofers.com/',verify = False)
#Getting a source code in an organized format using a beautiful soup
soup = BeautifulSoup(res.text, 'lxml')
#====Finding the required components from the web page
#get the offer details of the product
offer = soup.find('div', {'class': 'plp-product__offer'}).text
#get the product name
productName = soup.find('div', {'class': 'plp-product__name--box'}).text
#get the product quantity
quantity = soup.find('div', {'class': 'plp-product__quantity'}).text
#get the product price
price = soup.find('span', {'class': 'plp-product__price--new'}).text
#creating a dictioanery of the details
product = {
    'name' : productName,
    'offer' : offer,
    'quantity' : quantity,
    'price' : price
    }
#Printitng all  the product details
print('====================================\nDetails of product are as follows\n====================================')
print('Name        : '+product['name'])
print('Offer       : '+product['offer'])
print('Quantity    : '+product['quantity'])
print('Price       : '+product['price']+'Rs.')