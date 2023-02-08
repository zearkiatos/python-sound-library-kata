from src.models.song import Song
from src.models.interpreter import Interpreter
from src.models.album import Album
from src.models.media import Media
from src.declarative_base import Session, engine, Base

if __name__ == '__main__':
    # Create the Database
    Base.metadata.create_all(engine)

    # Open the session
    session = Session()

    # create interpretes
    interpreter1 = Interpreter(
        name="Samuel Torres", curiosities_text="Es colombiano y vive en NY")
    interpreter2 = Interpreter(
        name="Aldo Gavilan", curiosities_text="Cantó a Cuba")
    interpreter3 = Interpreter(name="Buena Vista Social club")
    interpreter4 = Interpreter(
        name="Arturo Sandoval", curiosities_text="No sabía quien era")

    session.add(interpreter1)
    session.add(interpreter2)
    session.add(interpreter3)
    session.add(interpreter4)
    session.commit()

    #create albums
    album1 = Album(title="Latin Jazz Compilation", year=2021,
                   description="Album original", medio=Media.DISK)
    album2 = Album(title="Bandas sonoras famosas", year=2021,
                   description="Compilación", medio=Media.DISK)

    session.add(album1)
    session.add(album2)

       # Crear canciones
    song1 = Song(title = "Ajiaco", minutes = 3, seconds = 1, composer = "Samuel Torres")
    song2 = Song(title = "Forced Displacement", minutes = 3, seconds = 12, composer = "Desconocido")
    song3 = Song(title = "Alegría", minutes = 4, seconds = 27, composer = "AU")
    session.add(song1)
    session.add(song2)
    session.add(song3)

    # Relation albums with song
    album1.songs = [song1, song2]
    album2.songs = [song1, song3]

    song1.albumes=[album1, album2]
    song2.albumes=[album1]
    song3.albumes=[album2]

   # Relation songs with interpreter
    song1.interpreter = [interpreter1]
    song2.interpreter = [interpreter2]
    song3.interpreter = [interpreter3, interpreter4]
    session.commit()

    session.commit()
    session.close()
