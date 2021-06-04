# Snowballing darkweb

## Requirements

When snowballing the darkweb by [scraping](https://github.com/tymyrddin/orchard/blob/main/resources/cheatsheets/Darkweb-scraping.md) one needs a Tor browser or [Whonix workstation VM](https://github.com/tymyrddin/orchard/blob/main/mitigations/virtualisation/kvm/Whonix.md).

Pandas is a data manipulation package which can be used to store and export scraped data scraped to `.json` or `.csv` files.

    $ pip install pandas

Selenium is a browser automation packageuseful for crawling websites and extracting data.

    $ pip install selenium

For automation, selenium requires a driver. The Tor browser is based on Firefox. 

* Get Mozilla’s Geckodriver and extract it to the `~/.local/bin folder`.
* Get the path to the Tor browser Firefox binary on the local machine. 

