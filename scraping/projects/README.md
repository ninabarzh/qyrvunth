# Scrapy projects

## Requirements

    $ pip3 install scrapy

## Set up project

    $ scrapy startproject googleScraper
    $ cd googleScraper

## Configuration

For gloves off, edit the `settings.py` file and change the line `ROBOTSTXT_OBEY = True` to `False`.

If the logs are too verbose and difficult to read, that may be because the default `LOG_LEVEL` is set to `DEBUG`. Add `LOG_LEVEL = 'INFO'` in `settings.py`.

To change the user-agent of your spider, add:

    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"

Or pick one from the [database of believable user-agents](http://www.user-agents.org/index.shtml)



