class Animal:
    def __init__(self, tipo, nome, idade, cor, porte, especie, particularidade):
        self.tipo = tipo
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.porte = porte
        self.particularidade = particularidade

    def __str__(self):
        return f"Animal: {self.nome}, Idade: {self.idade}, Cor: {self.cor}, Especie: {self.especie}, Particularidade: {self.particularidade}"

class Pessoa:
    def __init__(self, nome, telefone, email, endereco, especie, preferencia):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.especie = especie
        self.preferencia = preferencia

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}, Endereço: {self.endereco}, Especie: {self.especie}, Preferência: {self.preferencia}"


class Cadrasto_geral:
    def __init__(self):
        self.animais = []
        self.pessoas = []

    def cadrastar_animal(self, animal):
        self.animais.append(animal)
    
    def cadastrar_pessoa(self, pessoa):
        self.pessoas.append(pessoa)

    def exibir(self):
        for animal in self.animais:
            print(animal)

        for pessoa in self.pessoas:
            print(pessoa)


animal1 = Animal('Cachorro','Rex', 5, "caramelo", 'medio', 'nenhuma')
pessoa1 = Pessoa('Gabriel', 21991820417, 'sla@gmail.com', 'avenida', 'ND', 'nenhuma')

cadastro = Cadrasto_geral()

cadastro.cadrastar_animal(animal1)
cadastro.cadastrar_pessoa(pessoa1)

cadastro.exibir()

