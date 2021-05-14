# importing urllib to open connection to the news wire website and fetching data from the site
import urllib
from urllib.request import urlopen as uReq
# datetime module to work on date
from datetime import datetime, timedelta
# importing timezone package to convert time into particular timezone
from pytz import timezone
# importing BeautifulSoup to parse the HTML we get from newswire website
from bs4 import BeautifulSoup as soup
# importing Regular Expression to fetch the date to varify received data with the date we asked for
import re

# initiating time zone
eastern = timezone('US/Eastern')

# adding headers to avoid 403 forbidden error
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
text_from_page = {}
current_date = datetime.now(eastern)
print(current_date)
# to generate last x days of urls to fetch the data
def getData(days):	
    for day in range(0,days):
        end_date = current_date + timedelta(days=-day) # Subtracting x days.
        end_date_formatted = end_date.strftime('%Y-%m-%d')  # formating the date
        date = str(end_date_formatted).split(' ')[0].split('-') # generating array of 3 elements year, month, and day ["2021","01","01"]
        print("Scrapping data of "+end_date_formatted)
        UClient = uReq(urllib.request.Request('https://www.prnewswire.com/news-releases/news-releases-list/?month='+date[1]+'&day='+date[2]+'&year='+date[0]+'&hour=04&pagesize=100', headers=hdr))
        page = UClient.read()
        UClient.close()
        # parsing the data using HTML parser BeautifulSoup
        page_soup = soup(page, 'html.parser')

        # While browsing the website for particular day it also yields data of previous days, so we are only extracting the data of the current iterating date
        # Find all tags for the same date.
        anchortags = page_soup.findAll("a", class_='newsreleaseconsolidatelink')
        # This regex finds the pattern for current day APR 12, 2021 or 04:00 ET
        date_regex = r"[A-Z]{3}\s*"+date[2]+",\s"+date[0]+"|(^[0-9]{2}:[0-9]{2}\s*[A-Z]{2}$)"
        
        text_from_a = ""
        for a in anchortags:
          s = a.find("small")
          match = re.match(date_regex, s.get_text().upper())
          # consider only data of the current iterating date
          if match:
            text_from_a += a.get_text()
        
        print("Received data of "+end_date_formatted+" !")
        # adding gathered data into data dictionary with the key as a date. {'2021-01-01': Data}
        text_from_page[str(end_date_formatted)] = text_from_a
    return text_from_page
