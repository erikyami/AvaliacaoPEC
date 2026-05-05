from functools import reduce

# --- CAMADA FUNCIONAL (Lógica de Dados) ---

def f_adicionar(lista, id_novo, nome, preco):
    # Imutabilidade: Retorna uma nova lista com o novo dicionário
    return lista + [{"id": id_novo, "nome": nome, "preco": preco}]

def f_remover(lista, id_busca):
    return list(filter(lambda p: p['id'] != id_busca, lista))

def f_atualizar(lista, id_busca, novo_nome, novo_preco):
    return list(map(lambda p: 
        {"id": id_busca, "nome": novo_nome, "preco": novo_preco} 
        if p['id'] == id_busca else p, lista))

def f_calcular_total(lista):
    return reduce(lambda acc, p: acc + p['preco'], lista, 0)


# --- CAMADA IMPERATIVA (Interface e Controle de Estado) ---

def sistema_cadastro():
    estoque = []      # Estado mutável (lista de produtos)
    proximo_id = 1    # Controle mutável para Autoincremento
    
    while True:
        print("\n=== SISTEMA COM AUTOINCREMENTO ===")
        print(f"Itens no estoque: {len(estoque)}")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Remover")
        print("5. Relatório (Total R$)")
        print("0. Sair")
        
        opcao = input("\nEscolha: ")

        if opcao == "0":
            break

        if opcao == "1":
            print(f"Gerando ID automático: {proximo_id}")
            nome = input("Nome do produto: ")
            preco = float(input("Preço: "))
            
            # Atualiza o estoque usando a função funcional
            estoque = f_adicionar(estoque, proximo_id, nome, preco)
            
            # Incremento imperativo do contador
            proximo_id += 1 
            print("Produto cadastrado com sucesso!")

        elif opcao == "2":
            print("\n--- ESTOQUE ---")
            if not estoque: print("Estoque vazio.")
            for p in estoque:
                print(f"ID: {p['id']} | Nome: {p['nome']} | R$ {p['preco']:.2f}")

        elif opcao == "3":
            id_busc = int(input("ID para editar: "))
            # Verificação simples antes de chamar a lógica funcional
            if any(p['id'] == id_busc for p in estoque):
                n_nome = input("Novo Nome: ")
                n_preco = float(input("Novo Preço: "))
                estoque = f_atualizar(estoque, id_busc, n_nome, n_preco)
                print("Produto atualizado!")
            else:
                print("ID não encontrado.")

        elif opcao == "4":
            id_rem = int(input("ID para remover: "))
            estoque = f_remover(estoque, id_rem)
            print("Operação de remoção concluída.")

        elif opcao == "5":
            total = f_calcular_total(estoque)
            print(f"\nValor total do inventário: R$ {total:.2f}")

if __name__ == "__main__":
    sistema_cadastro()