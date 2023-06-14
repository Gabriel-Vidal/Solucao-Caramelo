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
            tipo = input("Digite o tipo do animal: ")
            if tipo.isalpha():
                break
            else:
                print("O tipo deve conter apenas letras. Tente novamente.")

        while True:
            cor = input("Digite a cor do animal: ")
            if cor.isalpha():
                break
            else:
                print("A cor deve conter apenas letras. Tente novamente.")

        while True:
            porte = input("Digite o porte do animal: ")
            if porte.isalpha():
                break
            else:
                print("O porte deve conter apenas letras. Tente novamente.")

        while True:
            particularidade = input("Digite a particularidade do animal: ")
            if particularidade.isalpha():
                break
            else:
                print("A particularidade deve conter apenas letras. Tente novamente.")

        idade = input("Digite a idade aproximada do animal: ")

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
        nome = input("Digite o nome da pessoa: ")
        telefone = input("Digite o telefone da pessoa: ")
        especie_interesse = input("Digite a espécie de interesse para adoção: ")
        preferencias = input("Digite as preferências de animal: ")

        pessoa = Pessoa(nome, telefone, especie_interesse, preferencias)
        self.pessoas.append(pessoa)
        print("Pessoa cadastrada com sucesso!")

    def emitir_relatorio(self):
        # Lógica para cruzar os dados e gerar o relatório
        pass

    def buscar_animais(self, caracteristicas):
        # Lógica para buscar animais com base nas características informadas
        pass

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
