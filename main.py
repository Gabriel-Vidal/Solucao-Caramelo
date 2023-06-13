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

    def cadastrar_animal(self):
        tipo = input("Digite o tipo do animal: ")
        idade = input("Digite a idade aproximada do animal: ")
        cor = input("Digite a cor do animal: ")
        porte = input("Digite o porte do animal: ")
        particularidade = input("Digite a particularidade do animal: ")

        animal = Animal(tipo, idade, cor, porte, particularidade)
        self.animais.append(animal)

    def cadastrar_pessoa(self):
        nome = input("Digite o nome da pessoa: ")
        telefone = input("Digite o telefone da pessoa: ")
        especie_interesse = input("Digite a espécie de interesse para adoção: ")
        preferencias = input("Digite as preferências de animal: ")

        pessoa = Pessoa(nome, telefone, especie_interesse, preferencias)
        self.pessoas.append(pessoa)