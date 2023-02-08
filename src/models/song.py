from sqlalchemy import Column, Integer, String
from .declarative_base import Base

class Song(Base):
  __tablename__ = 'song'
  id = Column(Integer, primary_key=True)
  title = Column(String)
  minutes = Column(Integer)
  seconds = Column(Integer)
  composer = Column(String)