from repository.dao_entity import DAOEntity
from entities.docinho import Docinho

class Services:

    def __init__(self, repository):
        self.repository = repository

    def create(self, nome, sabor):
        # Validar dados (MUITO IMPORTANTE!!!!!)
        # Criar entidade
        # Solicitar persistência
        pass
        

    def list(self):
        pass

    def get(self, docinho_id):
        pass
        

    def update(self, docinho_id, nome, sabor):
        pass
        
            
            
    def delete(self, docinho_id):
        pass