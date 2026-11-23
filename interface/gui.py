from service.services import Services

class UI:

    def __init__(self, services):
        self.services = services

    def show_principal_menu(self):
        while True:
         print("=======MENU DE BOLO======")
         print("CADASTRAR 1")
         print("LISTAR TODOS 2")
         print("SAIR 3")

         resposta = input("Digite a resposta")

         if resposta == "1":
            print("CADASTRO")
            nome = input("Digite o nome:")
            sabor = input("Digite o sabor:")
            try:
               bolo = self.services.create(nome, sabor)
               print(f"Cadastrado! id = {bolo.id}")
            except:
               print("Erro")
         if resposta == "2":
            print("LISTAR TODOS")
            try:
               resposta = self.services.list()
               for i in resposta:
                   print(f"nome: {i.nome}// sabor: {i.sabor}// feito: {i.feito}// id: {i.id}")
            except:
               print("Erro")
         if resposta == "3":
            print("Saindo do sistema....")
            break