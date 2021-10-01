from os import name
import scrapy


class cognos_baseSpider(scrapy.Spider):
    name = "cognos_base"
    start_urls = [
        'https://www.ibm.com/support/pages/ibm-cognos-analytics-long-term-support-release-lts-1117'
    ]

    def parse(self, response):
        filename = f'cognos.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')


class cognosSpider(scrapy.Spider):
    name = "cognos"
    start_urls = [
        'https://www.ibm.com/support/pages/ibm-cognos-analytics-long-term-support-release-lts-1117'
    ]

    # def parse(self, response):
    #     for quote in response.css('table').getall():
    #         yield {
    #             'text': quote.css('span.text::text').get(),
    #             'author': quote.css('small.author::text').get(),
    #             'tags': quote.css('div.tags a.tag::text').getall(),
    #         }
    def parse(self, response):
        for row in response.xpath('descendant-or-self::table/tbody/tr'):
            yield {
                'version': row.xpath('td[1]//text()').extract_first(),
                'CentOS_6': row.xpath('td[2]//text()').extract_first(),
                'CentOS_Linux_7': row.xpath('td[3]//text()').extract_first(),
                'CentOS_Linux_8': row.xpath('td[4]//text()').extract_first(),
                'CentOS_Stream_8': row.xpath('td[5]//text()').extract_first(),
            }
