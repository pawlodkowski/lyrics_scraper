"""Script use for setting up data models in SQL Alchemy
(e.g. connecting to PostGres via ORM), in the spirit of
MVC architecture."""

from sqlalchemy import create_engine, Column, Text, Integer
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()

def connect_to_db():
    """
    Performs database connection to PostGres.
    Returns sqlalchemy engine instance.
    """

    HOST = 'localhost'
    PORT = '5432'
    DATABASE = 'metrolyrics'
    conn_string = f'postgres://{HOST}:{PORT}/{DATABASE}'
    conn = create_engine(conn_string)
    return conn

def create_lyrics_table(engine):
    """Constructing a base class for declarative class definitions (ORM)."""
    DeclarativeBase.metadata.create_all(engine)


class Lyrics(DeclarativeBase):
    """Sqlalchemy lyrics model"""
    __tablename__ = "lyrics" #boilerplate code

    #setting up the table definition
    id = Column(Integer, primary_key=True)
    song = Column('song', Text, nullable=False)
    text = Column('text', Text, nullable=False)

    def __init__(self, song, text):
        """declarative base class must have an __init__"""
        self.song = song
        self.text = text
