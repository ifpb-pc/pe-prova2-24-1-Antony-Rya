[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PEBCr5PN)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=16049602&assignment_repo_type=AssignmentRepo)
# Programação Estruturada: Prova 02

## Questão 1:

Dado um array inteiro **nums**, retorne verdadeiro se algum valor aparecer pelo menos duas vezes no array e retorne falso se cada elemento for distinto. Crie duas funções (q1a e q1b) que resolvam este problemas utilizando apenas as listas e outra que utilize dicionários.

### Exemplo 1:

Input: nums = [1,2,3,1]

Output: True

Explicação:

O elemento 1 apareceu nos índices 0 and 3.

### Exemplo 2:

Input: nums = [1,2,3,4]

Output: False

Explicação:

Todos os elementos são distintos.

### Exemplo 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

## Questão 2:

Dadas duas strings s e t, retorne verdadeiro se t for um **anagrama** de s, e falso caso contrário.

Exemplo 1:

Entrada: s = "anagram", t = "nagaram"

Saída:True

Exemplo 2:

Entrada: s = "rat", t = "car"

Saída: Falso


## Questão 3:

Leia um arquivo CSV chamado estoque.csv, contendo informações de produtos em estoque (Nome, Quantidade, Preço). Atualize o arquivo CSV, multiplicando o preço de todos os produtos por 1.1 (aumento de 10%). Além de atualizar o arquivo, sua função deve retornar o valor total em estoque (soma da quantidade de cada produto x preço).

Dica: Você pode utilizar o módulo csv para ler e escrever de volta os dados atualizados no arquivo ou as funções read, readline, readlines, write, writelines

## Questão 4:

Você deverá ler valores numéricos até o usuário digitar 0. Use uma função ler_valores() para retornar os valores deverão ser passados para uma função processa_lista(lista) que irá retornar 2 listas, uma lista para valores pares e uma lista para ímpares. O tamanho máximo de cada uma das listas é de 5. Logo, cada vez que uma das listas ficar cheia você deve substituir os valores mais antigos pelos valores novos. Após executar a função, você deve imprimir o conteúdo em cada uma das listas.

Exemplos
Entrada: [2, 4, 6, 8, 10, 12, 14, 0]

Saída Esperada:

Lista de Pares: [12, 14, 6, 8, 10]
Lista de Ímpares: []
Entrada: [1, 3, 5, 7, 9, 11, 0]

Saída Esperada:

Lista de Pares: []
Lista de Ímpares: [11, 9, 7, 5, 3]
Entrada: [2, 4, 6, 8, 10, 12, 1, 3, 5, 7, 9, 11, 0]

Saída Esperada:

Lista de Pares: [12, 4, 6, 8, 10]
Lista de Ímpares: [11, 3, 5, 7, 9]