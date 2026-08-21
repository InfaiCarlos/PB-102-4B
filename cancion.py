from contenido import Contenido

class Cancion(Contenido):

    def __init__(self, titulo, duracion, genero):
        super().__init__(titulo, duracion)
        self.genero = genero

    #Polimorfismo

    def reproducir(self):
        print(f"Reproduciendo la cancion: {self.titulo}")

    def mostrar_informacion(self):
        print("\n ---CANCION---")
        print(f"Titulo: {self.titulo} ")
        print(f"Duracion: {self.duracion} minutos")
        print(f"Genero: {self.genero}")