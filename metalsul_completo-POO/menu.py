from repositories.funcionario_repository import FuncionarioRepository


class Menu:
    def __init__(self):
        self.repository = FuncionarioRepository()

    def exibir(self):
        while True:
            print()
            print("-"*60)
            print("METALSUL - SISTEMA DE GERENCIAMENTO")
            print("-"*60)
            print("1 - Cadastrar Funcionario")
            print("2 - Buscar Funcionario")
            print("3 - Listar Funcioanrio")
            print("4 - Atualizar Funcionario")
            print("5 - Excluir Funcionario")
            print("0 - Sair")
            print("="*60)

            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.cadastrar_funcionario()

            elif opcao == "2":
                self.buscar_funcionario()

            elif opcao == "3":
                self.listar_funcionario()

            elif opcao == "4":
                self.atualizar_funcionario()

            elif opcao == "5":
                self.excluir_funcionario()
            
            elif opcao == "0":
                self.repository.fechar()
                print()
                break
            
    def cadastrar_funcionario(self):
        pass

    def buscar_funcionario(self):
        pass

    def listar_funcionario(self):
        pass

    def atualizar_funcionario(self):
        pass

    def excluir_funcionario(self):
        pass
