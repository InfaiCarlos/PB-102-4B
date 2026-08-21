from contenido import Contenido

class Podcast(Contenido):

    def __init__(self, titulo, duracion, categoria, num_episodio):
        super().__init__(titulo, duracion)
        self.categoria = categoria
        self.num_episodio = num_episodio

    # POLIMORFISMO

    def reproducir(self):
        print(f" Reproduciendo Podcast {self.titulo} "  
            f" -Episodio: {self.num_episodio}")

    def mostrar_informacion(self):
        print("\n ---PODCAST---")
        print(f"Titulo: {self.titulo} ")
        print(f"Duracion: {self.duracion} minutos")
        print(f"Categoria: {self.categoria}")
        print(f"Episodio: {self.num_episodio}")