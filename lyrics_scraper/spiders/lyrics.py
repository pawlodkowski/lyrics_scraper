# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import re
from ..items import LyricsScraperItem


class LyricsSpider(scrapy.Spider):
    name = 'lyrics'
    allowed_domains = ['www.metrolyrics.com']
    start_urls = ['http://www.metrolyrics.com/top-artists.html/']

    def clean(self, lyricstext):

        lyricstext = ' '.join(lyricstext)
        lyricstext = re.sub('\n|\r|\t|\\|\,|\'|\"|\,|\*', '', lyricstext)
        lyricstext = re.sub('\-|\:|\)|\(|\[|\]|\{|\}', ' ', lyricstext)
        lyricstext = re.sub('\s+', " ", lyricstext)
        return lyricstext

    def parse(self, response):

        item = LyricsScraperItem() #container defined in items.py

        artists = response.xpath('//a[@class="image"]/@href').getall()
        #all artist links on homepage

        for a in artists:
            yield Request(a)

        songs = response.xpath('//td/a/@href').getall()
        for s in songs:
            yield Request(s)

        title = response.xpath('//div[@class="banner-heading"]/h1/text()').get()
        # text = response.xpath('//div[@id="lyrics-body-text"]//text()').getall()
        text = response.xpath('//div[@class="lyrics-body"]//p[@class="verse"]/text()').getall()
        text = self.clean(text)

        item['song'] = title
        item['text'] = text

        #check if any are empty
        if title and text:
            # print(item)
            yield item
        else:
            pass
