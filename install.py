from database.connection import get_connection

def install():
    connection = get_connection()

    try:
        connection.execute("""CREATE TABLE IF NOT EXISTS bolo 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome TEXT NOT NULL, sabor TEXT NOT NULL, 
        feito BOOLEAN DEFAULT 0)""")

        resultado = connection.execute("SELECT COUNT(*) FROM bolo")
        resposta = resultado.fetchone()[0]
        if resposta == 0:
            connection.execute("""INSERT INTO bolo (nome, sabor, feito) 
            VALUES (?, ?, ?)""", 
            ("mornango do amor", "morango com baunilha", False))
        
        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")