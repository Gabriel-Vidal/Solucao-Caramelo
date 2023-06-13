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
        tipo = self.ler_string("Digite o tipo do animal: ")
        idade = self.ler_inteiro("Digite a idade aproximada do animal: ")
        cor = self.ler_string("Digite a cor do animal: ")
        porte = self.ler_string("Digite o porte do animal: ")
        particularidade = self.ler_string("Digite a particularidade do animal: ")

        animal = Animal(tipo, idade, cor, porte, particularidade)
        self.animais.append(animal)

    def cadastrar_pessoa(self):
        nome = self.ler_string("Digite o nome da pessoa: ")
        telefone = self.ler_string("Digite o telefone da pessoa: ")
        especie_interesse = self.ler_string("Digite a espécie de interesse para adoção: ")
        preferencias = self.ler_string("Digite as preferências de animal: ")

        pessoa = Pessoa(nome, telefone, especie_interesse, preferencias)
        self.pessoas.append(pessoa)

    @staticmethod
    def ler_inteiro(mensagem):
        while True:
            try:
                valor = int(input(mensagem))
                return valor
            except ValueError:
                print("Valor inválido. Digite um número inteiro.")

    @staticmethod
    def ler_string(mensagem):
        while True:
            valor = input(mensagem)
            if valor:
                return valor
            print("Valor inválido. Digite uma string não vazia.")