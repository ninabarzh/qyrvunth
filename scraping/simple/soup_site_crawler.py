#!/usr/bin/python3

"""Recursive crawler using soup"""

import requests
from bs4 import BeautifulSoup as Soup, SoupStrainer
from bs4.element import Tag
from bloom_filter2 import BloomFilter
from queue import Queue
from urllib.parse import urlparse, urljoin

start_url = 'https://tymyrddin.space'
netloc = 'tymyrddin.space'
visited = BloomFilter(max_elements=100000, error_rate=0.1)
visitlist = Queue()

# -----------------------------------------------------------------------
# Fetch a response requesting a url
# -----------------------------------------------------------------------

def get_response(url):
    response = requests.get(url)
    if response.status_code == 301:
        print("The server is redirecting to a different endpoint")
    elif response.status_code == 400:
        print("Bad request")
    elif response.status_code == 401:
        print("We are not authenticated")
    elif response.status_code == 403:
        print("Can not access forbidden resources")
    elif response.status_code == 404:
        print("The resource is not available on the server")
    else:
        return response


# -----------------------------------------------------------------------
# Extract the links contained in a page with beautifulsoup
# -----------------------------------------------------------------------

def isurlabsolute(url):
    return bool(urlparse(url).netloc == netloc)


def find_urls(response):
    for link in Soup(response.content, 'lxml', parse_only=SoupStrainer('a')):
        if type(link) == Tag and link.has_attr('href'):
            href = link['href']
            if isurlabsolute(href) == False:
                href = urljoin(response.url, href)
            href = str(href)
            if href not in visited:
                visitlist.put_nowait(href)


# -----------------------------------------------------------------------
# Visit and do something useful (example) 
# -----------------------------------------------------------------------

def something_useful(response):

    soup = Soup(response.content, 'html.parser')

    # Search for the main div (the div with the most paragraphs)

    ps = soup.select('p')
    parents = [p.parent for p in ps]

    def count_child_paragraphs(element):
        return len(element.findAll('p', recursive=False))

    parents.sort(key = count_child_paragraphs, reverse=True)
    main_div = parents[0]

    # Add the main title (h1) if it's not already there

    if not main_div.findAll('h1'):
        titles = soup.findAll('h1')
        if titles:
            main_title = titles[0]
            main_div.insert(0, main_title)

    return str(main_div)
    

def visit(url):
    print("Visiting %s" % url)
    response = get_response(url)

    # Do something useful here
    result = something_useful(response)
    with open('output.html', 'w') as file:
        file.write(result)

    visited.add(url)
    return response


# -----------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------

if __name__ == '__main__':
    visitlist.put_nowait(start_url)
    while visitlist.empty() != True:
        url = visitlist.get()
        response = visit(url)
        find_urls(response)
        visitlist.task_done()
    visitlist.join()