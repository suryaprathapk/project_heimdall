import scrapy

from scrapy.linkextractors import LinkExtractor

import pandas as pd


class firstSpider(scrapy.Spider):
    name = "basic_search"
    start_urls = [
        "https://www.google.com/search?q=wiki.centos.com+7+eol"
    ]

    def parse(self, response):
        xlink = LinkExtractor()
        for link in xlink.extract_links(response):
            print(link)

    def parse(self, response):
        xlink = LinkExtractor()
        for link in xlink.extract_links(response):
            if len(str(link)) > 200 or 'Cent' in link.text:
                print(len(str(link)), link.text, link, "\n")
