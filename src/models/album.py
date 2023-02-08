from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .declarative_base import Base
from media import Media


class Album(Base):
  __tablename__ = 'album'
  id = Column(Integer, primary_key=True)
  title = Column(String)
  year = Column(Integer)
  description = Column(String)
  media = Column(Media)
  songs = relationship('Song', secondary='album_song')