#!/usr/bin/python3

"""
Simple script to fetch all pages of a http site using 
- urllib
- regular expressions
"""

# -----------------------------------------------------------------------
# Fetch a single page
# -----------------------------------------------------------------------

from urllib.request import Request, urlopen
from urllib.error import URLError

def get_html(url):

    # construct http request for the given url 
    req = Request(url,
              data=None, 
              headers={'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'})

    # send request, handle the server's responses, and fetch the html 
    html = None
    try:
        html = urlopen(req)
    except URLError as e:
        if hasattr(e, 'reason'):
            print('Failed to reach server.')
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)

    # On error, simply return an empty binary string
    if html is None:
        print('Server not found')
        html = b''

    # On success, read the html content into a binary string
    else: 
        html  = html.read()

    return html


# -----------------------------------------------------------------------
# Extract the links contained in a webpage using regular expressions
# -----------------------------------------------------------------------

import re

def find_urls(html_binary):

    url_binary_regex = b'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    urls = re.findall(url_binary_regex, html_binary)
    urls = [url.decode('utf-8') for url in urls]
    print(urls)
    return urls


# -----------------------------------------------------------------------
# Filtering:
# Avoid image files to be able to filter using common file extensions
# To remain on the same website, filter urls whose netloc is external
# -----------------------------------------------------------------------

from urllib.parse import urlparse

def has_bad_format(url):
    exts = ['.gif', '.png', '.jpg']
    return any(url.find(ext) >= 0 for ext in exts)

def filter_urls(urls, netloc):
    urls = [url for url in urls if urlparse(url).netloc == netloc]
    urls = [url for url in urls if not has_bad_format(url)]
    return urls


# -----------------------------------------------------------------------
# Iterate and visit the new urls
# -----------------------------------------------------------------------
from bs4 import BeautifulSoup

def something_useful(b_html):

    soup = BeautifulSoup(b_html, 'html.parser')

    # Search for the main div (the div with the most paragraphs)

    ps = soup.select('p')
    parents = [p.parent for p in ps]

    def count_child_paragraphs(element):
        return len(element.findAll('p', recurvise=False))

    parents.sort(key = count_child_paragraphs, reverse=True)
    main_div = parents[0]

    # Add the main title (h1) if it's not already there

    if not main_div.findAll('h1'):
        titles = soup.findAll('h1')
        if titles:
            main_title = titles[0]
            main_div.insert(0, main_title)

    return str(main_div)

def process_html(url, b_html):

    # Do something useful here
    result = something_useful(b_html)

    print('Visiting url : {}'.format(url))
    print(result)


# -----------------------------------------------------------------------
# Main loop
# -----------------------------------------------------------------------

start_url = 'https://tymyrddin.space/portfolio.html'
to_visit = set([start_url])
visited = set()

while to_visit:
    url = to_visit.pop()
    visited.add(url)

    html = get_html(url)
    process_html(url, html)
    
    links = find_urls(html)
    links = filter_urls(links, 'tymyrddin.space')
    links = set(links)
    newlinks = (links - visited) - to_visit
    
    to_visit = to_visit | newlinks