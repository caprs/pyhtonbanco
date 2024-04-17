import mysql.connector
from tabulate import tabulate

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="teste",
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM clientes")

resultadosclientes = cursor.fetchall()

for resultado in resultadosclientes:
    print(tabulate(resultadosclientes, headers=[], tablefmt='grid'))


cursor.execute("SELECT * FROM produtos")

resultadosprodutos = cursor.fetchall()

for resultado in resultadosprodutos:
    print(tabulate(resultadosprodutos, headers=[], tablefmt='grid'))

idvendas = str(input("Digite o id das vendas: "))
id_cliente = str(input("Digite o id do cliente: "))
id_produto = str(input("Digite o id do produto: "))
total_venda = str(input("Digite o total da venda: "))

sql = "INSERT INTO vendas (idvendas,id_cliente,id_produto,total_venda) VALUES (%s,%s,%s,%s);"

cursor.execute(sql,(idvendas,id_cliente,id_produto,total_venda))
connection.commit()

cursor.close()
connection.close()