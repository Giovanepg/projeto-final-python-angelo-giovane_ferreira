````markdown
# 📚 Sistema de Gerenciamento de Livros em Python

Este projeto é um **sistema simples de cadastro e gerenciamento de livros**, desenvolvido em Python e executado diretamente pelo terminal.  
O programa permite registrar livros, listar, atualizar, remover e gerar relatórios completos do acervo.

![](/mnt/data/A_set_of_four_digital_user_interface_prototype_scr.png)

---

## ⚙️ Estrutura Geral

O sistema funciona por meio de um **menu interativo**, usando um loop `while` que continua executando até o usuário escolher a opção **0 - Sair**.

Cada opção do menu chama uma função específica, deixando o código organizado, modular e fácil de entender.

---

## 🧩 Funcionalidades Principais

### 1️⃣ Cadastrar Livro
Solicita ao usuário:
- ID (gerado automaticamente)
- Título  
- Autor  
- Valor em reais  

O livro é armazenado como um **dicionário**, dentro da lista `livros`.

---

### 2️⃣ Listar Livros
Exibe todos os livros cadastrados, mostrando:
- ID  
- Título  
- Autor  
- Valor (formatado em R$)

Caso a lista esteja vazia, o sistema informa o usuário.

---

### 3️⃣ Atualizar Livro
Permite alterar o título e o autor de um livro.
Funcionamento:

- O sistema pede o **ID** do livro  
- Procura na lista  
- Se encontrado, solicita os novos dados  
- Atualiza o dicionário correspondente

Se o ID não existir, mostra uma mensagem de erro.

---

### 4️⃣ Remover Livro
Remove um livro também baseado no ID.

- O usuário informa o ID  
- O sistema busca na lista  
- Caso encontre, exclui o registro  
- Exibe mensagem de confirmação

Se não encontrar, informa que o ID é inválido.

---

### 5️⃣ Gerar Relatório do Acervo
Exibe um relatório contendo:

✔ Total de livros cadastrados  
✔ Lista completa, ordenada por ID  
✔ Valor de cada livro  
✔ Contagem de livros por autor  

Útil para visualizar rapidamente a situação geral do acervo.

---

### 0️⃣ Sair
Encerra o sistema com uma mensagem simples.

---

## 🧠 Estruturas de Dados Utilizadas

| Estrutura | Função |
|----------|--------|
| **list** | Armazena todos os livros cadastrados (`livros`). |
| **dict** | Representa cada livro (com ID, título, autor e valor). |
| **int / float** | Usados para identificar o livro e registrar seu valor. |
| **for / if** | Controlam toda a lógica de busca, atualização e listagem. |

---

## 🔄 Estruturas de Controle

O sistema usa:

- **while** → mantém o menu rodando  
- **for** → percorre os livros cadastrados  
- **if / elif / else** → controla o fluxo das operações  
- **funções (def)** → deixam o código organizado, separado por tarefas  

---

