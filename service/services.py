from repository.dao_entity import DAOEntity
from entities.bolo import Bolo

class Services:

    def __init__(self, repository):
        self.repository = repository

    def create(self, nome, sabor):
       if not nome or not nome.strip():
           raise ValueError("Erro")
       if not sabor or not sabor.strip():
           raise ValueError("Erro")
        
       bolo = Bolo()
       bolo.nome = nome.strip()
       bolo.sabor = sabor.strip()
       bolo.feito = False
       bolo.id = self.repository.create(bolo)
       return bolo
        
        

    def list(self):
        return self.repository.find_all()

    def get(self, docinho_id):
        pass
        

    def update(self, docinho_id, nome, sabor):
        pass
        
            
            
    def delete(self, docinho_id):
        pass