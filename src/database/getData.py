from src.models.song import Song
from src.models.interpreter import Interpreter
from src.models.album import Album
from src.models.media import Media
from src.declarative_base import Session, engine, Base

if __name__ == '__main__':
    session = Session()
    songs = session.query(Song).all()

    print("The songs storaged are:")
    for song in songs:
        print("Title: "+song.title+" (00:"+str(song.minutes)+":"+str(song.seconds)+")")

        print("Interpreters")
        for interpreter in song.interpreters:
            print(" - "+interpreter.name)
        
        for album in song.albums:
            print(" -- Present in the album: "+album.title)
        
        print("")

    print('The albums storaged are:')
    albums = session.query(Album).filter(Album.media == Media.DISK).all()
    for album in albums:
      print("Album: " + album.title)

    session.close()