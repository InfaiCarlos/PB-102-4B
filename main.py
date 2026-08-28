from artista import Artista
from cancion import Cancion
from podcast import Podcast
from contenido import Contenido
from playlist import Playlist
from usuario import Usuario
from album import Album


def main():

    # CREAR CANCIONES

    cancion_nueva = Cancion("Beat it", 4.5, "Pop")
    cancion_dos = Cancion("Bad", 3.8, "Pop") 

    cancion_nueva.mostrar_informacion()

    #Crear ARTISTA

    artista = Artista("Michael Jackson", "Pop")

    artista.agregar_canciones(cancion_nueva)
    artista.agregar_canciones(cancion_dos)

    artista.mostrar_informacion()

    #CREAR PLAYLIST
    new_playlist = Playlist("Favoritos", "Clásicos del POP")
    #new_playlist.mostrar_playlist()
    new_playlist.agregar_cancion(cancion_nueva)
    new_playlist.agregar_cancion(cancion_dos)

    new_playlist.mostrar_playlist()

    #CREAR USUARIO
    usuario_uno = Usuario("Eric", "ea@gmail.com", True)

    usuario_uno.crear_playlist(new_playlist) 

    usuario_uno.mostrar_info()

    #CREAR ALBUM
    album_uno = Album("Thriller", "Michael Jackson")
    album_uno.agregar_cancion(cancion_nueva)
    album_uno.agregar_cancion(cancion_dos)
    album_uno.mostrar_informacion(album_uno)

if __name__ == "__main__":
    main()