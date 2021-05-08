from bs4 import BeautifulSoup
import requests

# Headers on my request.get
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51",
	"Accept-Language": "en-US,en;q=0.9,es;q=0.8"
}

### Constants ###
# a total of 7 pages
price_pages = ["https://www.zillow.com/houston-tx/apartments/1-_beds/paymenta_sort/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Houston%2C%20TX%22%2C%22mapBounds%22%3A%7B%22west%22%3A-95.87288353290072%2C%22east%22%3A-95.14229271258822%2C%22south%22%3A29.32700450652518%2C%22north%22%3A30.28267889014576%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A39051%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A307707%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A1000%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22sort%22%3A%7B%22value%22%3A%22paymenta%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22pagination%22%3A%7B%7D%7D"]

# empty list for the prices
house_prices_list = []
test_list = []
tag_html = []

### For loop to iterate through the web pages ###
for page in price_pages:
	google_form_link = "https://docs.google.com/forms/d/e/1FAIpQLSe1CmIORWNM4PHgbja7ipbUn5kqr_fiU3BVKYaqAS9U9K5Ixw/viewform?usp=sf_link"
	response = requests.get(page, headers = headers)
	houston_houses = response.text

	soup = BeautifulSoup(houston_houses, "html.parser")

	house_price = soup.select('.list-card-heading')

	for house in house_price:
		tag_html.append(house)

	for price in house_price:
		test_list.append(price.text)

	for price in house_price:
		number = ""
		print(price.text)
		for char in price.text:
			if char == "+":
				break
			elif char.isdigit():
				number += char
		house_prices_list.append(number)
				#house_prices_list.append(price.text)

	#for price in house_price:
		#number = price.split('$')[1]
		#print(number)
for i in range(len(test_list)):
	print(test_list[i], "\t", house_prices_list[i])
# print(f"The test is this {test_list}")

for i in range(len(tag_html)):
	print(tag_html[i])



#page = "https://www.zillow.com/homes/Houston,-TX_rb/"
#response_1 = requests.get(page, headers = headers)
#houston_houses_1 = response_1.text

#soup_1 = BeautifulSoup(houston_houses_1, "html.parser")

#house_price_1 = soup_1.select('.list-card-price')

#tag_html_1 = []

#for house in house_price_1:
	#price = house.select(".list-card-price")[0].contents[0]
#	tag_html_1.append(house.text)

#print(tag_html_1)