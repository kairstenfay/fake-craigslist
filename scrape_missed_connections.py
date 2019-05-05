from bs4 import BeautifulSoup
import requests
import json
import html


def main():
    url = 'https://seattle.craigslist.org/d/missed-connections/search/mis'
    store = []

    for link in get_post_list(url):
        print(f"Attempting to retrieve data from {link}")

        post_doc = requests.get(link).text
        post = BeautifulSoup(post_doc, 'html.parser')
        store.append({
            "id": link[8:len(link) - 5],  # Remove 'https://' and '.html' from URL
            "geo": get_geo(post),
            "title": post.title.string,
            "content": get_content(post)
        })

        # var pID
        # if id="has_been_removed":
        # like with 'https://seattle.craigslist.org/see/mis/d/seattle-what-free-really-feels-like/6879541375.html'
    with open('output.json', 'w') as outfile:
        json.dump(store, outfile, indent=4)


def get_post_list(url: str) -> list:
    """
    Given a URL, return a list of all URLs of the postings
    """
    html_doc = requests.get(url).text
    soup = BeautifulSoup(html_doc, 'html.parser').find(id="sortable-results")  # Jump to postings
    links_with_text = [a['href'] for a in soup.find_all('a', href=True) if a.text]  # Extract post links
    links = list(filter(lambda x: x != '#', links_with_text))  # Remove '#' links
    return links


def get_content(post) -> str:
    """
    Given a BeautifulSoup object *post*, return the body of the message
    """
    content = post.find(id="postingbody")
    if not content:
        print("Could not retrieve data from post")
        return
    content.p.extract()  # Remove <p> tag
    return content.text.strip()


def get_geo(post) -> str:
    """
    Given a BeautifulSoup object *post*, returns the affiliated city
    Mostly are real locations, but some suspicious labels,
    May want to extract from subdomain or lat/long
    """
    geo = post.find_all("meta", {"name" : "geo.placename"})
    if geo:
        # grabs all the (one) meta tags where meta name=geo.placename, then takes the first item of the list
        # THEN grabs the content out of the first item
        geo_content = post.find_all("meta", {"name" : "geo.placename"})[0]['content']  # why does find not work
    else:
        geo_content = None
    return geo_content


if __name__ == "__main__":
    main()
