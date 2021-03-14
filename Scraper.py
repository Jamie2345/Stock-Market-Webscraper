# Note this might only work on uk's yahoo finance

# scraping
import requests
from bs4 import BeautifulSoup

# making csv
import pandas as pd

# deleting old csv
import os


class Scrape:
    def _scrape(self, url):
        # making request and finding the class for the current price
        r = requests.get(url)  # make a request to the website
        soup = BeautifulSoup(r.content, 'html.parser')  # used to scape website
        find_price_class = (soup.find('span', {"class": "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}))  # search for the current price of the stock
        find_stock_name = (soup.find('h1', {"class": "D(ib) Fz(18px)"}))  # search for the name of the stock to use as graph title
        return [find_price_class.text, find_stock_name.text]  # return the stock in a list 0 index is price 1 index is stock name

    def add_to_csv(self, urls):
        try:  # if spreadsheet exists delete it (this stops errors when you change the links to stocks)
            os.remove(r"PATH-TO-SPREADSHEET.csv")
        except:
            pass  # do nothing

        if len(urls) > 4:  # stops you from having more than four stock otherwise they wouldn't fit on the screen when you plot graph aswell as the scraping would take too long
            return "You Cannot Have More Than Four Stocks"

        while True:  # loop forever updating the csv
            col = []
            for url in urls:  # scraping each url for stocks price
                scraped_data = self._scrape(url)
                col.append(scraped_data[0])
                col.append(scraped_data[1])

            df = pd.DataFrame(col)
            df = df.T
            df.to_csv(r"PATH-TO-SPREADSHEET.csv", mode='a', header=False)  # adding all prices to a csv


c = Scrape()
c.add_to_csv(["https://uk.finance.yahoo.com/quote/BTC-GBP?p=BTC-GBP"])  # you can have whatever links to stocks you want (up to 4)
