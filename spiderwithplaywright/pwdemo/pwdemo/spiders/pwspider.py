import scrapy


class PwspiderSpider(scrapy.Spider):
    name = 'pwspider'

    def start_requests(self):
        yield scrapy.Request('http://quotes.toscrape.com/', meta = {'playwright' : True}) ## https://shoppable-campaign-demo.netlify.app/#/


    def parse(self, response):
        yield {
            'text' : response.text
        }
