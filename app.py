from flask import Flask, request, jsonify
from Usuario import Usuario
from flask_cors import CORS

misUsuario = []
misUsuario.append(Usuario(1,'usuario1','123'))
misUsuario.append(Usuario(2,'usuario2','123'))


app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def login():

	if request.method == 'POST':

		response = {}


		nombre = request.form.get('nombre_usuario')
		passw = request.form.get('passw_usuario')

		for user in misUsuario:

			if user.autenticar(nombre,passw) == True:

				response["id"] =user.id
				response["usuario"] = user.usuario

				return response

		return "False"

	

@app.route("/")
def index():
	nombre = misUsuario[0].usuario
	return "<H1>" + nombre + "</H1>"


if __name__ == "__main__":
	app.run(threaded=True, port=5000,debug=True)