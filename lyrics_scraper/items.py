# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

#Scraped Data -> temporary container (Item) -> Pipeline -> PostGres

import scrapy


class LyricsScraperItem(scrapy.Item):
    # define the fields for your item here like:
    song = scrapy.Field()
    text = scrapy.Field()
    
