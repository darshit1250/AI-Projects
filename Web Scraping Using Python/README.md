# Web Scraping Using Python
  This is the beginner project of Web scraping using Python.
  
# Overview
  PRNewsWire(https://www.prnewswire.com/news-releases/news-releases-list/) has been scrapped to fetch the stock symbols from last 10 days news. 
  In order to fetch the stock symbols RegEx is used. After fetching the stock symbols, finance.yahoo.com is used to fetch the last 10 days prices.
  Generated visulization to show demonstrate the ups and downs.
  
# Liberaries used
  * urllib (https://github.com/node-modules/urllib) - to open the connection to the site.
  * datetime module - to fetch the current date and perform few opertions on it.
  * BeautifulSoap (https://github.com/waylan/beautifulsoup) - to parse the HTML from fetched data.
  * RegEx - to find the pattern of stock symbol (e.g. NASDAQ:AMZN)
  * MatplotLib (https://github.com/matplotlib/matplotlib) - to visulize the closing prices of last 10 days.

# Challenges faced while implementation
  * Used url query parameter to get the last 10 days data. The issue was if there is no news or less news of a particular day it returns previous days' news hence 
    we looked more deep to identify whether the data is of a current date or not.
  * While fetching data from finance.yahoo.com, faced many issues of null data and data in different format.
