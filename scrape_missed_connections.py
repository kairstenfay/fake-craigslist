from bs4 import BeautifulSoup
import requests

url = 'https://seattle.craigslist.org/d/missed-connections/search/mis'
html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.find(id="sortable-results").find_all('li'))
