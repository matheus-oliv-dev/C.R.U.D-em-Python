import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

def conectar_banco():
    """Estabelece a conexão com o banco de dados."""
    load_dotenv()
    try:
        conexao = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        return conexao
    except Error as e:
        print(f"❌ Erro ao conectar ao banco de dados: {e}")
        return None

def cadastrar_produto(cursor, conexao):
    try:
        nome_produto = input("Digite o nome do produto: ")
        valor = float(input("Digite o valor do produto: "))
        
        comando = "INSERT INTO vendas (nome_produto, valor) VALUES (%s, %s)"
        valores = (nome_produto, valor)
        cursor.execute(comando, valores)
        conexao.commit()
        print(f"✅ Produto '{nome_produto}' cadastrado com sucesso!")
    except ValueError:
        print("❌ Erro: O valor digitado para o preço é inválido. Use números, e ponto para centavos (ex: 10.50).")
    except Error as e:
        print(f"❌ Erro no banco de dados ao cadastrar: {e}")

def listar_produtos(cursor):
    try:
        comando = 'SELECT * FROM vendas'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        
        print("\n--- Lista de produtos ---")
        if not resultado:
            print("Nenhum produto encontrado no banco de dados.")
            return

        for x in resultado:
            # Assumindo que a coluna 0 é o ID, 1 é o nome, e 2 é o valor
            # Verifique se a sua tabela segue essa estrutura
            id_prod = x[0]
            nome = x[1]
            valor = x[2]
            print(f"ID: {id_prod} | Produto: {nome} | Valor: R$ {valor:.2f}")
    except Error as e:
        print(f"❌ Erro no banco de dados ao listar: {e}")
    except IndexError:
        print(f"❌ Erro ao exibir: Formato inesperado das colunas da tabela. Dados brutos recebidos: {x}")

def atualizar_produto(cursor, conexao):
    try:
        id_produto = int(input("Digite o ID do produto que deseja atualizar: "))
        novo_valor = float(input("Digite o NOVO valor do produto: "))
        
        comando = "UPDATE vendas SET valor = %s WHERE id = %s"
        valores = (novo_valor, id_produto)
        cursor.execute(comando, valores)
        conexao.commit()
        
        # rowcount indica quantas linhas foram afetadas no banco
        if cursor.rowcount > 0:
            print("✅ Produto atualizado com sucesso!")
        else:
            print("⚠️ Nenhum produto encontrado com este ID.")
    except ValueError:
        print("❌ Erro: Entrada inválida. Certifique-se de digitar apenas números corretos para ID e valor.")
    except Error as e:
        print(f"❌ Erro no banco de dados ao atualizar: {e}")

def deletar_produto(cursor, conexao):
    try:
        id_produto = int(input("Digite o ID do produto para deletar: "))
        
        comando = "DELETE FROM vendas WHERE id = %s"
        valores = (id_produto,)
        cursor.execute(comando, valores)
        conexao.commit()
        
        if cursor.rowcount > 0:
            print("✅ Produto removido com sucesso!")
        else:
            print("⚠️ Nenhum produto encontrado com este ID.")
    except ValueError:
        print("❌ Erro: O ID deve ser um número inteiro.")
    except Error as e:
        print(f"❌ Erro no banco de dados ao deletar: {e}")

def main():
    conexao = conectar_banco()
    if not conexao:
        # Sai do programa se não conseguiu conectar
        return
        
    cursor = conexao.cursor()
    print("Banco conectado com sucesso!")

    while True:
        print("\n" + "="*30)
        print("SISTEMA DE VENDAS")
        print("="*30)
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Atualizar produto")
        print("4 - Deletar produto")
        print("5 - Sair")
        print("="*30)

        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Por favor, digite apenas números.")
            continue

        if opcao == 1:
            cadastrar_produto(cursor, conexao)
        elif opcao == 2:
            listar_produtos(cursor)
        elif opcao == 3:
            atualizar_produto(cursor, conexao)
        elif opcao == 4:
            deletar_produto(cursor, conexao)
        elif opcao == 5:
            print("Saindo do sistema...")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")

    # Fecha a conexão ao sair do programa
    cursor.close()
    conexao.close()
    print("Conexão encerrada.")

if __name__ == "__main__":
    main()