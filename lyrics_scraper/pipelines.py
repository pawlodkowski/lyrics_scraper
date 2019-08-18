# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker
from lyrics_scraper.models import Lyrics, connect_to_db, create_lyrics_table

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#Scraped Data -> Item Container -> Pipeline -> PostGres

class LyricsScraperPipeline(object):

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates lyrics table.
        """
        engine = connect_to_db()
        create_lyrics_table(engine) #declarative base stuff
        self.Session = sessionmaker(bind=engine)

        # self.create_connection()
        # self.create_table()


    #### OLD BELOW ####

    # def create_connection(self):
    #     HOST = 'localhost'
    #     PORT = '5432'
    #     DATABASE = 'metrolyrics'
    #     conn_string_mac = f'postgres://{HOST}:{PORT}/{DATABASE}'
    #     self.conn = create_engine(conn_string_mac)
    #
    # def create_table(self):
    #     self.conn.execute("""CREATE TABLE IF NOT EXISTS lyrics(
    #                          song VARCHAR(50),
    #                          text TEXT);
    #     """)

    def process_item(self, item, spider):

        """Save lyrics in the database.
        This method is called for every item coming through the pipeline.
        """
        session = self.Session()
        # deal = Deals(**item)
        entry = Lyrics(item['song'], item['text'])

        try:
            session.add(entry)
            session.commit()
            print(f"\n\nInserted {item['song']} into DB!\n\n")
        except:
            session.rollback()
            raise
        finally:
            session.close()

        ###OLD###
        # # print("Pipeline test" + item['song'])
        # self.conn.execute(f"""INSERT INTO lyrics VALUES
        #                   ({item['song']}, {item['text']});
        # """)

        return item
