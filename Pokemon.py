class Pokemon:

    def __init__(self, id, nombre, tipo1, tipo2, total, hp, ataque, defensa, ataqueEs, defensaEs, velocidad,generacion,legendario, foto):
        self.id = id
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.total = total
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.ataqueEs = ataqueEs
        self.defensaEs = defensaEs
        self.generacion = generacion
        self.legendario = legendario
        self.foto = foto


    def dump(self):

        return {

            'id': self.id,
            'nombre': self.nombre,
            'tipo1':  self.tipo1,
            'tipo2': self.tipo2,
            'total': self.total,
            'hp':self.hp,
            'ataque':self.ataque,
            'defensa':self.defensa,
            'velocidad':self.velocidad,
            'ataqueEs':self.ataqueEs,
            'defensaEs':self.defensaEs,
            'foto':self.foto

        }
