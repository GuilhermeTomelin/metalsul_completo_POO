from repositories.funcionario_repository import FuncionarioRepository

def main():
    print("Iniciando o processo de exclusão...")
    repository = FuncionarioRepository()

    repository.excluir(1)

    repository.fechar()
    print("Conexão fechada e programa finalizado.")

if __name__ == "__main__":
    main()
