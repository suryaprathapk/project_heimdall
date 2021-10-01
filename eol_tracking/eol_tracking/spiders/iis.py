import scrapy


class iis_baseSpider(scrapy.Spider):
    name = "iis_base"
    start_urls = [
        'https://docs.microsoft.com/en-us/lifecycle/products/internet-information-services-iis'
    ]

    def parse(self, response):
        filename = f'iis.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')


class iisSpider(scrapy.Spider):
    name = "iis"
    start_urls = [
        'https://docs.microsoft.com/en-us/lifecycle/products/internet-information-services-iis'
    ]

    # def parse(self, response):
    #     for quote in response.css('table').getall():
    #         yield {
    #             'text': quote.css('span.text::text').get(),
    #             'author': quote.css('small.author::text').get(),
    #             'tags': quote.css('div.tags a.tag::text').getall(),
    #         }
    def parse(self, response):
        for row in response.xpath('//*[@class="table"]//tbody/tr'):
            yield {
                'version': row.xpath('td[1]//text()').extract_first(),
                'start_date': row.xpath('td[2]//text()').extract_first(),
                'end_date': row.xpath('td[3]//text()').extract_first()
            }
