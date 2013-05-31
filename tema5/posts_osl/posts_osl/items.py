# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class PostsOslItem(Item):

    titulo = Field()
    autor = Field()
    contenido = Field()
    categorias = Field()
    etiquetas = Field()
