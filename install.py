from database.connection import get_connection

def install():
    connection = get_connection()

    try:
        # Criar tabela no banco de dados
        pass
            
        
            
        
        # Inserir dados iniciais (OBRIGATÓRIO!!!!)
        
        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")