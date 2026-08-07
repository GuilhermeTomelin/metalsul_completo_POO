from datetime import date
from database.conexao import Conexao
from models.funcionario import Funcionario
from repositories.funcionario_repository import FuncionarioRepository

'''
def main():
    conexao = Conexao()
    print("\033[031mConexão realizada com sucesso!\033[m")

    conexao.fechar()
'''

def main():

    repository = FuncionarioRepository()
    funcionario = repository.buscar_por_id(3)

    if funcionario:
        print(funcionario)
    else:
        print("Funcionário não encontrado!")
    repository.fechar()



if __name__ == "__main__":
    main()