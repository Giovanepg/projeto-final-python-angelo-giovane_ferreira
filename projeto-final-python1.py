import random

# Inicialização da lista de livros
livros = []

def cadastrar_livros(livros):
    id = random.randint(1, 999)  # Gera um ID aleatório
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor: ")
    valor = float(input("Digite o valor do livro: R$ "))

    livros.append({"id": id, "titulo": titulo, "autor": autor, "valor": valor})
    print(f"Livro cadastrado com ID: {id}")

def listar_livros(livros):
    if len(livros) < 1:  # Verifica se a lista está vazia
        print("Não há livros no acervo!")
    else:
        for livro in livros:  # Percorre e mostra todos os livros
            print(f"{livro['id']} - Título: {livro['titulo']}, Autor: {livro['autor']}, Valor: R$ {livro['valor']:.2f}")

def atualizar_registro(livros):
    # Testa se o ID é numérico
    try:
        id_fornecido = int(input("Digite o ID do livro a ser atualizado: "))
    except ValueError:
        print(f"Erro: o ID deve ser um número inteiro")
        return

    # Procura o livro pelo ID
    livro_encontrado = None
    for livro in livros:
        if livro['id'] == id_fornecido:
            livro_encontrado = livro
            break

    if not livro_encontrado:
        print(f"Livro de ID {id_fornecido} não encontrado!")
        return
    
    try:
        novo_titulo = input("Digite o novo título: ")
        novo_autor = input("Digite o novo autor: ")    
        novo_valor = float(input("Digite o novo valor: "))
        
    except ValueError:
        print("Erro: o valor deve ser numérico.")
        return
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return

    # Atualiza o dicionário com os novos dados
    livro_encontrado['titulo'] = novo_titulo
    livro_encontrado['autor'] = novo_autor
    livro_encontrado['valor'] = novo_valor

    print("Dados atualizados com sucesso!")

def remover_livros(livros):
    id_fornecido = int(input("Digite o ID do livro para ser excluído: "))
    for livro in livros:
        if livro['id'] == id_fornecido:
            livros.remove(livro)  # Remove livro da lista
            print(f"Livro com ID {id_fornecido} removido!")
            break
    else:
        print(f"ID {id_fornecido} não encontrado.")

def gerar_relatorio(livros):
    if len(livros) < 1:  # Se não houver livros, sai da função
        print("Não há livros no acervo!")
        return

    total = len(livros)
    soma = 0  # Variável para o cálculo da média

    for livro in livros:
        soma += livro['valor']

    valor_medio = soma / len(livros)  # Calcula a média de preço

    print("---- RELATÓRIO DO ACERVO ----")
    print(f"Total de livros: {total}")
    print(f"Valor médio de preço: {valor_medio}\n")

    # Lista ordenada por id
    print("Lista de livros (ordenada por ID):")
    for livro in sorted(livros, key=lambda l: l['id']):
        print(f"  {livro['id']} - Título: {livro['titulo']}, Autor: {livro['autor']}, Valor: R$ {livro['valor']:.2f}")

    # Contagem por autor
    contagem_autores = {}
    for livro in livros:
        autor = livro['autor']
        contagem_autores[autor] = contagem_autores.get(autor, 0) + 1

    print("\nContagem por Autor:")
    print("---------------------------")

    # Ordena alfabeticamente os autores
    for autor in sorted(contagem_autores):
        qtd = contagem_autores[autor]
        palavra = "livro" if qtd == 1 else "livros"
        print(f"{autor:<20} - {qtd} {palavra}")

    print("---------------------------\n")


# Função principal - Exibe o menu
def menu():
    while True:
        print("MENU PRINCIPAL SIBL (Sistema Integrado de Bibliotecas e Livrarias)")
        print("1 - Cadastrar Livro")
        print("2 - Listar todos os livros")
        print("3 - Atualizar dados de um livro")
        print("4 - Remover livro")
        print("5 - Gerar relatório do acervo")
        print("0 - SAIR")

        opcao = int(input("Digite a opção correspondente: "))

        # Direciona para a função correspondente
        if opcao == 1:
            cadastrar_livros(livros)
        elif opcao == 2:
            listar_livros(livros)
        elif opcao == 3:
            atualizar_registro(livros)
        elif opcao == 4:
            remover_livros(livros)
        elif opcao == 5:
            gerar_relatorio(livros)
        elif opcao == 0:
            print("Saindo do menu...")
            break
        else:
            print("Opção inválida!")

menu()