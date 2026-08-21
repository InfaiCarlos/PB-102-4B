from artista import Artista
from cancion import Cancion
from podcast import Podcast
from contenido import Contenido


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




if __name__ == "__main__":
    main()