# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BossItem(scrapy.Item):
    # define the fields for your item here like:
    salary = scrapy.Field()
    era = scrapy.Field()
    education = scrapy.Field()
    job = scrapy.Field()
    welfares = scrapy.Field()
    year = scrapy.Field()
    descripes = scrapy.Field()
    introductions = scrapy.Field()
