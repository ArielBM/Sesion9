from Pokemon import Pokemon
import json

class CRUD_Pokemon:

    def __init__(self):
        self.misPokemon = []

    
    #MÉTODO PARA INSERTAR UN POKÉMON
    def insertar(self, id, nombre, tipo1, tipo2, total, hp, ataque, defensa, ataqueEs, defensaEs, velocidad,generacion,legendario, foto):

        self.misPokemon.append(Pokemon(id, nombre, tipo1, tipo2, total, hp, ataque, defensa, ataqueEs, defensaEs, velocidad,generacion,legendario, foto))

    
    #MÉTODO PARA OBTENER UN POKÉMON MEDIANTE SU ID
    def obtener_por_id(self, id):

        for pokemon in self.misPokemon:
            if pokemon.id == id:
                return pokemon.dump()

        return None


    #MÉTODO PARA OBTENER TODOS LOS POKÉMON
    def obtener_todos(self):

        return json.dumps([pokemon.dump() for pokemon in self.misPokemon]) 
