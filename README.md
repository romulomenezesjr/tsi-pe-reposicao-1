# Programação Estruturada: Prova 01

## Questão 1:

Faça um programa que calcula a quantidade de divisores de um número (incluindo 1 e o próprio número) que são divisíveis por 3.

[Referência](https://www.thehuxley.com/problem/2842?quizId=4323)

### Formato de entrada

O usuário deve digitar um inteiro N.

### Formato de saída

O programa deve exibir um inteiro R, sendo R o número de divisores de N que são divisiveis por 3. Caso não tenha nenhum, imprima "O numero nao possui divisores multiplos de 3" sem as aspas.

O programa deve imprimir

Quantidade de divisores divisiveis por 3: n / O numero nao possui divisores multiplos de 3

### Exemplo 1:

Entrada:

- 7

Saída:

- O número não possui divisores multiplos de 3

### Exemplo 2:

Entrada:

- 3

Saída:

- Quantidade de divisores divisiveis por 3: 1

### Exemplo 3:

Entrada:

- 555

Saída:

- Quantidade de divisores divisiveis por 3: 4

### Exemplo 4:

Entrada:

- 3144

Saída:

- Quantidade de divisores divisiveis por 3: 8

### Exemplo 5:

Entrada:

- 17640

Saída:

- Quantidade de divisores divisiveis por 3: 48

## Questões 2:

Escreva um programa que receba como entrada dois números inteiros e retorne a soma dos números positivos no intervalo definido por eles, considerando inclusive os extremos.

[Referência](https://www.thehuxley.com/problem/406?quizId=4323)

Obs: o intervalo pode ser crescente ou decrescente

### Exemplo 1:

Entrada:

- -2
- 2

Saída:

- 3

### Exemplo 2:

Entrada:

- 1
- 3

Saída:

- 3

### Exemplo 3:

Entrada:

- 10
- -10

Saída:

- 55

#### Formato de entrada

Dois números inteiros

Dica: os números podem ser informados em qualquer ordem (não necessariamente o primeiro será menor que o segundo)

#### Formato de saída

Um número inteiro

## Questão 3:

Uma empresa está migrando seus serviços para a nuvem e deseja calcular o custo total de infraestrutura para um determinado serviço web. Eles têm dados sobre o uso mensal de recursos e os custos associados a esses recursos. Sua tarefa é escrever um programa em Python que calcule o custo total mensal com base nas informações fornecidas.

A empresa utiliza os seguintes recursos, com os respectivos custos mensais:

1. **Servidores**: O custo mensal por servidor é de R$ 500.

2. **Banco de Dados**: O custo mensal por unidade de capacidade do banco de dados é de R$ 100.

3. **Armazenamento de Dados**: O custo mensal por gigabyte de armazenamento de dados é de R$ 0,10.

4. **Transferência de Dados**: O custo mensal por gigabyte de transferência de dados de entrada e saída é de R$ 0,05.

A entrada será fornecida da seguinte forma:

n - O número de servidores usados.
m - O número de unidades de capacidade do banco de dados.
o - A quantidade de armazenamento de dados em gigabytes.
p - A quantidade de transferência de dados de entrada e saída em gigabytes.

Seu programa deve calcular o custo total mensal com base nessas informações e imprimir o resultado. Além disso, ele deve verificar se o custo total mensal ultrapassa um limite máximo de R$ 10.000. Se o custo total mensal for maior que esse limite, o programa deve exibir uma mensagem indicando que o custo está acima do limite.

### Exemplo 1:

Entrada:

```
Número de servidores: 5
Unidades de capacidade do banco de dados: 10
Armazenamento de dados (em GB): 500
Transferência de dados de entrada e saída (em GB): 1000
```

Saída:

```
O custo total mensal estimado para a infraestrutura é de R$ 8,500.
```

### Exemplo 2:

Entrada:

```
Número de servidores: 10
Unidades de capacidade do banco de dados: 50
Armazenamento de dados (em GB): 1000
Transferência de dados de entrada e saída (em GB): 10000
```

Saída:

```
O custo total mensal está acima do limite.
```

## Questão 4:

Escreva um programa que calcule os N termos da série S abaixo:

S = (1/3) + (2/6) + (3/9) + (4/12) + …

O seu programa deve imprimir na saída padrão tanto os termos da série quanto o valor da soma com precisão de 2 casas decimais.

[Referência](https://www.thehuxley.com/problem/1089)

### Formato de entrada

Um valor N que representa a quantidade de termos da série.

### Formato de saída

Os termos da série e o valor da soma com precisão de 2 casas decimais.

### Exemplos:

Entrada:

- 0

Saída:

- 0.00

Entrada:

- 8

Saída:

- 1/3 + 2/6 + 3/9 + 4/12 + 5/15 + 6/18 + 7/21 + 8/24
- 2.67

Entrada:

- 4

Saída:

- 1/3 + 2/6 + 3/9 + 4/12
- 1.33
