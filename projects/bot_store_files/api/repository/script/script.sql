-- Banco de Dados MySQL
-- Apagar o banco de dados
drop database db_store_files;

-- Criar o banco de dados
create database db_store_files;

-- Atribuir os privilégios de acesso aos objetos do banco
-- para o usuário root
GRANT ALL PRIVILEGES ON db_store_files.* TO 'root' @'localhost';

-- Acesar o banco de dados: banco
USE db_store_files;

-- Criar a tabela: produto
CREATE TABLE product(
    id int AUTO_INCREMENT,
    name varchar(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    category varchar(20) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE order(
    id int AUTO_INCREMENT
    -- See how to-do attributes
    PRIMARY KEY (id)
);
