class Usuario:

    def __init__(self, nombre, id_usuario):

        self.__nombre = nombre
        self.__id_usuario = id_usuario

        # Lista de libros prestados
        self.__libros_prestados = []

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_id(self):
        return self.__id_usuario

    def get_libros_prestados(self):
        return self.__libros_prestados

    # Métodos para préstamos
    def prestar_libro(self, libro):
        self.__libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.__libros_prestados:
            self.__libros_prestados.remove(libro)

    def __str__(self):
        return f"Usuario: {self.__nombre} | ID: {self.__id_usuario}"