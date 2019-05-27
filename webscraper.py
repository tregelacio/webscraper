import requests
import urllib
import time
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://stockx.com/nike-ld-waffle-sacai-blue-multi'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print ('before find')

print soup.findAll('h3', limit=6)

print ('found all')

driver = webdriver.Chrome()
driver.get(url)

time.sleep(15)

elem = driver.find_element_by_class_name('form_group')


#button = driver.find_element_by_class_name('form-group')
#button.click()

''' This prints out the info on the starting page. No info of other sizes
sale = soup.select('.last-sale-block')

for sale in soup.select('.last-sale-block'):

	print sale.text

ask = soup.select('.bid')

for ask in soup.select('.bid'):

	print ask.text

bid = soup.select('.ask')

for bid in soup.select('.ask'):

	print bid.text
'''
# print soup