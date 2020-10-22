from flask import Flask, request, jsonify
from Usuario import Usuario
from flask_cors import CORS
from CRUD_Pokemon import CRUD_Pokemon
from CRUD_Usuarios import CRUD_Usuario


mis_pokemon = CRUD_Pokemon()
mis_usuarios = CRUD_Usuario()
mis_usuarios.crear('Ariel Bautista Méndez', 'foto.png', 'arielbm', 'mypass')


app = Flask(__name__)
CORS(app)


@app.route('/login', methods=['POST'])
def login():

    if request.method == 'POST':

        response = {}

        nombre = request.form.get('nombre_usuario')
        passw = request.form.get('passw_usuario')

        usuario = mis_usuarios.autenticar(nombre, passw)
        

        if usuario is not False:

            response["id"] = usuario.id
            response["usuario"] = usuario.nombre
            response["estado"] = 1

            return response

        response["estado"] = 0

        return response


@app.route('/obtener-pokemon')
def obtener_pokemon():

    id = int(request.args.get("id", None))
    poke = mis_pokemon.obtener_por_id(id)

    if poke is not None:

        return {
            'estado': 1,
            'id': id,
            'data': poke
        }

    else:

        return {
            'estado': 0,
            'id': id,
            'data': 'Pokémon no encontrado'
        }


@app.route('/obtener-todos-p')
def obtener_todos_p():

    return mis_pokemon.obtener_todos()


def foto_poke(id):

    result = int(id)/100
    if result >= 0.01 and result <= 0.09:
        return 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/00' + str(id) + '.png'

    elif result >= 0.1 and result <= 0.99:
        return 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/0' + str(id) + '.png'

    else:
        return 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/' + str(id) + '.png'


@app.route("/")
def index():
    return "<H1>Bienvenido a mis dominios</H1>"


if __name__ == "__main__":
    app.run(threaded=True, port=5000, debug=True)
