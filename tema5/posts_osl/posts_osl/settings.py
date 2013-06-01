# Scrapy settings for posts_osl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'posts_osl'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['posts_osl.spiders']
NEWSPIDER_MODULE = 'posts_osl.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
                    'posts_osl.pipelines.TagPipeline', 
                    'posts_osl.pipelines.NoTagPipeline'
                 ]
