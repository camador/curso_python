# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from posts_osl.items import oslItem

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

        # Items a devolver
        items = []

        # Instancia un selector
        hxs = HtmlXPathSelector(response)

        # Selecciona los posts de la página principal
        posts = hxs.select("//div[@class='entry hentry']")

        # Recorre los posts extrayendo la información
        for post in posts:

            # Item para almacenar los datos
            item = oslItem()
            item['titulo'] = post.select("h2[@class='entry-title']/a/text()").extract()
            item['autor'] = post.select("div[@class='entry-byline']/address[@class='author vcard']/a/text()").extract()
            item['contenido'] = post.select("div[@class='entry-content']/*").extract()
            item['categorias'] = post.select("p[@class='entry-meta']/span[@class='entry-categories']/a/text()").extract()
            item['etiquetas'] = post.select("p[@class='entry-meta']/span[@class='entry-tags']/a/text()").extract()
            items.append(item)

        return items
