#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import pandas as pd

import os
import time
import csv
import re

# Function
def exploitsearch():

    # Set the web driver to use Firefox and set the url of the hidden service to be scraped.
    url = "https://example.onion"
    binary = FirefoxBinary("/path/to/firefox/binary")
    driver = webdriver.Firefox(firefox_binary=binary)

    # Open Tor browser and get the url.
    driver.get(url)
    time.sleep(2)

    # Initialise list of URLs to open)
    i = 2
    url_list = []

    # Add the first URL to the list
    url_list.append(url)

    # Iterate in order to create URls
    while i < 21:

        url_to_add = "https://example.onion/route&page=" + str(i) + "rest"
        url_list.append(url_to_add)
        i += 1

    # Print resulting list
    print(url_list)

    # Create dataframe
    listing_frame = pd.DataFrame(columns=["listing"])

    # Iterate over the different webpages created previously
    for webpage in url_list:

        # Open page
        driver.get(webpage)

        # On currently open page, create a list of all the listings
        listings = driver.find_elements_by_xpath("//*[@class = 'cl-list-elements']//*[@class='cldt-summary-full-item-main']")

        # Iterate over the listings in order to find each listing's details
        for listing in listings:

            # Extract the text
            listing_data = listing.text

            # Create a dictionary
            listing_data = {"listing": listing_data}

            # Add dictionary to a dataframe
            frame = pd.DataFrame(listing_data, columns=["listing"], index=[0])

            # Append frame to main dataframe
            listing_frame = listing_frame.append(frame, ignore_index=True)

            # Wait time
            time.sleep(1)

            # Print frame
            print(listing_frame)

    # Print final main frame
    print(listing_frame)

    # Done, quit the Tor browser
    driver.quit()

# Main
exploitsearch()
