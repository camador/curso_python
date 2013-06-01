# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class oslSpider(BaseSpider):

    name = 'osl'
    allowed_domains = ['osl.ugr.es']
    start_urls = ['http://osl.ugr.es/']

    def parse(self, response):

        #
        # Selectores:
        #
        # Posts: "//div[@class='entry hentry']"
        # Título:  "//div[@class='entry hentry']/h2[@class='entry-title']/a/text()'"
        # Autor: "//div[@class='entry hentry']/div[@class='entry-byline']/address[@class='author vcard']/a/text()"
        # Contenido: "//div[@class='entry hentry']/div[@class='entry-content']/*"
        # Categorías: "//div[@class='entry hentry']/p[@class='entry-meta']/span[@class='entry-categories']/a/text()"
        # Etiquetas: "//div[@class='entry hentry']/p[@class='entry-meta']/span[@class='entry-tags']/a/text()"

        # Instancia un selector
        hxs = HtmlXPathSelector(response)

        # Selecciona los posts de la página principal
        posts = hxs.select("//div[@class='entry hentry']")

        # Recorre los posts extrayendo la información
        for post in posts:
            print '--------------------'
            print u'Título: ', post.select("h2[@class='entry-title']/a/text()").extract()[0]
            print u'Autor: ', post.select("div[@class='entry-byline']/address[@class='author vcard']/a/text()").extract()[0]
            print u'Contenido: ', '\n'.join(post.select("div[@class='entry-content']/*").extract())
            print u'Categorías: ', ', '.join(post.select("p[@class='entry-meta']/span[@class='entry-categories']/a/text()").extract())
            print u'Tags: ', ', '.join(post.select("p[@class='entry-meta']/span[@class='entry-tags']/a/text()").extract())

        print '--------------------'
