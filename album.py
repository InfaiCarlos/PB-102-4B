class Album:
    def __init__(self, nombre, artista):
        self.nombre = nombre
        self.artista = artista
        self.canciones = []



    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

        print(f"{cancion.titulo} fue agregada "
            f" al album {self.nombre}")

    def mostrar_informacion(self, album):
        print(f"\n---ALBUM: {album.nombre} ---")
        print(f"Artista: {album.artista}")

        if len(album.canciones) == 0:
            print("El album está vacio")
        else:
            for cancion in album.canciones:
                print(f" - {cancion.titulo} "
                    f"({cancion.genero})")

    
        