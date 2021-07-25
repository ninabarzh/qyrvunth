""" Google Spider (Not working yet) """

#-----------------------------------------------------
# Parse URL
#-----------------------------------------------------

from urllib.parse import urlparse

netloc = 'www.google.ch'

def has_bad_format(url):
    exts = ['.gif', '.png', '.jpg']
    return any(url.find(ext) >= 0 for ext in exts)

def filter_urls(urls, netloc):
    urls = [url for url in urls if urlparse(url).netloc == netloc]
    urls = [url for url in urls if not has_bad_format(url)]
    return urls

#-----------------------------------------------------
# Spider
#-----------------------------------------------------

import scrapy

class GoogleSpider(scrapy.Spider):
    # This will be used to run the spider
    name = "google"

    # Keep our spider on google's domain
    allowed_domains = [netloc]

    # The crawler will start with those URL's
    start_urls = ['https://' + netloc]

    # The function to handle the server's responses
    def parse(self, response):
        self.logger.info('Processing {}'.format(response.request.url))
        if response.url != response.request.url:
            self.logger.info('\t==> Redirected to {}'.format(response.url))

        # Use CSS selector to extract href urls
        urls = response.css('a::attr(href)').extract()
        urls = filter_urls(urls, netloc)

        # Follow the links
        for url in urls:
            yield response.follow(url, callback=self.parse)
