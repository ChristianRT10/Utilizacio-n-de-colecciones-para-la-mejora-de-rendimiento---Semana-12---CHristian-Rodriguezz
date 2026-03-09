from modelos.libros import Libro
from modelos.usuarios import Usuario
from servicios.biblioteca_servicio import BibliotecaServicio


def menu():

    biblioteca = BibliotecaServicio()

    while True:

        print("\n--- BIBLIOTECA DIGITAL ---")
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Eliminar usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro por título")
        print("8. Buscar libro por autor")
        print("9. Buscar por categoría")
        print("10. Ver libros de usuario")
        print("11. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")

            libro = Libro(titulo, autor, categoria, isbn)

            biblioteca.agregar_libro(libro)

        elif opcion == "2":

            isbn = input("ISBN del libro: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":

            nombre = input("Nombre: ")
            id_usuario = input("ID Usuario: ")

            usuario = Usuario(nombre, id_usuario)

            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":

            id_usuario = input("ID Usuario: ")
            biblioteca.eliminar_usuario(id_usuario)

        elif opcion == "5":

            id_usuario = input("ID Usuario: ")
            isbn = input("ISBN del libro: ")

            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "6":

            id_usuario = input("ID Usuario: ")
            isbn = input("ISBN del libro: ")

            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "7":

            titulo = input("Título: ")
            biblioteca.buscar_titulo(titulo)

        elif opcion == "8":

            autor = input("Autor: ")
            biblioteca.buscar_autor(autor)

        elif opcion == "9":

            categoria = input("Categoría: ")
            biblioteca.buscar_categoria(categoria)

        elif opcion == "10":

            id_usuario = input("ID Usuario: ")
            biblioteca.libros_usuario(id_usuario)

        elif opcion == "11":

            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()