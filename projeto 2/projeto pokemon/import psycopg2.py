

# CÓDIGO SQL

# CREATE TABLE pokemon (
#  id SERIAL PRIMARY KEY,
#  nome VARCHAR(50),
#  tipo VARCHAR(50),
#  nivel INTEGER
# );

# CREATE TABLE treinador (
#  id SERIAL PRIMARY KEY,
#  nome VARCHAR(50),
#  cidade VARCHAR(50)
# );

# CREATE TABLE captura (
#  treinador_id INTEGER treinador(id),
#  pokemon_id INTEGER pokemon(id),
#  data_captura DATE,
#  PRIMARY KEY (treinador_id, pokemon_id)
# );

import psycopg2

def exibir_tabela(tabela):
    cur.execute(f"SELECT * FROM {tabela}")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def inserir_dados(tabela):
    nome = input("Digite o nome: ")
    tipo = input("Digite o tipo: ")
    nivel = int(input("Digite o nível: "))

    cur.execute(f"INSERT INTO {tabela} (nome, tipo, nivel) VALUES (%s, %s, %s)", (nome, tipo, nivel))
    conn.commit()
    print("Dados inseridos com sucesso!")

def atualizar_dados(tabela):
    id = int(input("Digite o ID do registro a ser atualizado: "))
    nome = input("Digite o novo nome: ")
    tipo = input("Digite o novo tipo: ")
    nivel = int(input("Digite o novo nível: "))

    cur.execute(f"UPDATE {tabela} SET nome = %s, tipo = %s, nivel = %s WHERE id = %s", (nome, tipo, nivel, id))
    conn.commit()
    print("Dados atualizados com sucesso!")

def remover_dados(tabela):
    id = int(input("Digite o ID do registro a ser removido: "))

    cur.execute(f"DELETE FROM {tabela} WHERE id = %s", (id,))
    conn.commit()
    print("Dados removidos com sucesso!")

# Estabelecer conexão com o banco de dados
conn = psycopg2.connect(
    host="localhost",
    database="tentativa",
    user="postgres",
    password="postgres"
)

# Criar um cursor para executar comandos SQL
cur = conn.cursor()

# Menu de navegação
while True:
    print("== MENU ==")
    print("1. Visualizar dados da tabela Pokémon")
    print("2. Visualizar dados da tabela Treinador")
    print("3. Inserir dados na tabela Pokémon")
    print("4. Inserir dados na tabela Treinador")
    print("5. Atualizar dados na tabela Pokémon")
    print("6. Atualizar dados na tabela Treinador")
    print("7. Remover dados na tabela Pokémon")
    print("8. Remover dados na tabela Treinador")
    print("0. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        exibir_tabela("pokemon")
    elif opcao == "2":
        exibir_tabela("treinador")
    elif opcao == "3":
        inserir_dados("pokemon")
    elif opcao == "4":
        inserir_dados("treinador")
    elif opcao == "5":
        atualizar_dados("pokemon")
    elif opcao == "6":
        atualizar_dados("treinador")
    elif opcao == "7":
        remover_dados("pokemon")
    elif opcao == "8":
        remover_dados("treinador")
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")

# Fechar a conexão com o banco de dados
cur.close()
conn.close()