from src.models.song import Song
from src.models.interpreter import Interpreter
from src.declarative_base import Session, engine, Base

if __name__ == '__main__':
  session = Session()
  song = session.query(Song).get(2)
  interpreter = session.query(Interpreter).get(4)

  song.minutes = 5
  song.seconds = 30
  song.composer = "Pedro Pérez"
  song.interpreter.append(interpreter)
  session.add(song)
  session.commit()
  session.close()