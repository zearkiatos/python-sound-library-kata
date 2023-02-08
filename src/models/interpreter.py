from sqlalchemy import Column, Integer, String, ForeignKey
from .declarative_base import Base

class Interpreter(Base):

  __tablename__ = 'interpreter'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  curiosities_text = Column(String)
  song = Column(Integer, ForeignKey('song.id'))