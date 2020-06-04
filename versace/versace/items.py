# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VersaceItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    product_currency = scrapy.Field()
    product_category = scrapy.Field()
    product_colour = scrapy.Field()
    product_size = scrapy.Field()
    product_description = scrapy.Field()
    product_region = scrapy.Field()
    product_link = scrapy.Field()
    product_time = scrapy.Field()

    pass
