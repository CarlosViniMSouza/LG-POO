1. O que acontece se você tentar acessar diretamente o atributo __saldo fora da classe?

resp.: `AttributeError: 'BankAccount' object has no attribute 'balance'` -> Isso é, o interpretador acusa um erro onde o programa tenta fazer a leitura/acesso da variavel privada, mas não pode faze-lo.

2. Como o método __init__ ajuda a inicializar os atributos da classe?

resp.: Ele é chamado automaticamente quando uma nova instância da classe é criada, e serve para inicializar os atributos da classe `(definir seus valores iniciais)`.

3. Por que é importante usar encapsulamento em uma classe como ContaBancaria?

resp.: Para proteger as características da classe de possivéis acesso indevidos por outras classes e/ou métodos não pertencentes a classe.

4. Como você pode adicionar métodos adicionais para aumentar a funcionalidade da classe ContaBancaria?

resp.: Pode-se adicionar métodos que realizam processos específicos, ou que manipulam os atributos para determinados fins.
