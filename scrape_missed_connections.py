from bs4 import BeautifulSoup
import requests
import json
import html

url = 'https://seattle.craigslist.org/d/missed-connections/search/mis'
html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, 'html.parser').find(id="sortable-results")  # Jump to postings

links_with_text = [a['href'] for a in soup.find_all('a', href=True) if a.text]  # Extract post links
links = list(filter(lambda x: x != '#', links_with_text))  # Remove '#' links

store = []
for link in links:
    post_doc = requests.get(link).text
    post = BeautifulSoup(post_doc, 'html.parser')
    content = post.find(id="postingbody")
    content.p.extract()  # Remove <p> tag
    stripped_content = content.text.strip()

    store.append({
                "id": link[8:],  # Remove 'https://'
                "title": str(post.title.string),
                "content": stripped_content,
    })
    
    # var pID
    # if id="has_been_removed": 
    # like with 'https://seattle.craigslist.org/see/mis/d/seattle-what-free-really-feels-like/6879541375.html'


    # counter = 0
    # for i in temp.children:
    #     if i.text:
    #         print(str(counter) + ' ' + str(i.text) + '\n')
    #     counter+=1
print(json.dumps(store, indent=4))

