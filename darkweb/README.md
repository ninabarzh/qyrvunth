# Darkweb scraping

## Requirements

Requires the `requests`, `beautifulsoup`, `pandas` and `re` libraries.Pandas is a data manipulation package which can be used to store and export scraped data scraped to `.json` or `.csv` files.

When snowballing the darkweb by scraping one needs a Tor browser or [Whonix workstation VM](https://github.com/tymyrddin/orchard/blob/main/mitigations/virtualisation/kvm/Whonix.md). The Tor browser is based on Firefox.

Selenium is a browser automation package useful for crawling websites and extracting data. For automation, selenium requires a driver. The Tor browser is based on Firefox. 

* Get Mozilla’s Geckodriver and extract it to the `~/.local/bin` folder.
* Get the path to the Tor browser Firefox binary on the local machine. 

## Initialisation

    # Set the web driver to use Firefox and set the url of the hidden service to be scraped.
    binary = FirefoxBinary("/path/to/firefox/binary")
    driver = webdriver.Firefox(firefox_binary = binary)
    url = https://example.onion

    # Open Tor browser and get the url.
    driver.get(url)

## Scraping

Locating HTML elements to collect the data, using class name (right-click it and click inspect):

    driver.find_element_by_class_name("postMain")

Or by using XPath, the location of the element in the HTML structure (right-click menu of the HTML item in the inspect interface). 

    driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[1]/div/a[1]')

To find multiple elements, use “find_elements” instead of “find_element”: 

    driver.find_elements_by_class_name("postMain")

Getting the text of an element using the text function:

    driver.find_element_by_class_name('postContent').text

Storing elements by saving the element in a variable and appending the variable to a list: 

    post_content_list = []
    postText = driver.find_element_by_class_name('postContent').text
    post_content_list.append(postText)

Crawling between pages if page numbers are included in the URL is possible by looping over a range and altering the url:

    for i in range(1, MAX_PAGE_NUM + 1):
        page_num = i
        url = 'first part of url' + str(page_num) + 'last part of url'
        driver.get(url)

## Export

Exporting lists to a `.csv` file as tabular data using Pandas: 

    df['postURL'] = post_url_list
    df['author'] = post_author_list
    df['postTitle'] = post_title_listdf.to_csv('scrape.csv')

Exporting lists to a `.json` file as tabular data using Pandas: 

    df['postURL'] = post_url_list
    df['author'] = post_author_list
    df['postTitle'] = post_title_listdf.to_json('scrape.json')

## Mind the defenses

Many hidden services have anti-crawling measures in place, primarily captchas are used. Auto-solvers exist, but many sites use unique captcha types that the solvers cannot solve. 

Scraping the dark web can be dangerous. Use [applicable infosec](https://github.com/tymyrddin/orchard/tree/main/mitigations/data) to the best of your knowledge and abilities. 
