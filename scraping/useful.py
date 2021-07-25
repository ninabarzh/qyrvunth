#!/usr/bin/python3

"""
Something useful:
    Use beautifulsoup to parse the main div of a page
"""

# -----------------------------------------------------------------------
# Fetch a single page
# -----------------------------------------------------------------------


# -----------------------------------------------------------------------
# Some useful things
# -----------------------------------------------------------------------

from bs4 import BeautifulSoup

def maindiv(url, b_html):

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