from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawllingSpider(CrawlSpider):
    name = 'crawlling'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    rules = [
        Rule(LinkExtractor(allow='catalogue/category')),
    ]
#  callback='parse_item', follow=True)
    # def parse_item(self, response):
    #     self.logger.info('Hi, this is an item page! %s', response.url)
    #     item = scrapy.Item()
    #     item['url'] = response.url
    #     return item