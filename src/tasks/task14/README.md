- Crie uma classe `Venda` que contenha o nome do produto, a quantidade vendida e o preço unitário. Em seguida, crie uma classe `HistoricoVendas` que armazene uma lista de vendas.

Implemente:

1. Um método `total_por_produto()` que retorne o total arrecadado por cada produto usando reduce.
2. Um gerador `listar_vendas_acima_de(valor)` que liste apenas as vendas acima de um valor específico.
3. Use *lambda* e *reduce* para somar as vendas por produto.
4. Implemente o método `listar_vendas_acima_de` como um gerador para economia de memória.

---

- Crie uma classe `Funcionario` com atributos como **nome, cargo, e salario**. Em seguida, crie uma classe `SistemaRH` que gerencie uma lista de funcionários. 

Adicione:

1. Um método `aumentar_salario` que aumenta o salário dos funcionários.
2. Um decorator `autenticar_acesso` que verifique se o usuário tem permissão para realizar um aumento salarial. 
3. Se o cargo do usuário for "Gerente", ele pode aumentar o salário; caso contrário, não.
4. Use o decorator `autenticar_acesso` para verificar o cargo antes de permitir o aumento salarial.

---

- Crie uma classe `Conta` que armazene uma lista de transações. 

Implemente:

1. Um método `filtrar_transacoes_por_tipo(tipo)` que use filter para retornar todas as transações de um determinado tipo (ex.: "Depósito").
2. Um método `aplicar_taxa` que use map para aplicar uma taxa a cada transação de tipo "Saque".
3. Use *filter()* para separar transações de acordo com o tipo especificado.
4. Use *map()* para aplicar a taxa apenas nas transações de saque.
