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
        while True:
            tipo = input("Digite o tipo do animal (Cachorro, Gato, etc...: ").lower()
            if tipo.isalpha():
                break
            else:
                print("O tipo deve conter apenas letras. Tente novamente.")

        while True:
            cor = input("Digite a cor do animal: ").lower()
            if cor.isalpha():
                break
            else:
                print("A cor deve conter apenas letras. Tente novamente.")

        while True:
            porte = input("Digite o porte do animal: ").lower()
            if porte.isalpha():
                break
            else:
                print("O porte deve conter apenas letras. Tente novamente.")

        while True:
            particularidade = input("Digite a particularidade do animal: ").lower()
            if particularidade.isalpha():
                break
            else:
                print("A particularidade deve conter apenas letras. Tente novamente.")

        idade = self.ler_inteiro("Digite a idade aproximada do animal: ")

        animal = Animal(tipo, idade, cor, porte, particularidade)

        while True:
            confirmacao = input("Os dados inseridos estão corretos? (S/N): ")
            if confirmacao.upper() == "S":
                self.animais.append(animal)
                print("Animal cadastrado com sucesso!")
                break
            elif confirmacao.upper() == "N":
                print("Por favor, insira novamente os dados do animal:")
                return self.cadastrar_animal()
            else:
                print("Opção inválida. Digite 'S' para confirmar ou 'N' para rejeitar.")

    def cadastrar_pessoa(self):
        while True:
            nome = input("Digite o nome da pessoa: ").lower()
            if nome.isalpha():
                break
            else:
                print("Nome inválido, por favor insira o nome da pessoa, corretamente!")

        while True:
            especie_interesse = input("Digite a espécie de interesse para adoção: ").lower()
            if especie_interesse.isalpha():
                break
            else:
                print("Digite o nome da espécie corretamente!")

        while True:
            preferencias = input("Digite as preferências de animal: ").lower()
            if preferencias.isalpha():
                break
            else:
                print("Digite a preferências pelo animal corretamente!")

        while True:
            telefone = input("Digite o telefone da pessoa: Ex:(DDDXXXXXXXXX): ")
            if telefone.isalnum() and len(telefone) == 11:
                break
            else:
                print("Digite um telefone válido com 11 números incluido DDD, conforme o exemplo!")

        pessoa = Pessoa(nome, telefone, especie_interesse, preferencias)

        while True:
            confirmacao = input("Os dados inseridos estão corretos? (S/N): ")
            if confirmacao.upper() == "S":
                self.pessoas.append(pessoa)
                print("Pessoa cadastrada com sucesso!")
                break
            elif confirmacao.upper() == "N":
                print("Por favor, insira novamente os dados da pessoa:")
                return self.cadastrar_pessoa()
            else:
                print("Opção inválida. Digite 'S' para confirmar ou 'N' para rejeitar.")

    @staticmethod
    def ler_inteiro(mensagem):
        while True:
            try:
                valor = int(input(mensagem))
                return valor
            except ValueError:
                print("Valor inválido. Digite um número inteiro.")


    def exibir_menu(self):
        print("----- Solução Caramelo -----")
        print("1 - Cadastrar animal")
        print("2 - Cadastrar pessoa")
        print("3 - Emitir relatório")
        print("4 - Buscar animais")
        print("0 - Sair")

    def executar_opcao(self, opcao):
        if opcao == "1":
            self.cadastrar_animal()
        elif opcao == "2":
            self.cadastrar_pessoa()
        elif opcao == "3":
            self.emitir_relatorio()
        elif opcao == "4":
            caracteristicas = input("Digite as características para busca: ")
            self.buscar_animais(caracteristicas)
        elif opcao == "0":
            return False
        else:
            print("Opção inválida. Por favor, tente novamente.")

        return True

    def executar(self):
        executando = True

        while executando:
            self.exibir_menu()
            opcao = input("Digite a opção desejada: ")
            executando = self.executar_opcao(opcao)

# Instanciar e executar o sistema
sistema = SolucaoCaramelo()
sistema.executar()
