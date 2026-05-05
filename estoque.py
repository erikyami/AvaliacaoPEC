import json
import os
import sys
import io
from functools import reduce

# Força o terminal a usar UTF-8 para exibir acentos e R$ corretamente
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# --- CAMADA DE PERSISTÊNCIA (Dados) ---

FILE_NAME = "estoque.json"

def carregar_dados():
    """Lê o arquivo JSON e retorna a lista de produtos."""
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []

def salvar_dados(lista):
    """Salva a lista atual de produtos no arquivo JSON."""
    try:
        with open(FILE_NAME, 'w', encoding='utf-8') as f:
            json.dump(lista, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")

# --- CAMADA FUNCIONAL (Lógica de Negócio) ---

def f_adicionar(lista, id_novo, nome, preco):
    # Retorna nova lista (Imutabilidade)
    return lista + [{"id": id_novo, "nome": nome, "preco": preco}]

def f_remover(lista, id_busca):
    # Retorna nova lista filtrada
    return list(filter(lambda p: p['id'] != id_busca, lista))

def f_atualizar(lista, id_busca, novo_nome, novo_preco):
    # Retorna nova lista com o item mapeado/alterado
    return list(map(lambda p: 
        {"id": id_busca, "nome": novo_nome, "preco": novo_preco} 
        if p['id'] == id_busca else p, lista))

def f_calcular_total(lista):
    # Agrega os valores de preço
    return reduce(lambda acc, p: acc + p['preco'], lista, 0)


# --- CAMADA IMPERATIVA (Interface e Controle de Estado) ---

def sistema_cadastro():
    # Carrega estado inicial
    estoque = carregar_dados()
    
    # Calcula o próximo ID disponível (Maior ID + 1)
    proximo_id = max([p['id'] for p in estoque], default=0) + 1
    
    while True:
        print("\n" + "="*30)
        print("   SISTEMA DE ESTOQUE HÍBRIDO")
        print("="*30)
        print(f"Itens no estoque: {len(estoque)}")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Remover")
        print("5. Relatório (Total R$)")
        print("0. Salvar e Sair")
        
        opcao = input("\nEscolha uma opção: ")

        try:
            if opcao == "0":
                salvar_dados(estoque)
                print("Dados salvos com sucesso. Saindo...")
                break

            elif opcao == "1":
                print(f"\n[Gerando ID automático: {proximo_id}]")
                nome = input("Nome do produto: ")
                preco = float(input("Preço: "))
                
                estoque = f_adicionar(estoque, proximo_id, nome, preco)
                proximo_id += 1 
                salvar_dados(estoque) # Persistência automática
                print("✅ Produto cadastrado!")

            elif opcao == "2":
                print("\n" + "-"*15 + " ESTOQUE " + "-"*15)
                if not estoque: 
                    print("O estoque está vazio.")
                for p in estoque:
                    print(f"ID: {p['id']:03d} | Nome: {p['nome']:<15} | R$ {p['preco']:>8.2f}")

            elif opcao == "3":
                id_busc = int(input("Digite o ID para editar: "))
                if any(p['id'] == id_busc for p in estoque):
                    n_nome = input("Novo Nome: ")
                    n_preco = float(input("Novo Preço: "))
                    estoque = f_atualizar(estoque, id_busc, n_nome, n_preco)
                    salvar_dados(estoque)
                    print("✅ Produto atualizado!")
                else:
                    print("❌ ID não encontrado.")

            elif opcao == "4":
                id_rem = int(input("Digite o ID para remover: "))
                tamanho_antes = len(estoque)
                estoque = f_remover(estoque, id_rem)
                
                if len(estoque) < tamanho_antes:
                    salvar_dados(estoque)
                    print("✅ Produto removido.")
                else:
                    print("❌ ID não encontrado.")

            elif opcao == "5":
                total = f_calcular_total(estoque)
                print(f"\n💰 Valor total do inventário: R$ {total:.2f}")

            else:
                print("⚠️ Opção inválida!")

        except ValueError:
            print("\n❌ ERRO: Digite valores numéricos válidos para Preço ou ID.")
        except Exception as e:
            print(f"\n❌ Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    sistema_cadastro()