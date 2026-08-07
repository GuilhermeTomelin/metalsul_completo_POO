from database.conexao import Conexao
from datetime import date
from models.funcionario import Funcionario
from repositories.funcionario_repository import FuncionarioRepository


def main():
    funcionario = Funcionario(
        nome = "Carlos Fabío",
        cpf = "123.123.123.12",
        rg = "123.123.12",
        data_nascimento= date(2001,12,1),
        sexo = "Macho",
        estado_civil= "Casado",
        email= "carlos_fabio@gmail.com",
        telefone= "47 9712-3582",
        celular= "Iphone",
        cargo= "chefe de TI",
        departamento= "Centro WEg",
        salario= "12000.00",
        data_admissao= date(2020, 4, 23),
        data_demissao= date(2023,12,3),
        turno = "Primeiro",
        status= "Ativo",
        observacoes= "Funcionario Top!",
    )
    repository = FuncionarioRepository() #Criação de um objetivo chamado repository
    repository.salvar(funcionario) #Salvar
    repository.fechar()
    
if __name__ == "__main__":
    main()
