### Exercício 1: Sistema de Transferência Bancária com Exceções Personalizadas

- Crie uma classe **Conta** com atributos *titular, saldo, limite*.

- Adicione métodos: *depositar, sacar, transferir*.

- Crie exceções personalizadas para tratar os seguintes erros:

1. **SaldoInsuficienteError (InsufficientBalanceError)**: Lançada ao tentar sacar um valor superior ao saldo disponível.

2. **LimiteExcedidoError (LimitExceededError)**: Lançada ao tentar transferir um valor que ultrapassa o limite da conta.

3. **ContaDestinoInvalidaError (InvalidDestinationAccountError)**: Lançada ao tentar transferir para uma conta inexistente.

Implemente um bloco *try-except* para capturar e exibir as mensagens de erro personalizadas.

---

### Exercício 2: Validação de Dados do Usuário com Exceções

Crie uma classe **Usuario** que contenha *nome, idade, email*. No método `__init__()`, valide os dados:

1. Levante uma *ValueError* se o nome for vazio.

2. Levante uma *TypeError* se idade não for um número inteiro.

3. Levante uma *ValueError* se email não contiver um "@".