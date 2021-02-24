# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EnglishItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
    img_url = scrapy.Field()

class TeacherItem(scrapy.Item):
    tname = scrapy.Field()
    trank = scrapy.Field()
    tinfo = scrapy.Field()
    timg = scrapy.Field()