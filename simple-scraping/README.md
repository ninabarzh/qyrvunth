# Scraping scripts

These scripts are just for fun and educational purposes. Mature crawling software like Scrapy, Nutch or Heritrix do a way better job.

## Requirements

### Requests

The `requests` library simplifies the process of making http requests: The `GET` request can be used to retrieve information from a web server (download the HTML content of a specified web page) and makes it very easy to use proxies that require authentication. The `POST` request can be used to post form data. And he requests library 

    $ pip3 install requests

### Urllib

As an alternative for simple projects, `urllib` can be used, a package that collects several modules for working with URLs. 

* urllib.request for opening and reading URLs https://docs.python.org/3.8/library/urllib.request.html
* urllib.error containing the exceptions raised by urllib.request https://docs.python.org/3.8/library/urllib.error.html
* urllib.parse for parsing URLs https://docs.python.org/3.8/library/urllib.parse.html
* urllib.robotparser for parsing robots.txt files https://docs.python.org/3.8/library/urllib.robotparser

It offers a slightly more complex interface for handling common situations - like basic authentication, cookies, proxies and so on.

### Beautifulsoup

`beautifulsoup` is a Python library that can extract (parse) HTML data and can turn even invalid markup into a parse tree.

    $ pip3 install beautifulsoup4

### Pandas

`pandas` is a data manipulation package which can be used to store and export scraped data to `.json` or `.csv` files.

    $ pip3 install pandas

### Selenium

`selenium` is an open-source browser tool (web driver) that allows for automating processes such as logging into a social media platform. It can execute test cases or test scripts on web applications and render web pages by running JavaScript.

    $ pip3 install selenium

For automation, selenium requires a driver. For firefox, get Mozilla’s Geckodriver and extract it to the `~/.local/bin` folder. Then get the path to the Firefox binary on the local machine.

    $ which firefox

or

    $ whereis firefox

### Bloomfilter

Especially recursive crawling can get out of hand fast. With bloomfilter the desired maximum number of elements and maximum false positive probability can be set https://pypi.org/project/bloom-filter2/

### Darkweb

* When [snowballing the darkweb]snowballing-darkweb.py) one needs a Tor browser or [Whonix workstation VM](https://github.com/tymyrddin/orchard/blob/main/mitigations/virtualisation/kvm/Whonix.md). The Tor browser is based on Firefox.
 
