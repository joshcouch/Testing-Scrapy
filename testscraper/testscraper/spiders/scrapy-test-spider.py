import scrapy


class testspider(scrapy.Spider):
    name = 'testspi'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'quote' : quote.css('span.text::text').get(),
                'author' : quote.css('small.author::text').get(),
                'tags' : quote.css('a.tag::text').getall(),
            }
        try:
            next_page = response.css('li.next').css('a').attrib['href']
        except KeyError:
            next_page = None
        if next_page:
            yield response.follow(next_page, callback = self.parse)