from bs4 import BeautifulSoup
import requests
import json

# url = 'https://seattle.craigslist.org/d/missed-connections/search/mis'
# html_doc = requests.get(url).text
# soup = BeautifulSoup(html_doc, 'html.parser').find(id="sortable-results")  # Jump to postings

# links_with_text = [a['href'] for a in soup.find_all('a', href=True) if a.text]  # Extract post links
# links = list(filter(lambda x: x != '#', links_with_text))  # Remove '#' links

link = 'https://seattle.craigslist.org/skc/mis/d/kent-2-the-female-at-renton-haul/6877187434.html'
store = []
#for link in links:
if link:
    post_doc = requests.get(link).text
    post = BeautifulSoup(post_doc, 'html.parser')
    content = post.find(id="postingbody")
    subtree = content.p
    subtree.extract()

    store.append({
                "id": link[8:],  # Remove 'https://'
                "title": str(post.title.string),
                "content": str(content.text)
    })
    
    # var pID
    # if id="has_been_removed": 
    # like with 'https://seattle.craigslist.org/see/mis/d/seattle-what-free-really-feels-like/6879541375.html'


    # counter = 0
    # for i in temp.children:
    #     if i.text:
    #         print(str(counter) + ' ' + str(i.text) + '\n')
    #     counter+=1
print(json.dumps(store))

