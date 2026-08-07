-- Active: 1786137889080@@127.0.0.1@5432@metalsul
INSERT INTO funcionario (
    nome, cpf, rg, data_nascimento, sexo, estado_civil, 
    email, telefone, celular, cargo, departamento, 
    salario, data_admissao, turno, status
) VALUES (
    'Carlos Silva', '12345678901', '1234567', '1985-05-15', 'M', 'Casado',
    'carlos.silva@email.com', '4733710000', '47999998888', 'Soldador', 'Produção',
    3500.00, '2023-01-10', 'Manhã', 'ATIVO'
);