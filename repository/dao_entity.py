from database.connection import get_connection
from entities.bolo import Bolo

class DAOEntity:

    def create(self, bolo):
        connection = get_connection()
        
        try:
            cursor = connection.execute("""INSERT INTO bolo (nome, sabor, feito) VALUES (?,?,?)""", (bolo.nome, bolo.sabor, bolo.feito))
            connection.commit()
            return cursor.lastrowid
        finally:
            connection.close()
            
       

    def find_all(self):
        connection = get_connection()
        
        try:
            cursor = connection.execute("SELECT * FROM bolo")
            
            lista = cursor.fetchall()
            
            registro = []
            for i in lista:
                bolo = Bolo()
                bolo.id = i[0]
                bolo.nome = i[1]
                bolo.sabor = i[2]
                bolo.feito = i[3]
                
                registro.append(bolo)
            return registro
        finally:
            connection.close()

    def find_by_id(self, docinho_id):
        # Consultar pelo ID
        pass

    def update(self, docinho):
        # Atualizar
        pass

    def delete(self, docinho_id):
        # Excluir
        pass