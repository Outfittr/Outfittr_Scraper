# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OutfitterScraperItem(scrapy.Item):
    clothing = scrapy.Field()
    image_names = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
