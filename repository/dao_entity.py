from database.connection import get_connection
from entities.docinho import Docinho

class DAOEntity:

    def create(self, bolo):
        connection = get_connection()
        
        try:
            cursor = connection.execute("""INSERT INTO bolo (nome, sabor, feito) VALUES (?,?,?)""", (bolo.nome, bolo.sabor, bolo.feito))
            connection.commit()
            return cursor.lastrowid
        finally:
            connection.close
            
       

    def find_all(self):
        # Consultar todas as entidades
        pass

    def find_by_id(self, docinho_id):
        # Consultar pelo ID
        pass

    def update(self, docinho):
        # Atualizar
        pass

    def delete(self, docinho_id):
        # Excluir
        pass