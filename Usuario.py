# public class Usuario
class Usuario:

    # public Usuario(int id, String nombre, String foto, String nombre_usuario, String contrasenia)
    def __init__(self, id, nombre, foto, nombre_usuario, contrasenia):

        self.id = id
        self.nombre = nombre
        self.foto = foto
        self.nombre_usuario = nombre_usuario
        self.contrasenia = contrasenia

    # public void autenticar(String nombre_usuario, String contrasenia)

    def autenticar(self, nombre_usuario, contrasenia):

        if self.nombre_usuario == nombre_usuario and self.contrasenia == contrasenia:
            return True
        return False

    def modificar_datos(self, nombre, foto, nombre_usuario, contrasenia):

        self.id = id
        self.nombre = nombre
        self.foto = foto
        self.nombre_usuario = nombre_usuario
        self.contrasenia = contrasenia

    def dump(self):

        return {

            'id': self.id,
            'nombre': self.nombre,
            'foto':  self.foto,
            'nombre_usuario': self.nombre_usuario

        }
