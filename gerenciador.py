import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="0612"
    )

    with conn:
        with conn.cursor() as cursor:
            cod_entrada = input("O que você deseja?\n 1 - Consultar Senhas\n 2 - Cadastrar Senha\n\n")

            try:
                cod_entrada = int(cod_entrada)
            except ValueError:
                print("Por favor, digite um valor inteiro válido.")
                exit()

            if cod_entrada != 1 and cod_entrada != 2:
                print("Insira um valor válido.")
            elif cod_entrada == 2:
                nome = input("Informe o nome do App ou Site: ")
                senha = input("Informe a senha: ")

                cursor.execute("INSERT INTO armazenadados (nome, senha) VALUES (%s, %s)", (nome, senha))
                conn.commit()

                print("Nova senha adicionada com sucesso para o app/site: {0}".format(nome))
            else:
                cursor.execute("SELECT * FROM armazenadados")
                senhasSalvas = cursor.fetchall()
                if len(senhasSalvas) == 0:
                    print("Não há senhas salvas.")
                else:
                    print("Senhas Salvas:")
                    for senha in senhasSalvas:
                        print(f"Nome: {senha[0]}, Senha: {senha[1]}")
            input("\nPressione Enter para sair...")


except psycopg2.Error as error:
    print("Ocorreu um erro durante a conexão com o banco de dados: {0}".format(error))
