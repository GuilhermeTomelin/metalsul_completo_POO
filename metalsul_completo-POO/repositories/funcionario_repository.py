from database.conexao import Conexao
#from database.conexao import Conexao
from models.funcionario import Funcionario
from repositories.funcionario_repository import Funcionario

class FuncionarioRepository:
    def __init__(self):
        self.db = Conexao()
    def salvar(self, funcionario):
        sql = """
        INSERT INTO funcionario
        (

            nome,

            cpf,

            rg,

            data_nascimento,

            sexo,

            estado_civil,

            email,

            telefone,

            celular,

            cargo,

            departamento,

            salario,

            data_admissao,

            data_demissao,

            turno,

            status,

            observacoes

        )

        VALUES
        (

            %s,%s,%s,%s,%s,%s,%s,%s,%s,

            %s,%s,%s,%s,%s,%s,%s,%s

        )
    """
        valores = ( 
            funcionario.nome,

            funcionario.cpf,

            funcionario.rg,

            funcionario.data_nascimento,

            funcionario.sexo,

            funcionario.estado_civil,

            funcionario.email,

            funcionario.telefone,

            funcionario.celular,

            funcionario.cargo,

            funcionario.departamento,

            funcionario.salario,

            funcionario.data_admissao,

            funcionario.data_demissao,

            funcionario.turno,

            funcionario.status,

            funcionario.observacoes
        )
        #bloco de tratamento de erro
        try:
            self.db.cursor.execute(sql, valores)
            self.db.commit()
            print("Funcionário salvo com sucesso!")
        except Exception as erro:
            self.db.rollback()
            print(f"Erro ao salvar funcionário: {erro}")

    def buscar_por_id(self, id_funcionario):
        def __init__(self):
                self.db = Conexao()

        sql = """
                SELECT id_funcionario, nome_funcionario from funcionario
                WHERE id_funcionario = %s
        """

        try:
            self.db.cursor.execute(sql, id_funcionario)
            registro = self.db.cursor.fetchone()
        except Exception as e:
            print("Funcionario nao encontrado")

    def buscar_por_id(self, id_funcionario):
        pass
    def listar(self):
        pass
    def atualizar(self, funcionario):
        pass
    def excluir(self, id_funcionario):
        pass
    def fechar(self):
        self.db.fechar()

