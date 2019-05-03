from bs4 import BeautifulSoup
import requests

url = 'https://seattle.craigslist.org/d/missed-connections/search/mis'
html_doc = requests.get(url).text

soup = BeautifulSoup(html_doc, 'html.parser').find(id="sortable-results")  # Jump straight to postings
links_with_text = [a['href'] for a in soup.find_all('a', href=True) if a.text]  # Extract all links to postings
links = list(filter(lambda x: x != '#', links_with_text))  # Remove '#' links
print(links)
