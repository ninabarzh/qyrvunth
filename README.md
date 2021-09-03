# Qyrvunth

Scraping is not entirely extinct yet. For web applications, this means making a request to a URL and examining what the server returns. One can then parse the returned data to grab the latest news headlines or do some reconnaissance on an organisation or opposing team, snowball the darkweb, mine repositories for identities (and who knows, a password or two), and while scrapy was originally designed for web scraping, it can also be used to extract data using APIs. 

## Requirements

Websites differ, not only the data, also the layout, encodings, and everything changes regularly. What works today may not work tomorrow. There will never be a good-fit-for-all scraper.

* The requests library is a lightweight wrapper over the tedious task of
handling HTTP.
* Beautiful Soup aids in parsing content, and gives options to extract the required
information from XML and HTML structures in a friendly manner. It can not navigate pages automatically and is hard to scale.
* Scrapy is a website scraping framework/library. It is much more
powerful than Beautiful Soup, and it can be scaled. OTOH, more options must be configured.

For simple quick scrapers in the context of pentesting (no need for scaling or parallel execution) a combination of requests and Beautiful Soup can be used because it is lightweight. 

In the context of developing web applications, scrapy is the way to go (and being prepared to handle dynamic content that is rendered with JavaScript). 

* The Python library `builtwith` aims to detect the technologies a website uses.
* Use Chrome DevTools to see where information resides - Disabling JavaScript is necessary see how a scraper sees the website.
* If a website uses JavaScript for rendering, use reverse engineering the AJAX/XHR calls with a tool, or use a tool like Selenium or Portia to render the websites.

## Ode to the Scraper

I'm looking at this scraper

And feel envious

Of its power, its control

When inundated with information

Or unbearably unclear

It can scrape away the overload

No matter how tough the entire payload

It can always be relied upon to clean up the excess

Why isn't life so easy?

When for us the going gets tough, we are forced to look through it

There is no easy scraping our way to a clear image

In final words, Ode to the Scraper!
