import mysql.connector
from tabulate import tabulate


try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="teste",
    )

    cursor = connection.cursor()



    print(f"(1) Cadastrar cliente")
    print(f"(2) Cadastrar produto")
    print(f"(3) Fazer venda")
    print(f"(4) Listar produto")
    print(f"(5) Listar cliente")
    print(f"(6) Listar vendas")

    menu = int(input("Digite a opcao"))

    if menu == 1:
        nome = str(input("Digite seu nome: "))
        email = str(input("Digite seu email: "))
        cel = str(input("Digite seu celular: "))

        sql = "INSERT INTO clientes (nome, email, telefone) VALUES (%s,%s,%s);"
        cursor.execute(sql,(nome, email, cel))
        connection.commit()
        

    elif menu == 2:
        
        nome = str(input("Digite o nome do produto: "))
        preco_unit = str(input("Digite o preço do produto: "))
        custo_unit = str(input("Digite o custo do produto: "))
        marca = str(input("Digite a marca do produto"))
        sql = "INSERT INTO produtos (nome, preco_unit, custo_unit, marca) VALUES ( %s, %s, %s, %s);"
        cursor.execute(sql,(nome, preco_unit, custo_unit, marca))
        connection.commit()
        

    elif menu == 3:
        cursor.execute("SELECT * FROM clientes")

        resultadosclientes = cursor.fetchall()

        for resultado in resultadosclientes:
            print(tabulate(resultadosclientes, headers=[], tablefmt='grid'))


        cursor.execute("SELECT * FROM produtos")

        resultadosprodutos = cursor.fetchall()

        for resultado in resultadosprodutos:
            print(tabulate(resultadosprodutos, headers=[], tablefmt='grid'))

        
        id_cliente = str(input("Digite o id do cliente: "))
        id_produto = str(input("Digite o id do produto: "))
        total_venda = str(input("Digite o total da venda: "))

        sql = "INSERT INTO vendas (id_cliente,id_produto,total_venda) VALUES (%s,%s,%s);"

        cursor.execute(sql,(id_cliente,id_produto,total_venda))
        connection.commit()

    elif menu == 4:
        cursor.execute("SELECT * FROM produtos")
        resultadosprodutos = cursor.fetchall()

        print(f"Informações de produto: ")
        for resultado in resultadosprodutos:
            print(f"{resultado}") 
    
    elif menu == 5:
        cursor.execute("SELECT * FROM clientes")
        resultadosclientes = cursor.fetchall()

        print(f"Informações dos clientes: ")
        for resultado in resultadosclientes:
            print(f"{resultado}")

    elif menu == 6:
        cursor.execute("SELECT * FROM vendas")
        resultadosVendas = cursor.fetchall()

        print("informações de vendas: ")
        for resultado in resultadosVendas:
            print(f"{resultado}")
    
    else:
        print("Opção inválida")

    cursor.close()
    connection.close()
    
except Exception as e:
    print(f"Erro ao salvar os dados: {e}")