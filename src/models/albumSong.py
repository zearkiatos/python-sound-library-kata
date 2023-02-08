from sqlalchemy import Column, Integer, ForeignKey
from .declarative_base import Base

class AlbumSong(Base):
   __tablename__ = 'album_song'

   album = Column(Integer, ForeignKey('album.id', primary_key=True))
   song = Column(Integer, ForeignKey('song.id', primary_key=True))