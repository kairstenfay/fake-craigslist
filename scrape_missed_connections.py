from bs4 import BeautifulSoup
import requests

url = 'https://seattle.craigslist.org/d/missed-connections/search/mis'
html = requests.get(url).text
print(html)