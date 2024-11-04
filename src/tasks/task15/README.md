## Exercício: Sistema de Gerenciamento de Livros e Biblioteca

**Objetivo:** Criar uma aplicação que gerencia informações de uma biblioteca, incluindo livros, autores e usuários. O sistema deve permitir a adição de novos livros, consulta de livros por autor, e exportação/importação de dados em diferentes formatos (texto, binário, JSON e CSV).

---

Estrutura do Exercício:

1. Classes a serem implementadas:

- **Livro**: Representa um livro, com atributos como título, autor, ano de publicação e gênero.

- **Biblioteca**: Gerencia uma coleção de livros e oferece métodos para manipulação e
consulta dos dados.

---

2. Funcionalidades da Classe Biblioteca:

- **Adicionar livros**: Permitir a adição de novos livros à biblioteca.

- **Listar livros por autor**: Usando filter e lambda, retornar todos os livros de um autor específico.

- **Exportar e importar dados**: Salvar e carregar dados da biblioteca em diferentes formatos de arquivo (texto, JSON, CSV, binário com pickle).

---

3. Relatórios Funcionais:

- Usar *map()* para transformar os dados de livros em uma lista com títulos de todos os livros.

- Usar *reduce()* para contar o número total de livros por um determinado gênero.

---

4. Atividades:

- **Adicionar Novos Livros**: Use a classe Biblioteca para adicionar pelo menos cinco
livros com diferentes autores e gêneros.

- **Consultar Livros por Autor**: Usando listar_livros_por_autor, consulte livros de
um autor específico e verifique se a consulta retorna os livros corretos.

- **Contar Livros por Gênero**: Teste o método contar_livros_por_genero para
verificar se ele retorna o número correto de livros por gênero.

- **Exportar e Importar Dados**: Exporte e importe os dados da biblioteca usando
todos os formatos (texto, JSON, CSV e binário) para se familiarizar com a
manipulação de arquivos em diferentes formatos.

- **Verificar Consistência dos Dados**: Após importar dados de cada arquivo, verifique
se todos os livros foram importados corretamente.

---

5. Filtros

- **Funcionais Avançados**: Adicione um método que filtre livros com base em múltiplos critérios, como ano de publicação e gênero, usando uma combinação de filter e lambda.

- **Adicionar Função de Backu**p: Crie uma função de backup que salve todos os dados da biblioteca em um formato escolhido automaticamente (binário ou JSON).
