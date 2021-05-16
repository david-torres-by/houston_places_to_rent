import re
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Chrome driver path for Selenium
#chrome_driver_path = "C:\Development\chromedriver.exe"
#driver = webdriver.Chrome(executable_path= chrome_driver_path)
#driver.get("https://www.zillow.com/homes/for_rent/San-Antonio,-TX_rb/")

# Headers on my request.get
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51",
	"Accept-Language": "en-US,en;q=0.9,es;q=0.8"
}

### Constants ###
number_of_page = 1
# Count of links that it'll retrieve of each page
count = 0
# Count of prices that it'll retrieve of each page
prices_count = 0
web_pages = ["https://www.zillow.com/homes/for_rent/San-Antonio,-TX_rb/"]
# a total of 7 pages
for i in range(1):
	number_of_page += 1
	page = f"https://www.zillow.com/homes/for_rent/San-Antonio,-TX_rb/{number_of_page}_p/"
	web_pages.append(page)

print(web_pages)

# empty list for the prices
house_prices_list = []
test_list = []
link_list = []
price = []

# Making a bot that makes sure that the filter is always on 1000

### For loop to iterate through the web pages ###
for page in web_pages:
	google_form_link = "https://docs.google.com/forms/d/e/1FAIpQLSe1CmIORWNM4PHgbja7ipbUn5kqr_fiU3BVKYaqAS9U9K5Ixw/viewform?usp=sf_link"
	response = requests.get(page, headers = headers)
	houston_houses = response.text

	soup = BeautifulSoup(houston_houses, "html.parser")

	house_price = soup.select('.list-card-heading')

	for price in house_price:
		test_list.append(price.text)

	house_price2 = soup.find_all("div",{"class":"list-card-info"})

	for tag in house_price2:
		image_heading = soup.find_all("div",{"class":"list-card-heading"})
		#for price in image_heading:
			#price_of_houses = soup.find_all("div",{"class":"list-card-price"})
			#price_of_houses2 = soup.select('.list-card-price')




	#for price in house_price:
		#number = ""
		#print(price.text)
		#for char in price.text:
			#if char == "+":
				#break
			#elif char.isdigit():
				#number += char
		#house_prices_list.append(number)
				#house_prices_list.append(price.text)

	house_link = soup.find_all("div",{"class":"list-card-info"})

	#links of each house
	for link in house_link:
		link_tag = link.find_all("a", {"class": "list-card-link list-card-link-top-margin"})
		#print(link_tag)
		for link in link_tag:
			if "https" not in link.get("href"):
				break
			else:
				count += 1
				links = link.get("href")
				link_list.append(links)

	#print(house_link_test.text)
	#for price in house_price:
		#number = price.split('$')[1]
		#print(number)

##### Printing Each price and next to it, the price separated #####
#for i in range(len(test_list)):
	#print(test_list[i], "\t", house_prices_list[i])

#prices in each of the links
print(link_list)
print(f"There is a total of {count} house links")
for link in link_list:
	response2 = requests.get(link, headers = headers)
	price_page = response2.text
	soup2 = BeautifulSoup(price_page, "html.parser")

	house_price2 = soup2.find_all("div",{"hdp__sc-1tsvzbc-1 FNtGJ ds-chip"})
	#house_price2 = soup2.select('.Text-c11n-8-33-0__aiai24-0')
	for price in house_price2:
		prices = price.find_all("span", {"Text-c11n-8-33-0__aiai24-0 sc-pIITJ gXthEq"})
		for price in prices:
			prices_count += 1
			#int_price = ''.join(x for x in price.text if x.isdigit())
			house_prices_list.append(price.text)

print(f"There is a total of {prices_count} prices")

prices_count = 0
iterations = 0
for price in house_prices_list:
	prices_count += 1
	int_price = re.sub('[^0-9,]', "", price).replace(",", "")
	house_prices_list[iterations] = int(int_price)
	iterations += 1

print(f"There is a total of {prices_count} prices")

for i in range(len(link_list)):
	print(link_list[i], "\t", house_prices_list[i])

print("##### MY OWN FILTERS NURUJUJU #####")
my_own_price_list = []
my_own_links_list = []
index_prices_list = []

for price in house_prices_list:
	if price > 1500:
		pass
	else:
		#print(house_prices_list.index(price))
		index_prices_list.append(house_prices_list.index(price))

print(index_prices_list)

for index in index_prices_list:
	my_own_price_list.append(house_prices_list[index])
	my_own_links_list.append(link_list[index])


print("####Rent of houses above $1500 USD JIJIJI####")
for i in range(len(link_list)):
	print(my_own_links_list[i], "\t", my_own_price_list[i])