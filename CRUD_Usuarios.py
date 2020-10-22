from Usuario import Usuario
import json


class CRUD_Usuario:

    # CONSTRUCTOR
    def __init__(self):
        self.usuarios = []
        self.contador = 0

    # MÉTODO PARA CREAR USUARIOS

    def crear(self, nombre, foto, nombre_usuario, contrasenia):

        for usuario in self.usuarios:

            if usuario.nombre_usuario == nombre_usuario:
                # print('el nombre de usuario ya está en uso')
                return False

        self.usuarios.append(
            Usuario(self.contador, nombre, foto, nombre_usuario, contrasenia))
        self.contador += 1
        print("El usuario se creó correctamente")
        return True

    # MÉTODO PARA LISTAR USUARIOS

    def listar(self):

        print('id:\tNombre:\t\tNombre de usuario:')

        for usuario in self.usuarios:

            print(str(usuario.id) + '\t' + usuario.nombre +
                  '\t\t' + usuario.nombre_usuario)

    def devolver_usuarios(self):

        return json.dumps([usuario.dump() for usuario in self.usuarios])


    def autenticar(self, nombre_usuario, pass_usuario):

        for usuario in self.usuarios:

            if usuario.autenticar(nombre_usuario, pass_usuario) == True:
                
                return usuario

        return False
