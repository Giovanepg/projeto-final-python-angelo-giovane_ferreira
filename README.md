# 📚 Sistema de Gerenciamento de Livros em Python — **SIBL**

Este projeto apresenta o **Sistema Integrado de Bibliotecas e Livrarias (SIBL)**, desenvolvido em Python e executado diretamente no terminal.  
O sistema permite cadastrar livros, listar registros, atualizar dados, remover itens e gerar relatórios completos do acervo.

---

## ⚙️ Estrutura Geral do Sistema

O programa funciona através de um **menu interativo**, utilizando um loop `while` que mantém o sistema ativo até o usuário escolher a opção **0 - Sair**.

Cada opção chama uma função específica, deixando o código organizado e fácil de manter.

```
MENU PRINCIPAL SIBL
1 - Cadastrar Livro
2 - Listar todos os livros
3 - Atualizar dados de um livro
4 - Remover livro
5 - Gerar relatório do acervo
0 - Sair
```

---

## 🧩 Funcionalidades

### **1️⃣ Cadastrar Livro**
O sistema solicita ao usuário:

- Título  
- Autor  
- Valor do livro (em R$)  

O ID é gerado automaticamente com `random.randint()`.

Cada livro é armazenado como um **dicionário** dentro da lista `livros`:

```python
{"id": 101, "titulo": "Exemplo", "autor": "Autor", "valor": 39.90}
```

Inclui tratamento de erro para evitar valores inválidos.

---

### **2️⃣ Listar Livros**
Mostra todos os livros cadastrados, exibindo:

- ID  
- Título  
- Autor  
- Valor formatado em R$  

Se não houver livros cadastrados, exibe uma mensagem informando o usuário.

---

### **3️⃣ Atualizar Dados do Livro**
Permite alterar completamente um livro existente.

Fluxo:

1. Usuário informa o ID  
2. O sistema valida o número e verifica se existe  
3. São solicitados os novos dados:  
   - Título  
   - Autor  
   - Valor  
4. Os dados são atualizados no dicionário correspondente  

Inclui validação de entrada numérica e tratamento de exceções.

---

### **4️⃣ Remover Livro**
Remove um livro baseado no ID fornecido:

- Caso exista → o livro é removido  
- Caso não exista → o sistema informa que o ID não foi encontrado  

---

### **5️⃣ Gerar Relatório do Acervo**
Gera um relatório contendo:

✔ Total de livros cadastrados  
✔ Média dos valores dos livros  
✔ Lista completa, ordenada por ID  
✔ Contagem de livros por autor  

Exemplo:

```
---- RELATÓRIO DO ACERVO ----
Total de livros: 3
Valor médio de preço: 42.50

Lista de livros (ordenada por ID):
12 - Título: ABC, Autor: João, Valor: R$ 20.00
35 - Título: XYZ, Autor: Ana, Valor: R$ 45.00

Contagem por Autor:
João                 - 2 livros
Ana                  - 1 livro
```

---

## 🧠 Estruturas de Dados Utilizadas

| Estrutura | Utilização |
|----------|------------|
| **list** | Armazena todos os livros cadastrados |
| **dict** | Representa cada livro individualmente |
| **random** | Gera IDs automaticamente |
| **float / int** | Utilizados para valores e identificadores |

---

## 🔄 Estruturas de Controle

O sistema utiliza:

- **while** → mantém o menu ativo  
- **for** → percorre a lista de livros  
- **if / elif / else** → controla decisões e fluxos  
- **try / except** → trata erros como:  
  - ID inválido  
  - Valor não numérico  
  - Exceções inesperadas  

---

## 🧱 Organização do Código

O sistema está dividido em funções, facilitando manutenção e leitura:

- `cadastrar_livros()`  
- `listar_livros()`  
- `atualizar_registro()`  
- `remover_livros()`  
- `gerar_relatorio()`  
- `menu()`  
