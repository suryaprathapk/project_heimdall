import scrapy
import json

with open('C:\\suryas\\tech_stack_eol_tracking\eol_tracking/oracle.json') as f:
    data = json.load(f)


class oracle_baseSpider1(scrapy.Spider):
    name = "oracle_base_with_search"
    start_urls = [
        data[0]['link']
    ]

    def parse(self, response):
        filename = f'oralce.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')


class oracleSpider1(scrapy.Spider):
    name = "oracle_with_search"
    start_urls = [
        data[0]['link']
    ]

    # def parse(self, response):
    #     for quote in response.css('table').getall():
    #         yield {
    #             'text': quote.css('span.text::text').get(),
    #             'author': quote.css('small.author::text').get(),
    #             'tags': quote.css('div.tags a.tag::text').getall(),
    #         }
    def parse(self, response):
        for row in response.xpath('//*[@class="km"]//tbody/tr'):
            yield {
                'version': row.xpath('td[1]//text()').extract_first(),
                'release_date': row.xpath('td[2]//text()').extract_first(),
                'minimum_support_period': row.xpath('td[3]//text()').extract_first(),
                'end_of_support': row.xpath('td[4]//text()').extract_first(),
                'extended_support': row.xpath('td[5]//text()').extract_first(),
                'sustaining_support': row.xpath('td[6]//text()').extract_first()
            }
