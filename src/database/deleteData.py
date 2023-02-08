from src.models.song import Song
from src.models.interpreter import Interpreter
from src.models.album import Album
from src.models.media import Media
from src.declarative_base import Session, engine, Base

if __name__ == '__main__':
    session = Session()
    song2 = session.query(Song).get(2)
    session.delete(song2)
    session.commit()
    session.close()
