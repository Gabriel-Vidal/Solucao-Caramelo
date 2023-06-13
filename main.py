class Animal:
    def __init__(self, tipo, idade, cor, porte, particularidade):
        self.tipo = tipo
        self.idade = idade
        self.cor = cor
        self.porte = porte
        self.particularidade = particularidade


class Pessoa:
    def __init__(self, nome, telefone, especie_interesse, preferencias):
        self.nome = nome
        self.telefone = telefone
        self.especie_interesse = especie_interesse
        self.preferencias = preferencias


class SolucaoCaramelo:
    def __init__(self):
        self.animais = []
        self.pessoas = []