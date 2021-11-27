import MySQLdb # conecta com o MySQL Server


def conectar():   # função que fará a conexão com MySQL 
   try:
       conn = MySQLdb.connect(
           database = "pmysql",
           host = "localhost",
           user = "marcio",
           passwd = "rocha")
       return conn
    except psycopg2.Error as e:
        print(f'Erro na conexão MySQL Server: {e}')

# Para testar este trecho usa-se:

# from utils import conectar
# conn = conectar()


def desconectar(conn): # Função para desconectar do servidor
    if conn:
        conn.close()
  


def listar():   # Função para listar os elementos do banco
    conn = conectar() #fazendo a conexão
    cursor = conn.cursor() #criando um cursor que irá executar as querys
    cursor.execute("SELECT * FROM produtos") # query a ser executada
    produtos = cursor.fetchall() # transformando em uma lista

    if len(produtos)> 0: #verifica se há elementos na lista
        print("Listando produtos...")
        print("--------------------------------------------------------")
        for produto in produtos: #percorre a lista
            print(f'ID:{produto[0]}')
            print(f'Produto:{produto[1]}')
            print(f'Preco:{produto[2]}')
            print(f'Estoque:{produto[3]}')
            print("-----------------------------------------")

    else:
        print("Não existem produtos cadastrado")
    
    desconectar(conn)

def inserir():
    conn = conectar()
    cursor = conn.cursor()

    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do produto: '))
    estoque = int(input('Informe a quantidade em estoque: '))

    #Inserindo elementos no banco de dados

    cursor.execute(f"INSERT INTO produtos(nome, preco, estoque) VALUES ('{nome}', {preco}, {estoque})")

    conn.commit() #concluindo a transação

    if cursor.rowcount == 1: # Confirmando se o dado foi inserido com sucesso
        print(f'O produto {nome} foi inserido com sucesso.')
    else:
        print('Não foi possível inserir o produto.')
    
    desconectar(conn)




def atualizar(): # Função que faz a atulização no banco de dados.
    conn = conectar()
    cursor = conn.cursor()

    id = int(input('Informe o ID do produto: ')) # Sempre ao utilizar o update ou delete devemos especificar em qual elemento queremos trabalhar.
    nome = input('Informe o novo nome do produto: ')
    preco = float(input('Informe o nome preço do produto: '))
    estoque = int(input('Informe a nova quantidade em estoque: '))

    cursor.execute(f'UPDATE produtos SET nome = "{nome}", {preco}, {estoque} WHERE id = {id} ')

    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto {nome} foi atulizado com sucessor.')
    else:
        print('Ocorreu um erro ao atualizar o produto.')
    
    desconectar(conn)

def deletar(): # deletando um elemento do banco de dados

    conn = conectar()
    cursor = conn.cursor()

    id = int(input('Informe o ID do produto: '))

    cursor.execute(f'DELETE FROM produtos WHERE id = {id}') # sempre usando o WHERE para especificar

    conn.commit()
   
   if cursor.rowcount == 1:
        print('O produto foi delatado com sucesso.')

   else:
        print('Ocorreu um erro ao deletar o produto.')

def menu():  # Esta função irá gerar o menu inicial no qual o usuário poderá escolher a operação a ser realizada.
    
    print('=========Gerenciamento de Produtos==============')
    print('Selecione uma opção: ')
    print('1 - Listar produtos.')
    print('2 - Inserir produtos.')
    print('3 - Atualizar produto.')
    print('4 - Deletar produto.')
    opcao = int(input())
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')