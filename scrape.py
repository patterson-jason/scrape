#Import Beautiful Soup 4 into the program for use as screen scraper
from bs4 import BeautifulSoup
import requests
#Parse the html from the example document then save that as the variable "soup"

url="https://www.realtor.com/apartments/20736"
response=requests.get(url)

soup = BeautifulSoup(response.content,"html.parser")

soup_price=soup.findAll("span",{"data-label":"pc-price"})
soup_sqft=soup.findAll("li",{"data-label":"pc-meta-sqft"})


print(soup_price,soup_sqft)

