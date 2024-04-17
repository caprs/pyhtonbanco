import mysql.connector
try:
    connection = mysql.connector.connect(
        host = "localhost",
        user = "rost",
        password = "123456",
        database = "teste",
    )

    nome = str(input("Digite seu nome: "))
    email = str(input("Digite seu email: "))
    cel = str(input("Digite seu celular: "))

    sql = "INSERT INTO clientes (nome, email, telefone) VALUES (%s,%s,%s);"
    cursor = connection.cursor()
    cursor.execute(sql,(nome, email, cel))
    connection.commit()
    cursor.close()
    connection.close()

except Exception as e:
    print(f"Erro ao salvar os dados: {e}")