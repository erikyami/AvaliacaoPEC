# CRUD de Produtos: Híbrido (Imperativo & Funcional)
Aluno: Francisco Erik da Silva

Este projeto consiste em um sistema de gestão de estoque desenvolvido em Python como parte da avaliação da disciplina de **Paradigmas de Programação**. O objetivo é demonstrar a integração prática entre os paradigmas **Imperativo** e **Funcional**, separando a interface de usuário da lógica de transformação de dados.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **Módulos:** `functools` (para a operação de redução `reduce`)

---

## 🏗️ Estrutura do Projeto

O software foi estruturado em duas camadas conceituais para garantir clareza e previsibilidade:

### 1. Camada Funcional (Lógica de Dados)
Nesta camada, os dados são tratados seguindo princípios de imutabilidade. As funções não alteram a lista original, mas retornam novas versões processadas:
* **Imutabilidade:** Operações como `f_adicionar` utilizam a concatenação de listas para gerar novos estados sem modificar a coleção anterior.
* **Funções de Ordem Superior:**
    * `filter`: Utilizada em `f_remover` para criar uma nova lista excluindo o ID selecionado.
    * `map`: Utilizada em `f_atualizar` para transformar a lista, substituindo apenas o item correspondente ao ID buscado.
    * `reduce`: Utilizada em `f_calcular_total` para agregar os preços de todos os produtos de forma declarativa.
* **Expressões Lambda:** Empregadas para definir lógicas de comparação e transformação de forma concisa dentro das funções de ordem superior.

### 2. Camada Imperativa (Interface e Estado)
Responsável pelo fluxo de execução, interação com o utilizador e gestão do ciclo de vida da aplicação:
* **Estado Mutável:** Gerencia as variáveis `estoque` (lista que armazena os dados) e `proximo_id` (controlo de autoincremento).
* **Autoincremento:** O sistema gere os IDs automaticamente, garantindo unicidade sem depender da entrada manual do utilizador.
* **Estruturas de Controlo:** Utilização de loops `while` e condicionais `if/elif` para coordenar o menu e validar as entradas de dados.

---

## 🔍 Funcionalidades Implementadas

1.  **Cadastrar (Create):** Regista um novo produto com um **ID gerado automaticamente**.
2.  **Listar (Read):** Exibe todos os produtos em stock de forma estruturada.
3.  **Atualizar (Update):** Permite alterar o nome e o preço de um produto existente através de uma busca por ID.
4.  **Remover (Delete):** Exclui um item gerando uma nova coleção filtrada.
5.  **Relatório (Aggregate):** Calcula dinamicamente o valor total acumulado no inventário utilizando redução funcional.

---

## 🚀 Como Executar

1. Certifique-se de que tem o Python 3 instalado no seu sistema.
2. Guarde o código-fonte num ficheiro chamado `estoque.py`.
3. Execute o comando no seu terminal:
   ```bash
   python estoque.py
   ```
## 📝 Conclusão

A implementação deste sistema CRUD demonstra que a coexistência de diferentes paradigmas em um mesmo projeto permite extrair o melhor de cada abordagem:

1. **Eficiência do Paradigma Imperativo:** Foi essencial para gerenciar o ciclo de vida da aplicação. O uso de estruturas de controle (`while`, `if/else`) e variáveis mutáveis facilitou a interação direta com o usuário e a manutenção de um estado global (estoque) que persiste durante a execução.
2. **Segurança do Paradigma Funcional:** Ao isolar a lógica de processamento em funções puras, garantimos que a manipulação de dados (filtros, mapeamentos e reduções) não gerasse efeitos colaterais indesejados. O uso de `map`, `filter` e `reduce` tornou o código mais conciso, declarativo e menos propenso a erros comuns de manipulação de coleções.

Essa estrutura híbrida resultou em um software onde a interface é clara e sequencial, enquanto o motor de processamento de dados é robusto, seguindo os princípios de imutabilidade e previsibilidade.

---

## Diferença percebidas entre os paradigmas
- No Paradigma Funcional: O foco está no "o quê" deve ser feito. As funções `f_remover` ou `f_atualizar` descrevem uma transformação de dados. Não há preocupação com o estado anterior da lista, apenas com o resultado da expressão.  
- No Paradigma Imperativo: O foco está no "como" as coisas acontecem. A função `sistema_cadastro` dita o passo a passo: ler entrada, verificar condição, atualizar variável, imprimir mensagem. É uma receita de bolo sequencial.  

## Vantagens e desvantagens de cada abordagem
- No paradigma funcional tem a vantagem de ter a imutabilidade e a modularidade, porém pode ter um uso maior de consumo de memória quando faz uma copia da lista a cada interação;
- No paradigma imperativo tem a vantagem de ter o controle do que será feito, mas ao trabalhar com mutabilidade pode ser mais fácil ter erros indesejados pelo mesmo motivo.

## Qual abordagem foi mais fácil/difícil e por quê
- O paradigma imperativo é mais fácil por ser mais direto, enquanto o paradigma funcional possui um nível de abstração maior, tentendo a ter uma curva de aprendizagem;


## Impacto na legibilidade e manutenção do código
- O paradigma funcional tem maior legibilidade e mais facibilidade na manutenção do código. 
- No paradigma imperativo é mais suscetível a erros devido a mutabilidade e manipulação de variáveis globais.
