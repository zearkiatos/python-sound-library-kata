from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .declarative_base import Base


class Song(Base):
  __tablename__ = 'song'
  id = Column(Integer, primary_key=True)
  title = Column(String)
  minutes = Column(Integer)
  seconds = Column(Integer)
  composer = Column(String)
  albums = relationship('Album', secondary='album_song')
  interpreters = relationship('Interpreter', cascade="all,delete,delete-orphan")