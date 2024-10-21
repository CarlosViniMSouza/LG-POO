1. O que acontece se você adicionar um novo método de pagamento sem modificar a função processar?

**Resp.: Poderia trabalhar com o reajuste da função 'payment_process()' da mesma forma como trabalhei com os demais métodos (Cartão, Boleto e Pix)**

2. Como o polimorfismo ajuda a manter o código flexível e extensível?

**Resp.: Basicamente, contribui no reaproveitamento do que foi feito anteriormente, e mantém o padrão estabelecido**

3. Qual é a diferença entre a função processar e os métodos processar_pagamento nas subclasses?

**Resp.: a função 'payment_process()' permite a alteração do comportamento dos métodos codificados (Em linhas gerais, quando muda-se o objeto de instânciação, muda-se a mensagem que será retornado pelo mesmo método)**

4. Como você pode garantir que todos os métodos de pagamento implementem o método processar_pagamento corretamente?

**Resp.: Fazendo com os todos os métodos sejam subclasses na class principal Pagamento/('Payment') juntamente com o mesmo nome do método processar_pagamento/(payment_process())**
