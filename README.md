# exercicios-python

## Lista de Exercícios de Python com Versionamento

### Identificação

* **Estudante:** Victor Martins Günther
* **Turma:** DSM3 - 2025 - 2ª Série
* **Unidade Curricular:** Programação de Aplicativos
* **Curso:** Técnico em Desenvolvimento de Sistemas — Integrado ao Ensino Médio
* **Docente:** Ewerton de Oliveira Cercal

---

### Descrição do Projeto

Este repositório contém a resolução de vinte e cinco exercícios práticos de lógica de programação desenvolvidos na linguagem Python. O objetivo da atividade é consolidar fundamentos essenciais, incluindo entrada e saída de dados, estruturas condicionais, laços de repetição e manipulação de listas, integrando as soluções a boas práticas de organização, documentação e controle de versão com Git e GitHub.

---

### Tecnologia Utilizada

* **Linguagem:** Python
* **Versão:** Python 3.12.2

---

### Estrutura do Repositório

O projeto está organizado em diretórios correspondentes às etapas temáticas do trabalho, garantindo a separação clara de cada exercício:

```text
exercicios-python/
├── README.md
├── .gitignore
├── parte1-variaveis/
│   ├── ex01.py
│   ├── ex02.py
│   ├── ex03.py
│   ├── ex04.py
│   └── ex05.py
├── parte2-condicionais/
│   ├── ex06.py
│   ├── ex07.py
│   ├── ex08.py
│   ├── ex09.py
│   └── ex10.py
├── parte3-while/
│   ├── ex11.py
│   ├── ex12.py
│   ├── ex13.py
│   ├── ex14.py
│   └── ex15.py
├── parte4-for/
│   ├── ex16.py
│   ├── ex17.py
│   ├── ex18.py
│   ├── ex19.py
│   └── ex20.py
└── parte5-listas/
    ├── ex21.py
    ├── ex22.py
    ├── ex23.py
    ├── ex24.py
    └── ex25.py
```

---

### Como Executar os Programas

Para executar qualquer um dos exercícios em seu ambiente local, siga os passos abaixo:

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/exercicios-python.git
   ```

2. **Navegar até a pasta do projeto:**
   ```bash
   cd exercicios-python
   ```

3. **Executar o exercício desejado:**
   Passe o caminho relativo da pasta e do arquivo para o interpretador Python. Exemplos:
   * Para rodar o Exercício 01 (Variáveis):
     ```bash
     python parte1-variaveis/ex01.py
     ```
   * Para rodar o Exercício 09 (Condicionais):
     ```bash
     python parte2-condicionais/ex09.py
     ```
   * Para rodar o Exercício 25 (Listas):
     ```bash
     python parte5-listas/ex25.py
     ```

---

### Índice dos Exercícios

#### Parte 1 — Variáveis, entrada e saída (`parte1-variaveis/`)
* **`ex01.py`**: Armazena o nome e a idade em variáveis e exibe cada valor em uma linha separada.
* **`ex02.py`**: Solicita dois números inteiros ao usuário e exibe a soma entre eles.
* **`ex03.py`**: Recebe o raio de um círculo e calcula a sua área considerando o valor de pi igual a 3.14159.
* **`ex04.py`**: Converte uma temperatura informada em graus Celsius para a escala Fahrenheit.
* **`ex05.py`**: Solicita o preço e a quantidade comprada de um produto e exibe o valor total formatado com duas casas decimais.

#### Parte 2 — Condicionais (`parte2-condicionais/`)
* **`ex06.py`**: Recebe um número inteiro e informa se ele é par ou ímpar.
* **`ex07.py`**: Recebe dois números e exibe qual é o maior, informando caso sejam iguais.
* **`ex08.py`**: Avalia um número informado e indica se ele é positivo, negativo ou igual a zero.
* **`ex09.py`**: Recebe a média de um estudante e classifica sua situação em Aprovado (>= 6), Recuperação (4 a 5.9) ou Reprovado (< 4).
* **`ex10.py`**: Solicita a idade do usuário e informa se ele atinge a idade mínima de 16 anos para votar.

#### Parte 3 — Repetição com while (`parte3-while/`)
* **`ex11.py`**: Exibe os números inteiros de 1 a 10, um por linha, utilizando o laço while.
* **`ex12.py`**: Solicita números continuamente e exibe o somatório total acumulado quando o valor 0 for digitado.
* **`ex13.py`**: Solicita a senha ao usuário repetidamente até que a senha correta ("senai123") seja digitada, liberando o acesso.
* **`ex14.py`**: Recebe um número e exibe a sua tabuada completa do 1 ao 10.
* **`ex15.py`**: Recebe números até que o valor 0 seja informado e exibe a quantidade total de números positivos digitados.

#### Parte 4 — Repetição com for (`parte4-for/`)
* **`ex16.py`**: Exibe os números inteiros de 1 a 20, um por linha, utilizando o laço for.
* **`ex17.py`**: Imprime na tela apenas os números pares contidos no intervalo de 2 a 20.
* **`ex18.py`**: Calcula e exibe a soma de todos os números inteiros no intervalo de 1 a 100.
* **`ex19.py`**: Recebe um número inteiro e calcula o seu fatorial iterativamente.
* **`ex20.py`**: Executa uma contagem regressiva de 10 até 1 e exibe a mensagem "Fim" ao encerrar.

#### Parte 5 — Listas (`parte5-listas/`)
* **`ex21.py`**: Cria uma lista contendo cinco números e exibe cada elemento individualmente.
* **`ex22.py`**: Percorre a lista de números criada e calcula a soma de todos os seus elementos.
* **`ex23.py`**: Percorre a lista de números e identifica qual é o maior valor presente.
* **`ex24.py`**: Filtra a lista pré-definida `[5, 12, 8, 20, 3, 15]` e informa quantos itens são estritamente maiores que 10.
* **`ex25.py`**: Recebe a lista `[3, 7, 1, 9, 4]` e exibe seus elementos na ordem inversa manipulando os índices.

---
