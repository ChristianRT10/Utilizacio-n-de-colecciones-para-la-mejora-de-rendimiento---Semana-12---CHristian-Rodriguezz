from modelos.libros import Libro
from modelos.usuarios import Usuario


class BibliotecaServicio:

    def __init__(self):

        # Diccionario de libros
        self.libros = {}

        # Diccionario de usuarios
        self.usuarios = {}

        # Set para IDs únicos
        self.ids_usuarios = set()

    # Añadir libro
    def agregar_libro(self, libro):

        if libro.get_isbn() in self.libros:
            print("El libro ya existe.")
        else:
            self.libros[libro.get_isbn()] = libro
            print("Libro agregado.")

    # Quitar libro
    def quitar_libro(self, isbn):

        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    # Registrar usuario
    def registrar_usuario(self, usuario):

        if usuario.get_id() in self.ids_usuarios:
            print("Usuario ya registrado.")
        else:
            self.ids_usuarios.add(usuario.get_id())
            self.usuarios[usuario.get_id()] = usuario
            print("Usuario registrado.")

    # Dar de baja usuario
    def eliminar_usuario(self, id_usuario):

        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # Prestar libro
    def prestar_libro(self, id_usuario, isbn):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        if isbn not in self.libros:
            print("Libro no disponible.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros[isbn]

        usuario.prestar_libro(libro)
        del self.libros[isbn]

        print("Libro prestado correctamente.")

    # Devolver libro
    def devolver_libro(self, id_usuario, isbn):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        usuario = self.usuarios[id_usuario]

        for libro in usuario.get_libros_prestados():

            if libro.get_isbn() == isbn:

                usuario.devolver_libro(libro)
                self.libros[isbn] = libro

                print("Libro devuelto.")
                return

        print("El usuario no tiene ese libro.")

    # Buscar por título
    def buscar_titulo(self, titulo):

        for libro in self.libros.values():
            if titulo.lower() in libro.get_titulo().lower():
                print(libro)

    # Buscar por autor
    def buscar_autor(self, autor):

        for libro in self.libros.values():
            if autor.lower() in libro.get_autor().lower():
                print(libro)

    # Buscar por categoría
    def buscar_categoria(self, categoria):

        for libro in self.libros.values():
            if categoria.lower() in libro.get_categoria().lower():
                print(libro)

    # Listar libros de usuario
    def libros_usuario(self, id_usuario):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        usuario = self.usuarios[id_usuario]

        for libro in usuario.get_libros_prestados():
            print(libro)
