# Solução Caramelo

![cachorro](./Imagens/cachorro.jpg)

Este é um programa que permite cadastrar animais e pessoas, emitir relatórios e realizar buscas de animais com base em suas características. A solução é implementada usando a linguagem Python.

 ## Funcionalidades do projeto
 - Cadastrar Animal: O programa permite cadastrar informações sobre animais, como tipo, cor, porte, particularidade e idade aproximada. Ele solicita os dados ao usuário e, em seguida, cria um objeto Animal com essas informações e o adiciona à lista de animais cadastrados.
![animais](./Imagens/Screenshot_1.png)

- Cadastrar Pessoa: O programa permite cadastrar informações sobre pessoas interessadas em adoção de animais. É solicitado o nome da pessoa, a espécie de interesse para adoção, as preferências de animal e o telefone de contato. Em seguida, um objeto Pessoa é criado com essas informações e adicionado à lista de pessoas cadastradas.
![pessoas](./Imagens/pessoa.png)

- Emitir Relatório: O usuário pode escolher emitir diferentes relatórios. Existem três opções:

- Relatório de Animais: Exibe uma lista com informações de todos os animais cadastrados, incluindo tipo, cor, porte, particularidade e idade.
![relatorio_animais](./Imagens/rela_animal.png)
- Relatório de Pessoas: Mostra uma lista com informações de todas as pessoas cadastradas, incluindo nome, telefone, espécie de interesse e preferências de idade de animal.
![relatorio_pessoas](./Imagens/rela_pessoa.png)
- Relatório de Compatibilidade: Gera um relatório mostrando quais animais são compatíveis com as preferências das pessoas cadastradas. Compara a espécie de interesse e as preferências de cor, porte e idade entre os animais e as pessoas, mostrando os resultados.
![compatibilidade](./Imagens/compatibilidade.png)
- Buscar Animais: Permite ao usuário buscar animais com base em características específicas. O usuário pode inserir uma palavra-chave relacionada ao tipo, cor, porte ou particularidade do animal. O programa então busca na lista de animais cadastrados e exibe os resultados correspondentes.