import scrapy


class oracle_baseSpider(scrapy.Spider):
    name = "oracle_base"
    start_urls = [
        'https://support.oracle.com/knowledge/Oracle%20Database%20Products/742060_1.html'
    ]

    def parse(self, response):
        filename = f'oracle.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')


class OracleSpider(scrapy.Spider):
    name = "oracle"
    start_urls = [
        'https://support.oracle.com/knowledge/Oracle%20Database%20Products/742060_1.html'
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
