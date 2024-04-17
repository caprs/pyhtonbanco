import mysql.connector
from tabulate import tabulate

# Conectando ao banco de dados
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="banco",
)

# Criar um cursor
cursor = connection.cursor()

# Executar o SELECT
cursor.execute("SELECT * FROM pedidos WHERE Custo_Venda > 500")

# Obtenha os resultados
resultados = cursor.fetchall()

# Feche o cursor e a conexão
cursor.close()
connection.close()

# Formatando os resultados em uma lista de listas
tabela_resultados = [list(resultado) for resultado in resultados]

# Imprimir os resultados em forma de tabela
print(tabulate(tabela_resultados, headers=cursor.column_names, tablefmt="grid"))
