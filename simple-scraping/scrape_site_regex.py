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
              headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

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

url_binary_regex = b'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'

def find_urls(html_binary):
    urls = re.findall(url_binary_regex, html_binary)
    urls = [url.decode('utf-8') for url in urls]
    return urls


# -----------------------------------------------------------------------
# Avoid image files to be able to filter using common file extensions
# -----------------------------------------------------------------------

def has_bad_format(url):
    exts = ['.gif', '.png', '.jpg']
    return any(url.find(ext) >= 0 for ext in exts)



# -----------------------------------------------------------------------
# To remain on the same website, filter urls whose netloc is external
# -----------------------------------------------------------------------

from urllib.parse import urlparse

def filter_urls(urls, netloc):
    urls = [url for url in urls if urlparse(url).netloc == netloc]
    urls = [url for url in urls if not has_bad_format(url)]
    return urls


# -----------------------------------------------------------------------
# Iterate and visit the new urls
# -----------------------------------------------------------------------
def process_html(url, b_html):
    # do something useful here 
    print('Visiting url : {}'.format(url))


# -----------------------------------------------------------------------
# Main (example of use)
# -----------------------------------------------------------------------

start_url = 'https://tymyrddin.space/'
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