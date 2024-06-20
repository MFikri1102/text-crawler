import scrapy

class ArticlesSpider(scrapy.Spider):
    name = "articles"
    start_urls = [
        'https://hellosehat.com/'
    ]

    def parse(self, response):
        for article in response.css('div.article-card'):
            yield {
                'title': article.css('h2::text').get(),
                'url': article.css('a::attr(href)').get(),
                'excerpt': article.css('p::text').get()
            }
        
        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

