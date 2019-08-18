# -*- coding: utf-8 -*-

from sqlalchemy import create_engine

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#Scraped Data -> Item Container -> Pipeline -> PostGres

class LyricsScraperPipeline(object):

    def __init__(self):

        self.create_connection()
        self.create_table()

    def create_connection(self):
        HOST = 'localhost'
        PORT = '5432'
        DATABASE = 'metrolyrics'
        conn_string_mac = f'postgres://{HOST}:{PORT}/{DATABASE}'
        self.conn = create_engine()

    def create_table(self):
        self.conn.execute("""CREATE TABLE IF NOT EXISTS lyrics(
                             song VARCHAR(50),
                             text TEXT
        );
        """)


    def process_item(self, item, spider):
        # print("Pipeline test" + item['song'])

        return item
