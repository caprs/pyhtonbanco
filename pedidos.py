import mysql.connector
try:
    connection = mysql.connector.connect(
        host = "localhost",
        user = "rost",
        password = "123456",
        database = "teste",
    )

    id_produto = str(input("Digite o Id do produto: "))
    nome = str(input("Digite o nome do produto: "))
    preco_unit = str(input("Digite o preço do produto: "))
    custo_unit = str(input("Digite o custo do produto: "))
    marca = str(input("Digite a marca do produto"))

    sql = "INSERT INTO pedidos (id_produto, nome, preco_unit, custo_unit, marca) VALUES (%s, %s, %s, %s, %s);"
    cursor = connection.cursor()
    cursor.execute(sql,(id_produto, nome, preco_unit, custo_unit, marca))
    connection.commit()
    cursor.close()
    connection.close()

except Exception as e:
    print(f"Erro ao salvar os dados: {e}")


