# -*- coding: utf-8 -*-

class TagPipeline(object):
    """
        Sólo admite los posts con etiquetas (tags) definidas
    """
    def process_item(self, item, spider):

        if item['etiquetas']:

            # Al menos una etiqueta definida, item correcto
            # Exportación
            print 'Item OK'

        return item

class NoTagPipeline(object):
    """
        Sólo admite los posts sin etiquetas (tags) definidas
    """
    def process_item(self, item, spider):

        if not item['etiquetas']:

            # No hay etiquetas definidas, item correcto
            # Exportación
            print 'No item OK'

        return item
