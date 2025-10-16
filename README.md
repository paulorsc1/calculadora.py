Calculadora com Pytest

   Criamos uma classe chamada Calculadora.

Uma classe é como um molde que agrupa várias funções (métodos) relacionadas.

Cada método faz uma operação matemática:

soma(a, b) → soma dois números.

subtrai(a, b) → subtrai o segundo número do primeiro.

multiplica(a, b) → multiplica os dois números.

divide(a, b) → divide o primeiro pelo segundo e avisa se tentar dividir por zero.

potencia(a, b) → calcula 
𝑎
𝑏
a
b
, ou seja, eleva a à potência b.

raiz(x) → calcula a raiz quadrada de x e avisa se o número for negativo.

media(lista) → calcula a média de uma lista de números e avisa se a lista estiver vazia.

modulo(x) → retorna o valor absoluto (ignora sinal negativo).

percentual(parte, total) → calcula a porcentagem de parte em relação ao total e avisa se o total for zero.

Os Testes (test_calculadora.py)

Usamos o pytest para criar testes automáticos.

Cada teste confirma que a função da calculadora funciona corretamente:

Por exemplo: assert c.soma(3, 2) == 5 → verifica se 3 + 2 é realmente 5.

Também testamos erros esperados, como:

Dividir por zero.

Raiz de número negativo.

Lista vazia na média.

Percentual com total zero.

Como tudo funciona junto

Você chama uma função da calculadora, por exemplo c.soma(4,5).

Ela retorna o resultado (neste caso, 9).

O pytest executa todos os testes e mostra se todas as funções estão funcionando corretamente.


# Como usar
1. Instale o pytest:
   ```bash
   pip install pytest
