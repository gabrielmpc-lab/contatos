import sqlite3

def conexao_banco():
    conexao = sqlite3.connect("contatos.db")

    cursor = conexao.cursor()

    sql = '''
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL,
        email TEXT NOT NULL
    );'''
    cursor.execute(sql)
    conexao.commit()
    return conexao

def adicionar_contato(nome, telefone, email):
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = '''
    INSERT INTO contatos (nome, telefone, email)
    VALUES (?, ?, ?);'''
    cursor.execute(sql, (nome, telefone, email))
    conexao.commit()
    conexao.close()

def listar_contatos():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM contatos;"
    cursor.execute(sql)
    contatos = cursor.fetchall()
    conexao.close()

    if len(contatos) == 0:
        print("Nenhum contato encontrado.")
    else:
        print("---> LISTA DE CONTATOS <---")
        print(f"{'ID':<5} | {'Nome':<20} | {'Telefone':<15} | {'Email':<30}")
        print("-" * 60)
        for contato in contatos:
            print(f"{contato[0]:<5} | {contato[1]:<20} | {contato[2]:<15} |{contato[3]:<30}")

def buscar_contato():
    nome = input("Digite o nome do contato que deseja buscar: ")
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM contatos WHERE nome LIKE ?;"
    cursor.execute(sql, ('%' + nome + '%',))
    contatos = cursor.fetchall()
    conexao.close()

    if len(contatos) == 0:
        print("Nenhum contato encontrado com esse nome.")
    else:
        print("---> RESULTADO DA BUSCA <---")
        print(f"{'ID':<5} | {'Nome':<20} | {'Telefone':<15} | {'Email':<30}")
        print("-" * 60)
        for contato in contatos:
            print(f"{contato[0]:<5} | {contato[1]:<20} | {contato[2]:<15} |{contato[3]:<30}")

def atualizar_contato():
    nome = input("Digite o nome do contato que deseja atualizar: ")
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM contatos WHERE nome LIKE ?;"
    cursor.execute(sql, ('%' + nome + '%',))
    contatos = cursor.fetchall()

    if len(contatos) == 0:
        print("Nenhum contato encontrado com esse nome.")
    else:
        print("---> RESULTADO DA BUSCA <---")
        print(f"{'ID':<5} | {'Nome':<20} | {'Telefone':<15} | {'Email':<30}")
        print("-" * 60)
        for contato in contatos:
            print(f"{contato[0]:<5} | {contato[1]:<20} | {contato[2]:<15} |{contato[3]:<30}")

        id_contato = input("Digite o ID do contato que deseja atualizar: ")
        novo_nome = input("Digite o novo nome do contato: ")
        novo_telefone = input("Digite o novo telefone do contato: ")
        novo_email = input("Digite o novo email do contato: ")

        sql_update = '''
        UPDATE contatos
        SET nome = ?, telefone = ?, email = ?
        WHERE id = ?;'''
        cursor.execute(sql_update, (novo_nome, novo_telefone, novo_email, id_contato))
        conexao.commit()
        conexao.close()
        print("Contato atualizado com sucesso!")

def remover_contato():
    nome = input("Digite o nome do contato que deseja remover: ")
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = "SELECT * FROM contatos WHERE nome LIKE ?;"
    cursor.execute(sql, ('%' + nome + '%',))
    contatos = cursor.fetchall()

    if len(contatos) == 0:
        print("Nenhum contato encontrado com esse nome.")
    else:
        print("---> RESULTADO DA BUSCA <---")
        print(f"{'ID':<5} | {'Nome':<20} | {'Telefone':<15} | {'Email':<30}")
        print("-" * 60)
        for contato in contatos:
            print(f"{contato[0]:<5} | {contato[1]:<20} | {contato[2]:<15} |{contato[3]:<30}")

        id_contato = input("Digite o ID do contato que deseja remover: ")
        sql_delete = "DELETE FROM contatos WHERE id = ?;"
        cursor.execute(sql_delete, (id_contato,))
        conexao.commit()
        conexao.close()
        print("Contato removido com sucesso!")

def menu ():
    while True:
        print("---> CONTATOS <---")
        print("1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Buscar contato pelo nome")
        print("4 - Atualizar contato")
        print("5 - Remover contato")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o email do contato: ")
            adicionar_contato(nome, telefone, email)
            print("Contato adicionado com sucesso!")

        elif opcao == "2": 
            listar_contatos()
        elif opcao == "3":
            buscar_contato()
        elif opcao == "4":
            atualizar_contato()
        elif opcao == "5":
            remover_contato()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()