## Exercício Integrado de Orientação a Objetos, Programação Funcional, RPA com BotCity, Arquivos Binários e Tratamento de Exceções

**Objetivo do Exercício:**

Criar uma aplicação Python orientada a objetos para gerenciar pedidos de uma loja virtual fictícia. Aplicar conceitos de programação funcional e RPA com BotCity, além de manipulação de arquivos em diferentes formatos (JSON e binário com pickle) e tratamento de exceções. A aplicação terá funcionalidades de cadastro, manipulação de pedidos e automatização de tarefas.

**Especificações do Exercício:**

*Estrutura de Classes:* A equipe deve criar uma estrutura de classes para representar Produto, Pedido e GestorDePedidos.

### Classe Produto:

Atributos: 

1. nome (*str*)

2. preco (*float*)

3. categoria (*str*)

Método: 

1. detalhes() - Retorna uma descrição do produto.

---

### Classe Pedido:

Atributos: 

1. produtos (*list* - lista de instâncias Produto), 

2. quantidade (*dict* - dicionário que mapeia cada produto à sua quantidade), 

3. cliente (*str*), 

4. status (*str* - valores possíveis: "Novo", "Processando", "Enviado").

Métodos:

1. total_pedido(): Calcula o total do pedido aplicando *map()* e *reduce()* nos produtos e suas quantidades.

2. detalhes_pedido(): Retorna os detalhes do pedido (*produtos, quantidade, cliente, status*).

---

### Classe GestorDePedidos:

Atributos:

1. pedidos (*list* - lista de pedidos)

Métodos:

1. adicionar_pedido(pedido): Adiciona um novo pedido à lista.

2. listar_pedidos_por_status(status): Retorna pedidos com um status específico usando filter.

3. pedidos_por_categoria(categoria): Usar *map()* para gerar um relatório de quantos produtos de uma categoria
específica foram vendidos.

3. total_vendas(): Retorna o valor total de vendas utilizando *reduce()*.

Manipulação de Arquivos:

1. salvar_dados_json(): Salva os pedidos em um arquivo JSON.

2. carregar_dados_json(): Carrega os dados de pedidos do JSON.

3. salvar_dados_binario(): Salva os dados em um arquivo binário usando pickle.

4. carregar_dados_binario(): Carrega os dados de um arquivo binário usando pickle.

---

### Tratamento de Exceções

Para tornar a aplicação mais robusta, implemente tratamento de exceções nos seguintes casos:

Manipulação de Arquivos:

1. Utilize *try-except* para lidar com erros de abertura e leitura de arquivos (ex.: *FileNotFoundError*).

2. Adicione mensagens de erro ao usuário para que ele saiba quando ocorre um problema durante a leitura ou gravação dos dados.

Validação de Pedidos e Produtos:

1. Verifique se os preços dos produtos são válidos (positivos) ao adicioná-los, lançando uma exceção personalizada ValorInvalidoError caso contrário.

2. Ao tentar adicionar um pedido, verifique se a quantidade é um número positivo e levante uma exceção QuantidadeInvalidaError caso contrário.

Decorator de *Log* para Métodos

1. Adicione um decorator log_atividade na classe GestorDePedidos para registrar a execução de métodos, incluindo informações como nome do método, argumentos e o valor de retorno. 

2. Aplique-o aos métodos adicionar_pedido() e listar_pedidos_por_status().

---

### Funcionalidade com BotCity

Use o BotCity para automatizar duas tarefas:

- Preenchimento de Interface Externa com Pedidos:

```
1. Configure o BotCity para abrir uma planilha ou formulário web e preencher os dados dos pedidos.

2. O bot deve iterar pela lista de pedidos na classe GestorDePedidos, navegando entre campos e preenchendo as informações de cada pedido (cliente, produtos, quantidades, total e status).
```

- Extração de Pedidos para a Aplicação:

```
1. Em um segundo momento, configure o BotCity para extrair os dados de pedidos de uma interface externa (planilha ou formulário) e carregar esses dados na aplicação.

2. Para cada linha de dados, o bot deve criar uma instância da classe Pedido e adicionar o pedido à lista de GestorDePedidos.
```

---

### Desafios e Reflexão em Equipe

Após concluir a atividade, peça à equipe para refletir sobre:

1. Tratamento de Exceções: Como o uso de exceções melhorou a robustez da aplicação?

2. Integração de Arquivos JSON e Binários: Qual formato de arquivo preferem para diferentes contextos e por quê?

3. Automação com RPA e BotCity: Como o BotCity pode ser usado para automatizar fluxos repetitivos de entrada e saída de dados?
