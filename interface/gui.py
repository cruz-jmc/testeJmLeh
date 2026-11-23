from service.services import Services

class UI:

    def __init__(self, services):
        self.services = services

    def show_principal_menu(self):
=======
        # Exibir opções
        # Receber escolha do usuário
        # Chamar os métodos do service
        print("1. Docinhos")
        print("2. Bolos")
        resposta = input("Selecione para qual menu você quer ser redirecionado:")
        
        if resposta == 1:
            while True:

                print("====================MENU DE DOCINHOS====================")

                print("CADASTRAR -> 1")
                print("LISTAR -> 2")
                print("BUSCAR POR ID -> 3")
                print("ATUALIZAR -> 4")
                print("DELETAR -> 5")
                print("SAIR -> 6")

                escolha = input("O que deseja fazer? R:")
                
                if escolha == 1:
                    nome = input( "Digite o nome do docinho a ser cadastrado: ")
                    nome = input( "Digite o sabor do docinho a ser cadastrado: ")
                    
                    try:
                        docinho = self.services.create(nome, sabor)
                        print(f"Docinho cadastrado com sucesso! Id: {docinho.id}")
                        
                    except ValueError as error:
                        print(f"Erro: {error}")
                
        if resposta == 2:
            # menu de bolos
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
