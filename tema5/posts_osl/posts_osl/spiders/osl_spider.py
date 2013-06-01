from scrapy.spider import BaseSpider

class oslSpider(BaseSpider):

    name = 'osl'
    allowed_domains = ['osl.ugr.es']
    start_urls = ['http://osl.ugr.es/']

    def parse(self, response):
        pass
    

