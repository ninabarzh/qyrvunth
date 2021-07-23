#!/usr/bin/python3

"""
Simple script to fetch all pages of a http site using 
- urllib
- beautifulsoup
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
# Use beautifulsoup to parse
# -----------------------------------------------------------------------

from bs4 import BeautifulSoup

# Fetch html from url

url = 'https://tymyrddin.space'
html = get_html(url)
soup = BeautifulSoup(html, 'html.parser')

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

# -----------------------------------------------------------------------
# Write main content to a new file
# -----------------------------------------------------------------------

with open('output.html', 'w') as file:
    file.write(str(main_div))