from service.services import Services

class UI:

    def __init__(self, services):
        self.services = services

    def show_principal_menu(self):
        while True:
         print("=======MENU DE BOLO======")
         print("CADASTRAR 1")
         print("SAIR 2")

         resposta = input("Digite a resposta")

         if resposta == "1":
            print("CADASTRO")
            nome = input("Digite o nome:")
            sabor = input("Digite o sabor:")
            try:
               bolo = self.services.create(nome, sabor)
               print(f"Cadastrado! id = {bolo.id}")
            except ValueError as erro:
               print("Erro: {erro}")
         if resposta == "2":
            print("Saindo do sistema....")
            break