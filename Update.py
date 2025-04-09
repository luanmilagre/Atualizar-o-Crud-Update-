# Importar a biblioteca
import mysql.connector

# Conexão com o MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Luanmilagre.123",
    database="teste"
)
cursor = conexao.cursor()

#Produto a ser atualizado
nome_produto = "chocolate"
valor = 5

# Comando SQL para atualizar dados
comando = "UPDATE vendas SET valor = %s WHERE nome_produto = %s"

# Dados que serão inseridos no comando
dados = (valor, nome_produto)

# Executa o comando
cursor.execute(comando, dados)
conexao.commit()  # Confirma as alterações no banco de dados

# Fecha a conexão
cursor.close()
conexao.close()
