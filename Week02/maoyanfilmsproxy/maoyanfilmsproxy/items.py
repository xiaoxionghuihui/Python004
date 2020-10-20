# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanfilmsproxyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    filmhref = scrapy.Field()
    #电影名称
    filmname = scrapy.Field()
    #上映时间
    filmtime = scrapy.Field()
    #电影类型
    filmtype = scrapy.Field()
    