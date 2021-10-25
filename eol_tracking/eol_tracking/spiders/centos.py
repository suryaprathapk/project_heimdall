import scrapy
import json

with open('C:\\suryas\\tech_stack_eol_tracking\\eol_tracking\\google_centos.json') as f:
    data = json.load(f)


class centos_baseSpider1(scrapy.Spider):
    name = "centos_html"
    start_urls = [
        data[0]['link']
    ]

    def parse(self, response):
        filename = f'centos.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')


class centosSpider1(scrapy.Spider):
    name = "centos_json"
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
        for row in response.xpath('descendant-or-self::table/tbody/tr'):
            yield {
                'version': row.xpath('td[1]//text()').extract_first(),
                'CentOS_6': row.xpath('td[2]//text()').extract_first(),
                'CentOS_Linux_7': row.xpath('td[3]//text()').extract_first(),
                'CentOS_Linux_8': row.xpath('td[4]//text()').extract_first(),
                'CentOS_Stream_8': row.xpath('td[5]//text()').extract_first()
            }
