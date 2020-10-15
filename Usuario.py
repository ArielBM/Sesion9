
class Usuario:

	def __init__(self, id, usuario, passw):

		self.id = id
		self.usuario = usuario
		self.passw = passw

	def autenticar(self, usuario, passw):

		if self.usuario == usuario and self.passw == passw:

			print("La autenticación fue correcta")
			return True

		print ("La autenticación fue incorrecta")
		return False

	def dump(self):

		return {

			'id' : self.id,
			'nombre' : self.usuario
		}