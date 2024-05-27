import mysql.connector

config = {                          # Substituir com a conexão ao banco de dados #   
    'user': 'root',                 # Nome do usuario do banco de dados #
    'password': 'adminadmin',       # Senha do usuario do banco de dados #
    'host': 'localhost',            # Host do banco de dados #
    'database': 'crud_example',     # Nome do banco de dados #
}

# Conectar ao banco de dados
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Função para criar um novo usuário
def create_user(name, email):
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    val = (name, email)
    cursor.execute(sql, val)
    conn.commit()
    print(f"Usuário {name} criado com sucesso!")

# Função para ler todos os usuários
def read_users():
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    for row in result:
        print(row)

# Função para atualizar um usuário
def update_user(user_id, name, email):
    sql = "UPDATE users SET name = %s, email = %s WHERE id = %s"
    val = (name, email, user_id)
    cursor.execute(sql, val)
    conn.commit()
    print(f"Usuário com ID {user_id} atualizado com sucesso!")

# Função para deletar um usuário
def delete_user(user_id):
    sql = "DELETE FROM users WHERE id = %s"
    val = (user_id,)
    cursor.execute(sql, val)
    conn.commit()
    print(f"Usuário com ID {user_id} deletado com sucesso!")

# Menu de operações CRUD
def menu():
    while True:
        try:
            choice = int(input("\nOperações CRUD\n1. Criar usuário\n2. Ler usuários\n3. Atualizar usuário\n4. Deletar usuário\n5. Sair\nEscolha uma opcao: "))
            if choice == 1:
                name = input("Nome: ")
                email = input("Email: ")
                create_user(name, email)
            elif choice == 2:
                read_users()
            elif choice == 3:
                user_id = int(input("ID do usuario: "))
                name = input("Novo nome: ")
                email = input("Novo email: ")
                update_user(user_id, name, email)
            elif choice == 4:
                user_id = int(input("ID do usuario: "))
                delete_user(user_id)
            elif choice == 5:
                break
            else:
                raise ValueError
        except ValueError:
            print("Escolha invalida!")

# Execução do menu
menu()

# Fechar a conexão com o banco de dados
cursor.close()
conn.close()
