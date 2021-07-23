#!/usr/bin/python3

"""Recursively crawl and scrape"""

import requests
from bs4 import BeautifulSoup as Soup, SoupStrainer
from bs4.element import Tag
from bloom_filter2 import BloomFilter
from queue import Queue
from urllib import urljoin

visited = BloomFilter(max_elements=100000, error_rate=0.1)
visitlist = Queue()

def isurlabsolute(url):
    return bool(urlparse(url).netloc)


def visit(url):
    print("Visiting %s" % url)
    visited.add(url)
    return requests.get(url)


def parsehref(response):
    if response.status_code == 200:
        for link in Soup(response.content, 'lxml', parse_only=SoupStrainer('a')):
            if type(link) == Tag and link.has_attr('href'):
                href = link['href']
                if isurlabsolute(href) == False:
                    href = urljoin(response.url, href)
                href = str(href)
                if href not in visited:
                    visitlist.put_nowait(href)
                else:
                    print("Already visited %s" % href)
    else:
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
            print("inexplicable error")

# -----------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------

if __name__ == '__main__':
    visitlist.put_nowait('http://tymyrddin.space/')
    while visitlist.empty() != True:
        url = visitlist.get()
        resp = visit(url)
        parsehref(resp)
        visitlist.task_done()
    visitlist.join()