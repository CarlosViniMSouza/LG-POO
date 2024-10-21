# Cenário

Você é responsável por desenvolver um sistema para uma biblioteca fictícia. Esse sistema deve ser capaz de:

1. Registrar e armazenar informações sobre livros e autores.
2. Registrar e gerenciar empréstimos de livros para clientes.
3. Calcular a quantidade total de livros na biblioteca e gerenciar o número de livros emprestados.

Além disso, você deve implementar a automação de algumas ações de registro de empréstimo em uma interface web usando BotCity.

Instruções

## Classe Autor:

A classe Autor deve representar o autor de um ou mais livros e incluir os
seguintes atributos:

- nome: Nome do autor (privado).
- livros: Lista de livros escritos pelo autor (privado).

### Métodos:

- adicionar_livro(self, livro): Método para adicionar um livro à lista de livros do autor.
- mostrar_livros(self): Exibe a lista de livros do autor.
- Getters e Setters para nome e livros.

## Classe Livro:

A classe Livro deve representar os livros e incluir os seguintes atributos:

- titulo: Título do livro (privado).
- autor: Autor do livro, representado por uma instância da classe Autor
(composição).
- codigo: Código do livro, usado para identificá-lo na biblioteca.
- disponivel: Variável booleana que indica se o livro está disponível para empréstimo (privado).

### Métodos:

- emprestar(self): Marca o livro como não disponível.
- devolver(self): Marca o livro como disponível.
- Getters e Setters para titulo, codigo e disponivel.

## Classe Biblioteca:

A classe Biblioteca deve representar a biblioteca em si e incluir os seguintes atributos:

- nome: Nome da biblioteca.
- livros: Lista de livros disponíveis na biblioteca (privado).
- emprestimos: Dicionário que associa o código de um livro ao nome do cliente que fez o empréstimo (privado).
- total_livros: Variável de classe que armazena o número total de livros na biblioteca.

### Métodos:

- adicionar_livro(self, livro): Adiciona um livro à lista da biblioteca e incrementa o total_livros.
- registrar_emprestimo(self, codigo_livro, cliente): Registra o empréstimo de um livro, marcando-o como indisponível e adicionando ao dicionário emprestimos.
- registrar_devolucao(self, codigo_livro): Registra a devolução de um livro, marcando-o como disponível e removendo-o de emprestimos.
- mostrar_livros_disponiveis(self): Lista todos os livros que estão disponíveis para empréstimo.
- Método de classe mostrar_total_livros(cls): Exibe o total de livros na
biblioteca.

## Automação com BotCity:

Crie uma automação que usa BotCity para simular a ação de um funcionário
registrando um empréstimo. O BotCity deve preencher os campos "Código
do Livro" e "Nome do Cliente" em um formulário de
empréstimo de uma interface web e submeter o formulário.

**INSTRUÇÕES PARA O ALUNO**

1. Implementar as classes Autor, Livro e Biblioteca, garantindo que os métodos e variáveis encapsulados estejam corretos.
2. Criar instâncias dessas classes para testar o funcionamento do sistema, adicionando autores, livros e gerenciando empréstimos.
3. Automatizar o registro de empréstimos usando o BotCity, preenchendo e
submetendo um formulário online para simular o processo de registro.
4. Entender a diferença entre herança e composição: Use Autor em Livro (composição) e relacione variáveis e métodos entre as classes para explorar esses conceitos.
