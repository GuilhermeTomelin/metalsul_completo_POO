from database.conexao import Conexao
from datetime import date
from models.funcionario import Funcionario

def main():
    funcionario = Funcionario(
        nome = "Alanis da Silva", 
        cpf = "12345678998", 
        cargo = "TI dev",
        departamento = "TECH", 
        salario = 7000.00, 
        data_admissao = date.today()
    )
    print(funcionario)

if __name__ == "__main__":
    main()
