from flask import Flask, request, jsonify
from Usuario import Usuario
from flask_cors import CORS
from CRUD_Pokemon import CRUD_Pokemon

misUsuario = []
misUsuario.append(Usuario(1,'usuario1','123'))
misUsuario.append(Usuario(2,'usuario2','123'))

mis_pokemon = CRUD_Pokemon()


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
				response["estado"] = 1

				return response

		response["estado"] = 0

		return response


@app.route('/pokemon', methods=['GET','POST'])
def pokemon():

	response = {}

	if request.method == 'POST':

		nombre_p = request.form.get('nombre_poke')
		especie_p = request.form.get('especie_poke')
		tipo_p = request.form.get('tipo_poke')
		foto_p = request.form.get('foto_poke')

		if mis_pokemon.crear(nombre_p,especie_p,tipo_p,foto_p) == True:

			response['estado'] = 1
			return response

		response['estado'] = 0
		return response

	if request.method == 'GET':

		return  mis_pokemon.devolver_pokemon()


@app.route("/single_poke",methods=['GET'])
def single_poke():

	if request.method == 'GET':

		nombre = request.args.get("nombre", None)
		response = {}

		poke = mis_pokemon.buscar(nombre)

		if poke == None:

			response['estado'] = 0

		else:

			response['estado'] = 1
			response['pokemon'] = poke

		return response


@app.route("/")
def index():
	nombre = misUsuario[0].usuario
	return "<H1>" + nombre + "</H1>"


if __name__ == "__main__":
	app.run(threaded=True, port=5000,debug=True)