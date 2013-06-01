# -*- coding: utf-8 -*-

from scrapy.contrib.exporter import XmlItemExporter

class TagPipeline(object):
    """
        Sólo exporta los posts con etiquetas (tags) definidas
    """

    def spider_opened(self, spider):

        # Crea el fichero para la exportación
        self.file = open('posts_con_tags.xml', 'w+b')

        # Inicializa el exportardor y comienza la exportación
        self.exporter = XmlItemExporter(self.file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
    
        # Termina la exportación
        self.exporter.finish_sporting()

        # Cierra el fichero
        self.file.close()

    def process_item(self, item, spider):

        if item['etiquetas']:

            # Al menos una etiqueta definida, exporta el item
            self.exporter.export_item(item)

        return item

class NoTagPipeline(object):
    """
        Sólo admite los posts sin etiquetas (tags) definidas
    """

    def spider_opened(self, spider):

        # Crea el fichero para la exportación
        self.file = open('posts_sin_tags.xml', 'w+b')

        # Inicializa el exportardor y comienza la exportación
        self.exporter = XmlItemExporter(self.file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
    
        # Termina la exportación
        self.exporter.finish_sporting()

        # Cierra el fichero
        self.file.close()

    def process_item(self, item, spider):

        if not item['etiquetas']:

            # No hay etiquetas definidas, exporta el item
            self.exporter.export_item(item)

        return item
