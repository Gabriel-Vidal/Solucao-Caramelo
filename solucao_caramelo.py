from animal import Animal
from pessoa import Pessoa


class SolucaoCaramelo:
    def __init__(self):
        self.animais = []
        self.pessoas = []

    def cadastrar_animal(self):
        while True:
            tipo = input("Digite o tipo do animal (Cachorro, Gato, etc...): ").lower()
            if tipo.strip() == '':
                print("O tipo não pode ser vazio. Tente novamente.")
            elif all(caractere.isalpha() or caractere.isspace() for caractere in tipo):
                break
            else:
                print("O tipo deve conter apenas letras. Tente novamente.")

        while True:
            cor = input("Digite a cor do animal: ").lower()
            if cor.strip() == '':
                print("A cor não pode ser vazia. Tente novamente.")
            elif all(caractere.isalpha() or caractere.isspace() for caractere in cor):
                break
            else:
                print("A cor deve conter apenas letras. Tente novamente.")

        while True:
            porte = input("Digite o porte do animal (Grande, Médio ou Pequeno): ").lower()
            if porte.isalpha() and porte in ['grande', 'medio', 'pequeno']:
                break
            else:
                print("Porte do animal inválido. Tente novamente.")

        while True:
            particularidade = str(input("Digite a particularidade do animal: ")).lower()
            if particularidade.strip() == '':
                print("a particularidade do animal não pode ser vazia. Tente novamente.")
            else:
                break

        idade = str(input("Digite a idade aproximada do animal: "))

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
            if all(caractere.isalpha() or caractere.isspace() for caractere in nome):
                break
            else:
                print("Nome inválido, por favor insira o nome da pessoa, corretamente!")

        while True:
            especie_interesse = input("Digite a espécie de interesse para adoção: ").lower()
            if all(caractere.isalpha() or caractere.isspace() for caractere in especie_interesse):
                break
            else:
                print("Digite o nome da espécie corretamente!")


        preferencias = str(input("Digite sua preferência do animal: "))

        while True:
            telefone = input("Digite o telefone da pessoa: Ex:(DDDXXXXXXXXX): ")
            if telefone.isalnum() and len(telefone) == 11:
                break
            else:
                print("Digite um telefone válido com 11 números incluindo o DDD, conforme o exemplo!")

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

    def emitir_relatorio(self):
        print("Escolha o relatório:")
        print("1 - Relatório de animais")
        print("2 - Relatório de pessoas")
        print("3 - Relatório de compatibilidade")
        relatorio_opcao = input("Digite o número do relatório desejado: ")

        if relatorio_opcao == "1":
            self.relatorio_animais()
        elif relatorio_opcao == "2":
            self.relatorio_pessoas()
        elif relatorio_opcao == "3":
            self.relatorio_compatibilidade()
        else:
            print("Opção inválida. Por favor, tente novamente.")

    def relatorio_animais(self):
        if self.animais:
            print("----- Relatório de animais -----")
            for animal in self.animais:
                print(f"Tipo: {animal.tipo}\n"
                      f"Cor: {animal.cor}\n"
                      f"Porte: {animal.porte}\n"
                      f"Particularidade: {animal.particularidade}\n"
                      f"Idade: {animal.idade}")
                print("-=-"*30)
        else:
            print("Não há animais cadastrados.")

    def relatorio_pessoas(self):
        if self.pessoas:
            print("----- Relatório de pessoas -----")
            for pessoa in self.pessoas:
                print(f"Nome: {pessoa.nome}\n"
                      f"Telefone: {pessoa.telefone}\n"
                      f"Espécie de Interesse: {pessoa.especie_interesse}\n"
                      f"Preferência de idade do animal: {pessoa.preferencias}")
                print("-=-"*30)
        else:
            print("Não há pessoas cadastradas.")

    def buscar_animais(self, caracteristicas):
        resultados = []
        for animal in self.animais:
            if caracteristicas.lower() in animal.tipo.lower() or caracteristicas.lower() in animal.cor.lower() or \
                    caracteristicas.lower() in animal.porte.lower() or caracteristicas.lower() in animal.particularidade.lower():
                resultados.append(animal)

        if resultados:
            print("----- Resultados da busca -----")
            for animal in resultados:
                print(f"Tipo: {animal.tipo} | Cor: {animal.cor} | Porte: {animal.porte} | "
                      f"Particularidade: {animal.particularidade} | Idade: {animal.idade}")
        else:
            print("Nenhum animal encontrado com as características fornecidas.")

    def relatorio_compatibilidade(self):
        if self.pessoas and self.animais:
            self.selecionar_animais_compativeis()
        else:
            print("Não há pessoas ou animais cadastrados suficientes para gerar o relatório de compatibilidade.")

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
